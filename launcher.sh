#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script
cd /home/pi/PoolPi
python3 /home/pi/PoolPi/poolmain.py &
python3 /home/pi/PoolPi/poolweb.py &