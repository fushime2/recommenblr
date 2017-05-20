# recommenblr
Recommendation tools for Tumblr users.

Find users having similar preferences.

# Requirements
- Python 3
- BeautifulSoup 4
- [Tumblpy](https://github.com/michaelhelmick/python-tumblpy)
- consumer key, consumer secret, oauth token and oauth token secret of Tumblr
  - https://www.tumblr.com/oauth/apps

# Usage
1. Edit `conf.txt`

	set 4 lines `consumer key`, `consumer secret`, `oauth token` and `oauth token secret` in `conf.txt`

2. Run

	`python recommenblr.py`

	An example of output.
	```
    http://metyashiko.tumblr.com/
    http://sagiri-izumi.tumblr.com/
    http://dezaki.tumblr.com/
    http://man-nona.tumblr.com/
    http://hkdmz.tumblr.com/
    http://oworion.tumblr.com/
    http://0ni-chan.tumblr.com/
    http://zsaber.tumblr.com/
    http://simplykasumi.tumblr.com/
    http://relatablepicturesofwatanabeyou.tumblr.com/
    http://nonging.tumblr.com/
    http://aoiikawaii.tumblr.com/
    http://the-coffin-princess.tumblr.com/
    http://malmrashede.tumblr.com/
    http://girlslovemyping.tumblr.com/
	```

# License
MIT License