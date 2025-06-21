import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image
import requests
from io import BytesIO
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Setup
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Advanced Weather App")
app.geometry("520x800")
app.resizable(False, False)

unit = "metric"  # or "imperial"

# Get user's city via IP
def get_user_city():
    try:
        ip_info = requests.get("https://ipinfo.io").json()
        return ip_info.get("city", "")
    except:
        return ""

# Insert default city after short delay (if user hasn't typed)
def insert_default_city():
    if not city_entry.get().strip():
        default_city = get_user_city()
        if default_city:
            city_entry.insert(0, default_city)

app.after(3000, insert_default_city)

# Convert UNIX to readable time
def convert_unix_time(unix_time):
    return datetime.fromtimestamp(unix_time).strftime('%H:%M')

# Toggle between light/dark mode
def toggle_theme():
    current = ctk.get_appearance_mode()
    ctk.set_appearance_mode("Dark" if current == "Light" else "Light")

# Toggle temperature unit
def toggle_unit():
    global unit
    unit = "imperial" if unit == "metric" else "metric"
    unit_btn.configure(text="Switch to °C" if unit == "imperial" else "Switch to °F")
    get_weather()

# Main weather function
def get_weather():
    city = city_entry.get().strip()
    if city == get_user_city():  # prevent default city being treated as user input
        result_label.configure(text="❗ Please enter a city name.")
        return


    try:
        api_key = "fa99d988698088dcf8fdde8f9f23da8c"  # Replace with your OpenWeatherMap API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={unit}"
        res = requests.get(url)
        data = res.json()

        if data.get("cod") != 200:
            result_label.configure(text=f"⚠️ {data.get('message')}")
            return

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"].title()
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        pressure = data["main"]["pressure"]
        sunrise = convert_unix_time(data["sys"]["sunrise"])
        sunset = convert_unix_time(data["sys"]["sunset"])
        icon_code = data["weather"][0]["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

        unit_symbol = "°F" if unit == "imperial" else "°C"
        wind_unit = "mph" if unit == "imperial" else "km/h"

        result_label.configure(
            text=f"🌡 Temp: {temp}{unit_symbol}\n"
                 f"🌥 {desc}\n"
                 f"💧 Humidity: {humidity}%\n"
                 f"💨 Wind: {wind} {wind_unit}\n"
                 f"📊 Pressure: {pressure} hPa\n"
                 f"🌅 Sunrise: {sunrise} | 🌇 Sunset: {sunset}"
        )

        # Weather Icon (CTkImage)
        icon_img = Image.open(BytesIO(requests.get(icon_url).content)).resize((100, 100))
        ctk_icon = CTkImage(light_image=icon_img, dark_image=icon_img, size=(100, 100))
        if app.winfo_exists():
            icon_label.configure(image=ctk_icon, text="")
            icon_label.image = ctk_icon

        # Forecast
        forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={unit}"
        forecast_data = requests.get(forecast_url).json()

        forecast_text = "📆 5-Day Forecast:\n"
        dates, temps = [], []

        for i in range(0, 40, 8):
            block = forecast_data["list"][i]
            date = block["dt_txt"].split()[0]
            day_temp = block["main"]["temp"]
            day_desc = block["weather"][0]["description"].title()
            forecast_text += f"{date}: {day_temp}{unit_symbol}, {day_desc}\n"
            dates.append(date)
            temps.append(day_temp)

        forecast_label.configure(text=forecast_text)
        draw_chart(dates, temps)

    except Exception as e:
        if app.winfo_exists():
            result_label.configure(text="⚠️ Error fetching weather data.")

# Draw matplotlib chart
def draw_chart(dates, temps):
    for widget in chart_frame.winfo_children():
        widget.destroy()

    fig, ax = plt.subplots(figsize=(6.5, 4), dpi=100)
    ax.plot(dates, temps, marker='o', color='skyblue')
    ax.set_title('5-Day Temperature Forecast')
    ax.set_ylabel("Temperature")
    ax.set_xlabel("Date")
    ax.grid(True)

    chart = FigureCanvasTkAgg(fig, master=chart_frame)
    chart.draw()
    chart.get_tk_widget().pack()

# ====================== UI ==========================

ctk.CTkLabel(app, text="🌦️ Weather App", font=("Arial", 24)).pack(pady=15)

city_entry = ctk.CTkEntry(app, width=250, placeholder_text="Enter city")
city_entry.pack(pady=5)

ctk.CTkButton(app, text="Get Weather", command=get_weather).pack(pady=5)
ctk.CTkButton(app, text="🔁 Refresh", command=get_weather).pack(pady=5)
ctk.CTkButton(app, text="🌓 Toggle Theme", command=toggle_theme).pack(pady=5)

unit_btn = ctk.CTkButton(app, text="Switch to °F", command=toggle_unit)
unit_btn.pack(pady=5)

icon_label = ctk.CTkLabel(app, text="")
icon_label.pack(pady=10)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 14), justify="left")
result_label.pack(pady=10)

forecast_label = ctk.CTkLabel(app, text="", font=("Arial", 12), justify="left")
forecast_label.pack(pady=10)

chart_frame = ctk.CTkFrame(app)
chart_frame.pack(pady=10, fill="both", expand=False)

app.mainloop()
