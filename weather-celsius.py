import requests
import json
from Tkinter import *

root = Tk()

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
    cel = "Temperature", curtemp - 273.15, "C°"
    humi = "Humidity:", curhumi,"%"
    pressure = "Pressure:", curpress, "hPa"
    print("Temperature:", cel, "Pressure:", curpres)
    #if your temp is Celsius then celsius = curtemp - 273.15

else:
    print("No city found.")

frame = LabelFrame(root, text="Weather")
frame.pack(fill="both", expand="yes")
temp = Label(frame, text=cel).pack()
humid = Label(frame, text=humi).pack()
press = Label(frame, text=pressure).pack()

root.mainloop()
