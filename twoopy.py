#!/usr/bin/python
import os
import sys
import csv
import datetime
import time
import twitter
import requests, json 
from twilio.rest import Client
import urllib

ts = time.time()
date =datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

def alert_call(temp):
    # Your Account Sid and Auth Token from twilio.com / console 
    account_sid = 'ACf0120c4257011023d579482537cea18b'
    auth_token = 'c7980cafd36ca09d131548c6f599259f'
    
    client = Client(account_sid, auth_token) 
    
    ''' Change the value of 'from' with the number  
    received from Twilio and the value of 'to' 
    with the number in which you want to send message.'''
    call = client.calls.create(
                        url='https://handler.twilio.com/twiml/EH491cc671122a7ef2f0e4119276d90140?Temp='+urllib.parse.quote_plus(temp)+'&Date='+urllib.parse.quote_plus(date),
                        to='+918910161263',
                        from_='+12015844115'
                    )
    return

def tweet_it(info):
 
        #connect to twitter
        TOKEN="1863934028-FlSTcl5A3LXR6i8IEa7DLik3SVMnS7i0JPwMPv5"
        TOKEN_KEY="B4NjgbWxcyguPJRr5pHP0ER4Uollgt2dPdF6Ul57qWY9K"
        CON_SEC="vSqsklnipN3rEH0y7zC0tYc8n"
        CON_SEC_KEY="mlldzHpyx8kZS8nVzHDM3sR56Oo23i4Jv0y3tYajrv2TG06kSn"
 
        my_auth = twitter.OAuth(TOKEN,TOKEN_KEY,CON_SEC,CON_SEC_KEY)
        twit = twitter.Twitter(auth=my_auth)
        
        try:
                tweet=date+"\n"+"Weather info for Kalyani \n" +info
                twit.statuses.update(status=tweet)
        except Exception as e:
                print (e)
                pass
        return

# Enter your API key here 
api_key = "e46eec2e93c497e58030ac1dceb351a6"
  
# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
# Give city name 
city_name = "Kalyani" 
  
# complete_url variable to store 
# complete url address 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
  
# get method of requests module 
# return response object 
response = requests.get(complete_url) 
  
# json method of response object  
# convert json format data into 
# python format data 
x = response.json() 
print (x)
# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
if x["cod"] != "404": 
  
    # store the value of "main" 
    # key in variable y 
    y = x["main"] 
  
    # store the value corresponding 
    # to the "temp" key of y 
    current_temperature = y["temp"]
    # print following values 
    wea = " Temperature (in Celsius): " + str(current_temperature - 273.15) + " degrees\n"
    tweet_it(wea)
    alert_call(str(current_temperature-273.15))
else: 
    print(" City Not Found ")