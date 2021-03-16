#!/usr/bin/env python
import tweepy

def follow(api):
    print("[!] Retrieving followers...")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            print(f"[!] Following {follower.name}")
            follower.follow()

