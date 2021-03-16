#!/usr/bin/env python
import tweepy

def authenticate(keys):
	auth = tweepy.OAuthHandler(keys['CONSUMER_KEY'], keys['CONSUMER_KEY_SECRET'])
	auth.set_access_token(keys['ACCESS_TOKEN'], keys['ACCESS_TOKEN_SECRET'])
	
	api = tweepy.API(
		auth,
		wait_on_rate_limit=True,
		wait_on_rate_limit_notify=True
	)

	try: api.verify_credentials()
	except BaseException as e: print("[x] Authentication Failed: {e}")
	else:
		print("[+] Authentication Succeeded!")
		return api