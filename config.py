#!/usr/bin/python3
# -----------------------------------------------------------
#
#
# Author : Matt Hawkins
# Modified by: fezfox
# Modified more by: Shawn Peterson
#
#
# -----------------------------------------------------------

BASEPATH = '/home/pi/PoolPi'

# Set the number of seconds between each loop.
# This determines how often the system checks the temperature.
LOOPDELAY = 300

# Default username and password hash "splishsplosh"
# Use hashgenerator.py in utils to create hash for your password
USERNAME = 'admin'
USERHASH = 'c7f9e589934a99848f2dba75a70b49dca6149988730389671d730e9376701adf'

# Flask needs a secret key or phrase to handle login cookie
FLASKSECRET = '7e8031df78fd55cba971df8d9f5740be'

# MQTT settings. MQTTIP allows you to utilize a remote MQTT server
MQTTIP = ''
MQTTPWORD = 'splishsplosh'
