#!/Users/dan/.virtualenvs/instagram-test/bin/python
from instagram.client import InstagramAPI
import sys
import time

access_token = "176201887.877f884.1cdbffd746974bb489a66c2b1df0e958"
client_secret = "e8336639f78444919b8b3f4c1ef0c326"

dans_user_id = "176201887"
lauras_user_id = "201990584"
user_id = lauras_user_id

previous_followers = 0

api = InstagramAPI(access_token=access_token, client_secret=client_secret)

while True:
    user_info = api.user(user_id=user_id)
    number_of_followers = user_info.counts["followed_by"]
    if number_of_followers != previous_followers:
        print "Followers: %s - %s" % (number_of_followers, time.asctime(time.localtime(time.time())))
        previous_followers = number_of_followers
    time.sleep(1)