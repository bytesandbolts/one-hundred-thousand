#!/usr/bin/env python
from instagram.client import InstagramAPI
import pyupm_grove as grove
import sys
import time

access_token = "176201887.877f884.1cdbffd746974bb489a66c2b1df0e958"
client_secret = "e8336639f78444919b8b3f4c1ef0c326"
dan_user_id = "176201887"
laura_user_id = "201990584"
previous_followers = 0

green_led = grove.GroveLed(2)
red_led = grove.GroveLed(3)

api = InstagramAPI(access_token=access_token, client_secret=client_secret)

while True:
    try:
        user_info = api.user(user_id=laura_user_id)
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
