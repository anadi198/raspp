#!/usr/bin/python
import sys
import Adafruit_DHT

def get_temp():
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    return temperature
