from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Fresnapp")
root.geometry("900x500+300+200")
root.resizable(False, False)


def getWeather():
    city = textfield.get()
    geolocator = Nominatim(user_agent="geoapiExcercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")
    # weather
    lat = str(location.latitude)
    lon = str(location.longitude)
    key = "5407c192dbf2ccac1f5e08055121db44"
    # api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&2a46bbb61325adf24df6391d00ddcb45"
    api = "https://api.openweathermap.org/data/2.5/weather?lat=" + \
        lat+"&lon="+lon+"&appid=5407c192dbf2ccac1f5e08055121db44"

    json_data = requests.get(api).json()
    print(json_data)
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    t.config(text=(temp, "°"))
    c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))

    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)


textfield = tk.Entry(root, justify="left", width=20,
                     font=("poppins", 25),
                     bg="#000",
                     border=2, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

SearchBtn = Button(text="Search", height=2,
                   cursor="exchange", command=getWeather)
SearchBtn.place(x=380, y=39)

# logo
Logo_image = PhotoImage(file="./src/logo_m.png")
logo = Label(image=Logo_image)
logo.place(x=115, y=120)

# Bottom Params
label1 = Label(root, text="WIND", font=(
    "Helvetica", 15, "bold"), fg="white")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=(
    "Helvetica", 15, "bold"), fg="white")
label2.place(x=260, y=400)

label3 = Label(root, text="DESCRIPTION", font=(
    "Helvetica", 15, "bold"), fg="white")
label3.place(x=430, y=400)

label4 = Label(root, text="PRESSURE", font=(
    "Helvetica", 15, "bold"), fg="white")
label4.place(x=650, y=400)

# time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)


t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)

c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w = Label(text="", font=("arial", 20, "bold"))
w.place(x=120, y=430)

h = Label(text="", font=("arial", 20, "bold"))
h.place(x=285, y=430)

d = Label(text="", font=("arial", 20, "bold"))
d.place(x=410, y=430)

p = Label(text="", font=("arial", 20, "bold"))
p.place(x=680, y=430)

root.mainloop()
