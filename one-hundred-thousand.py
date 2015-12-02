#!/usr/bin/env python
from instagram.client import InstagramAPI
import pyupm_grove as grove
import pyupm_uln200xa as upmULN200XA
import sys, time

access_token = "176201887.877f884.1cdbffd746974bb489a66c2b1df0e958"
client_secret = "e8336639f78444919b8b3f4c1ef0c326"
user_id = "201990584"

previous_number_of_followers = 0
previous_motor_position = 0

target_followers_lower_limit = 0
target_followers_upper_limit = 100000

# Stepper Motor
myUln200xa = None

# LED setup
green_led = grove.GroveLed(2)
red_led = grove.GroveLed(3)

# Instagram API setup
api = InstagramAPI(access_token = access_token, client_secret = client_secret)

# range mapper
def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return int(rightMin + (valueScaled * rightSpan))

while True:
    try:
        # Poll Instagram API
        user_info = api.user(user_id = user_id)

        # Parse received data
        number_of_followers = user_info.counts["followed_by"]
        myUln200xa = None
        # Update display when a change is detected
        if (number_of_followers != previous_number_of_followers and 
            number_of_followers >= target_followers_lower_limit and 
            number_of_followers <= target_followers_upper_limit):
            
            # LED control
            if (number_of_followers > previous_number_of_followers):
                green_led.on()
            elif (number_of_followers < previous_number_of_followers):
                red_led.on()
                
            # Motor position control
            motor_position = translate(number_of_followers, target_followers_lower_limit, target_followers_upper_limit, 0, 2048)
            if (motor_position != previous_motor_position):
                # Stepper motor setup
                myUln200xa = upmULN200XA.ULN200XA(4096, 8, 9, 10, 11)
                myUln200xa.setSpeed(5) # 5 RPMs
                
                motor_delta = motor_position - previous_motor_position
                if (motor_position > previous_motor_position):
                    myUln200xa.setDirection(upmULN200XA.ULN200XA.DIR_CCW)
                elif (motor_position < previous_motor_position):
                    myUln200xa.setDirection(upmULN200XA.ULN200XA.DIR_CW)
                
                # Rotate motor - abs() ensures number is always positive which is required by underlying library
                myUln200xa.stepperSteps(abs(motor_delta))
                # Release  motor otherwise it begins to heat up quite hot.
                myUln200xa.release()

            # Print outputs
            print "Followers: %s - Motor position: %s - %s" % (number_of_followers, motor_position, time.asctime(time.localtime(time.time())))
            previous_number_of_followers = number_of_followers
            previous_motor_position = motor_position

        # Sleep for 1 second then restart event cycle
        time.sleep(1)
        green_led.off()
        red_led.off()
    except KeyboardInterrupt:
        # Cleanup
        del green_led
        del red_led
        if 'myUln200xa' in globals() and myUln200xa is not None:
            myUln200xa.release()
        sys.exit(0)
