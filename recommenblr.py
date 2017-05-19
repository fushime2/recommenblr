#
# print recommended urls.
#

from user_recommender import UserRecommender


def print_urls(users):
    BASE = "http://{}.tumblr.com/"
    for user in users:
        url = BASE.format(user)
        print(url)


def main():
    with open("conf.txt", "r") as f:
        ck, cs, token, token_secret = f.read().strip().split()

    ur = UserRecommender(ck, cs, token, token_secret)

    # make list of N recommended users
    N = 30
    users = ur.recommend(N)

    print_urls(users)


if __name__ == '__main__':
    main()
