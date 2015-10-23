#!/Users/dan/.virtualenvs/instagram-test/bin/python

# Sourced from: http://stackoverflow.com/questions/1969240/mapping-a-range-of-values-to-another
def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

#sensor_value = 256
#actuator_value = translate(sensor_value, 1, 512, 5, 10)
sensor_value = 12744
actuator_value = translate(sensor_value, 0, 100000, 0, 2048)
print actuator_value
