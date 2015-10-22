from instagram.client import InstagramAPI

access_token = "7ef840b3ccb4480eb79ba40ab67de505"
client_secret = "e8336639f78444919b8b3f4c1ef0c326"
my_user_id = "176201887"

api = InstagramAPI(access_token=access_token, client_secret=client_secret)
recent_media, next_ = api.user_recent_media(user_id=my_user_id, count=10)
for media in recent_media:
   print media.caption.text
