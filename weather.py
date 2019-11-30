import requests
import json
from Tkinter import *
from flask import Flask

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

root.title("Weather in", city)

temp = Label(root, text=temperature)
temp.pack()

humi = Label(root, text=humidity)
humi.pack()

pres = Label(root, text=pressure)
pres.pack()

app = Flask(__name__)

@app.route('/')
def web():
    return render_template("index.html", temp1=cel, humid1=humi, press1=pressure, city1=city);

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
    
root.mainloop()
