import requests
import json
from tkinter import *
from flask import Flask

root = Tk()

key = "key"
url = "http://api.openweathermap.org/data/2.5/weather?"
city = "city"
fullurl = url + "appid=" + key + "&q=" + city
response = requests.get(fullurl) 
spr = response.json() 

if spr["cod"] != "404": 
    spr2 = spr["main"]
    curtemp = spr2["temp"]
    curpres = spr2["pressure"]
    curhumi = spr2["humidity"]
    spr3 = spr["weather"]
    temperature = "Temperature:", curtemp - 272.15,"C"
    pressure = "Pressure:", curpres,"hPa"
    humidity = "Humidity:", curhumi,"%"
    print("Temperature:", curtemp - 273.15, "Pressure:", curpres)
    #if your temp is Celsius then celsius = curtemp - 273.15

else:
    print("No city found.")
    

root.title("Weather in the city")

temp = Label(root, text=temperature)
temp.pack()

humi = Label(root, text=humidity)
humi.pack()

pres = Label(root, text=pressure)
pres.pack()

root.mainloop()
