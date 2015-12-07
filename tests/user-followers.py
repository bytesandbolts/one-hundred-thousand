#!/usr/bin/env python
from instagram.client import InstagramAPI

# You need to fill out these 3 lines.
# Need to create and instagram dev account to get an access token and client secret
# Input instagram userID of the person you wish the box to monitor.
access_token = ""
client_secret = ""
user_id = ""

api = InstagramAPI(access_token=access_token, client_secret=client_secret)
user_info = api.user(user_id=user_id)

print user_info.counts["followed_by"]
