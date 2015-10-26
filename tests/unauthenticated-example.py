#!/usr/bin/env python
from instagram.client import InstagramAPI

client_id = "877f884c9e4d40cf85031245d76a8593"
client_secret = "e8336639f78444919b8b3f4c1ef0c326"

api = InstagramAPI(client_id=client_id, client_secret=client_secret)
popular_media = api.media_popular(count=20)
for media in popular_media:
    print media.images['standard_resolution'].url
