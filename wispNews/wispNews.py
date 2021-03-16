#!/usr/bin/env python
import tweepy, sys, json
sys.path.append("./scripts")
from auth import authenticate

CONF_PATH = "./config/conf.json"

def get_conf():
    try:
        with open(CONF_PATH, 'r') as conf:
            keys = json.load(conf)
    except BaseException as e: print(f"[x] Error: {e}")
    else: return keys

if __name__ == '__main__':
    keys = get_conf()
    api = authenticate(keys)