#!/usr/bin/env python
from instagram.client import InstagramAPI

# You need to fill out these 2 lines.
# Need to create and instagram dev account to get a client id and client secret
client_id = ""
client_secret = ""

api = InstagramAPI(client_id=client_id, client_secret=client_secret)
popular_media = api.media_popular(count=20)
for media in popular_media:
    print media.images['standard_resolution'].url
