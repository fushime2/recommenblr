import urllib.request
import urllib.parse
import re

from bs4 import BeautifulSoup

from tumblpy import Tumblpy


class TumblrManager(object):
    following_users = set()

    def __init__(self, consumer_key=None, consumer_secret=None, oauth_token=None, oauth_token_secret=None):
        if consumer_key is None or consumer_secret is None or oauth_token is None or oauth_token_secret is None:
            self.t = Tumblpy()
        else:
            self.t = Tumblpy(consumer_key, consumer_secret, oauth_token, oauth_token_secret)

    def fetch_urls(self, LIM=4):
        """
        Fetch urls from user's likes.
        If you want more urls, increase LIM range 1 to 50 (default 4).
        :return a list: including urls
        """
        post_urls = []
        for cnt in range(LIM):
            try:
                likes = self.t.post('user/likes', params={"offset": 20 * cnt})
            except:
                continue

            liked_posts = likes["liked_posts"]
            for liked_post in liked_posts:
                post_url = liked_post["post_url"]
                post_urls.append(self.format_url(post_url))

        return post_urls

    def fetch_all_following_users(self):
        # seek total_blogs
        following = self.t.post("user/following", params={"limit": 1})
        total_blogs = following["total_blogs"]

        users = set()
        for i in range(total_blogs // 20 + 2):
            blogs = self.fetch_blogs(offset=20 * i)
            for user in blogs:
                users.add(user)

        return users

    def fetch_blogs(self, offset=0):
        try:
            following = self.t.post("user/following", params={"offset": offset})
        except:
            return []
        blogs = following["blogs"]
        ret = [blog["name"] for blog in blogs]
        return ret

    def format_url(self, url):
        """
        :return str: formated url
        """
        try:
            p = url.find("post/")
            front = url[:p + 18]
            back = url[p + 18:]
            return_url = front + urllib.parse.quote_plus(back, encoding="utf-8")
            return return_url
        except:
            return ""

    def is_following(self, user):
        if not self.following_users:
            self.following_users = self.fetch_all_following_users()
        return user in self.following_users

    def is_valid_id(self, id):
        """ Return True if id is following a rule of user name.  """
        alnum_reg = re.compile(r'^[a-zA-Z0-9-]+$')
        return alnum_reg.match(id) is not None


class TumblrScraper(object):
    def __init__(self, consumer_key=None, consumer_secret=None, oauth_token=None, oauth_token_secret=None):
        self.tm = TumblrManager(consumer_key, consumer_secret, oauth_token, oauth_token_secret)

    def fetch_users_from_url(self, url_list):
        """
        Fetch non-following users from given urls.
        :param url_list:
        :return: users list
        """
        users_list = []
        for url in url_list:
            try:
                html = urllib.request.urlopen(url)
            except:
                continue

            soup = BeautifulSoup(html, "lxml")
            a_nofollow = soup.find_all("a", rel="nofollow")  # Table of reblog and likes
            for a in a_nofollow:
                user = a.string
                if self.can_add(user):
                    users_list.append(user)

        return users_list

    def can_add(self, user):
        if user is None: return False
        return self.tm.is_valid_id(user) and not self.tm.is_following(user)
