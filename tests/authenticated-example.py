#!/usr/bin/env python
from instagram.client import InstagramAPI

# You need to fill out these 3 lines.
# Need to create and instagram dev account to get an access token and client secret
# Input instagram userID of the person you wish the box to monitor.
access_token = ""
client_secret = ""
my_user_id = ""

api = InstagramAPI(access_token=access_token, client_secret=client_secret)
recent_media, next_ = api.user_recent_media(user_id=my_user_id, count=10)
for media in recent_media:
   print media.caption.text
