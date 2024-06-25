#!/bin/python
#Get Your Location Using Your Public IP
import requests

URL=requests.get("https://api.ipify.org/?format=json")                
print(URL.text)
print (URL) #Making Sure of the Status

if URL.status_code==200:
    ip=URL.json()['ip'] #Storing the IP in a Variable
    print (ip) #Making Sure of the IP Passed to the Other Request
    Second_req=requests.get(f"https://ipinfo.io/{ip}/geo")
    if Second_req.status_code == 200:
        print(Second_req.text)
    else:
        print("Couldn't find the Location")
else:
    print("Couldn't find the IP")