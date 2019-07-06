#!/usr/bin/python3
#-----------------------------------------------------------
#
#
# Author : Matt Hawkins
# Modified by: fezfox
# Modified more by: Shawn Peterson
#
#
#-----------------------------------------------------------
import time
import logging
import config as c
import poollib as p
import paho.mqtt.client as mqtt

#Clear log
p.silentRemove(c.BASEPATH + '/logs/main.log')

logFormat = '%(asctime)s %(levelname)s:%(message)s'
logging.basicConfig(format=logFormat, filename=c.BASEPATH + '/logs/main.log', level=logging.DEBUG)
logging.info('Main start')

# Get the IDs of the DS18B20 temp sensors
mySensorIDs = p.getSensorIDs()

#Set number of seconds to wait between loops before sending data
loopDelay = c.LOOPDELAY

mqtt_ip = p.getIp()

#Use a remote MQTT server when specified
if c.MQTTIP:
    mqtt_ip = c.MQTTIP

#Setup MQTT broker details
client = mqtt.Client("PoolMain")
client.username_pw_set("mqtt", c.MQTTPWORD)
client.connect(mqtt_ip, 1883, 60)
client.loop_start()

if __name__ == '__main__':

    while True:
        try:
            logging.info('Read temperatures')
            temps = p.readTemps(mySensorIDs)
            
            logging.info('Publish temperatures')

            for i in range(len(temps)):
                client.publish("pool/temperature/" + str(i+1), temps[i])
           
            # Wait before doing it all again
            time.sleep(loopDelay)
        except:
            quit()

    logging.info('Main end')
