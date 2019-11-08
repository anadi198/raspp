#!/usr/bin/python
import os
import sys
import datetime
import time
import twitter
import requests, json 
from twilio.rest import Client
import urllib
import temp

ts = time.time()
date =datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

def alert_call(temp):
    account_sid = 'ACf0120c4257011023d579482537cea18b'
    auth_token = 'c7980cafd36ca09d131548c6f599259f'
    client = Client(account_sid, auth_token)
    call = client.calls.create(
                        url='https://handler.twilio.com/twiml/EH491cc671122a7ef2f0e4119276d90140?Temp='+urllib.parse.quote_plus(temp)+'&Date='+urllib.parse.quote_plus(date),
                        to='+919155343600',
                        from_='+12015844115'
                    )
    return

def tweet_it(info):
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

api_key = "e46eec2e93c497e58030ac1dceb351a6"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "Kalyani" 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
response = requests.get(complete_url) 
x = response.json() 
print (x)
if x["cod"] != "404": 
    y = x["main"] 
    current_temperature = y["temp"]
    rt_temp = temp.get_temp()
    wea = " Temperature (in Celsius) outside: " + str(current_temperature - 273.15) + " degrees\n Temperature (in celsius) inside: " + str(rt_temp) + " degrees\n"
    if(rt_temp>25):
            alert_call(str(rt_temp))
            wea += "HOTHOTHOT!"
    tweet_it(wea)
else: 
    print(" City Not Found ")
