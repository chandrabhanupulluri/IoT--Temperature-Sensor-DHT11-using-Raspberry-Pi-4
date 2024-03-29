import RPi.GPIO as GPIO
import dht11 # dependecy file
import time
import datetime
# importing the requests library 
import requests

# Enter Your API key here - Register at ThingSpeak
myAPI = 'P3NIC8ZHRRFMBLKJ' 
# URL where we will send the data, Don't change it
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 21, check what GPIO you connected to for output specific that number to pin
instance = dht11.DHT11(pin=21)

try:
    while True:
        result = instance.read()
        if result.is_valid():
            
            print("Last valid input: " + str(datetime.datetime.now()))
            
            r = requests.get(baseURL + '&field1=%s&field2=%s' % (result.temperature, result.humidity))

            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)

        time.sleep(6)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()
