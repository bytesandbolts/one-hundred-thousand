#!/Users/dan/.virtualenvs/instagram-test/bin/python
from instagram.client import InstagramAPI

access_token = "176201887.877f884.1cdbffd746974bb489a66c2b1df0e958"
client_secret = "e8336639f78444919b8b3f4c1ef0c326"
dan_user_id = "176201887"
laura_user_id = "201990584"

api = InstagramAPI(access_token=access_token, client_secret=client_secret)
user_info = api.user(user_id=laura_user_id)

print user_info.counts["followed_by"]