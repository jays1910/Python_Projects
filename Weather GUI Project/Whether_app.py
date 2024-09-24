import requests
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Weather App")

# City label and input
city_label = tk.Label(root, text="City:")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

# Weather label to display the result
weather_label = tk.Label(root, text="")
weather_label.pack()

# Fetch weather function
def fetch_weather():
    city = city_entry.get()
    api_key = "88dc35347#######727bd91b5b#####"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            # Convert temperature from Kelvin to Celsius
            temperature = data["main"]["temp"] - 273.15
            weather = data["weather"][0]["description"]

            weather_label.config(text=f"Temperature: {temperature:.2f}°C\nWeather: {weather}")
        else:
            messagebox.showerror("Error", f"City not found or other error: {data['message']}")
    except Exception as e:
        messagebox.showerror("Error", f"Unable to fetch weather data: {e}")

# Button to trigger the weather fetch
fetch_button = tk.Button(root, text="Fetch Weather", command=fetch_weather)
fetch_button.pack()

root.mainloop()
