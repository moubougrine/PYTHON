import os
import json
import urllib.request as urllib2

while True :
    ip = input("What's your target IP : ")
    url = "http://ip-api.com/json/"
    res = urllib2.urlopen(url + ip)
    data = res.read()
    value = json.loads(data)
    print("IP : " ,value["query"])
    print("Country : " ,value["country"])
    print("Region : " ,value["regionName"])
    print("City : " ,value["city"])
    print("Latitude : ", value["lat"])  
    print("Longitude : ", value["lon"])
    print("Timezone : " ,value["timezone"])
    print("Isp : " ,value["isp"])
    break