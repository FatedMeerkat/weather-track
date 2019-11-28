import requests
import json

key = "yourkey"
url = "http://api.openweathermap.org/data/2.5/weather?"
city = "yourcity"
fullurl = url + "appid=" + key + "&q=" + city
response = requests.get(fullurl) 
spr = response.json() 

if spr["cod"] != "404": 
    spr2 = spr["main"]
    curtemp = spr2["temp"]
    curpres = spr2["pressure"]
    curhumi = spr2["humidity"]
    spr3 = spr["weather"]
    print("Temperature:", temp, "Pressure:", pressure)

else:
    print("No city found.")
