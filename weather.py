# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 21:47:04 2021

@author: shadow
"""
import tkinter as tk
import requests
import time
 

def getWeather(root):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=6b0487a4bfbbe3be9a3aec72b3aee860"
    
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 19800))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 19800))

    final_info = condition + "\n" + str(temp) + "°C" 
    final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)

f = ("garamond", 15, "bold")
t = ("garamond", 35)
h=("optima", 35,"italic")

root = tk.Tk()
root.title("Weather App")
root.geometry('600x600')
root.configure(bg="#5ce6a3")
frame=tk.Frame(root,bg="#ADD8E6")
frame.place(relx=0.05,rely=0.05,relheight=0.9,relwidth=0.9)
label3 = tk.Label(frame, font=h,bg="#ADD8E6",text="CITY Name:")
label3.pack()
textField = tk.Entry(frame, justify='center', font = t)
textField.pack(pady=10)
textField.focus()
textField.bind('<Return>', getWeather)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: getWeather(root))
button.pack()

label1 = tk.Label(frame, font=t,bg="#ADD8E6")
label1.pack()

label2 = tk.Label(frame, font=f,bg="#ADD8E6")
label2.pack()

root.mainloop()
