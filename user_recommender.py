from tumblr_manager import TumblrManager, TumblrScraper


class UserRecommender(object):
    user_counter = {}

    def __init__(self, consumer_key=None, consumer_secret=None, oauth_token=None, oauth_token_secret=None):
        self.tm = TumblrManager(consumer_key, consumer_secret, oauth_token, oauth_token_secret)
        self.ts = TumblrScraper(consumer_key, consumer_secret, oauth_token, oauth_token_secret)

    def recommend(self, n=20):
        """
        :param int n: number of users
        :return: a list including n users
        """
        self.set_counter()
        cnt = sorted(self.user_counter.items(), key=lambda x: x[1], reverse=True)
        users = [t[0] for t in cnt]
        return users[:n]

    def set_counter(self):
        url_list = self.tm.fetch_urls()
        all_users = self.ts.fetch_users_from_url(url_list)
        # non_followed_users = list(filter(lambda x: not self.tm.is_following(x), all_users))
        for user in all_users:
            self.add_user(user)

    def add_user(self, user):
        if user not in self.user_counter:
            self.user_counter[user] = 1
        else:
            self.user_counter[user] += 1
