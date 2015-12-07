#!/usr/bin/env python
from instagram.client import InstagramAPI
import pyupm_grove as grove
import sys
import time

# You need to fill out these 3 lines.
# Need to create and instagram dev account to get an access token and client secret
# Input instagram userID of the person you wish the box to monitor.
access_token = ""
client_secret = ""
user_id = ""
previous_followers = 0

green_led = grove.GroveLed(2)
red_led = grove.GroveLed(3)

api = InstagramAPI(access_token=access_token, client_secret=client_secret)

while True:
    try:
        user_info = api.user(user_id=user_id)
        number_of_followers = user_info.counts["followed_by"]
        if number_of_followers != previous_followers:
            if number_of_followers > previous_followers and previous_followers != 0:
                green_led.on()
            elif number_of_followers < previous_followers and previous_followers != 0:
                red_led.on()
            print "Followers: %s - %s" % (number_of_followers, time.asctime(time.localtime(time.time())))
            previous_followers = number_of_followers
        time.sleep(1)
        green_led.off()
        red_led.off()
    except KeyboardInterrupt:
        del green_led
        del red_led
        sys.exit(0)
