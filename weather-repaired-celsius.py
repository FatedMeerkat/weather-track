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

canv = Canvas(master, width=480, height=320)
canv.pack()
canv.create_text(anchor=NW, text=cel)
canv.create_text(anchor=NW, text=humi)
canv.create_text(anchor=NW, text=pressure)
root.mainloop()
