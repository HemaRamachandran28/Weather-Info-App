# Weather Info App - Python GUI using CustomTkinter

**Weather Info App** is a Python-based GUI application built with `customtkinter` that allows users to view real-time weather information, 5-day forecasts, and visualized weather trends. It integrates `OpenWeatherMap API` for accurate weather data and supports light/dark theme toggling with a modern, responsive UI.

---

## What does the program do?

The application helps users:

- Get **real-time weather updates** for any city
- Auto-detect current city using IP address
- View **temperature, humidity, pressure, wind speed**, and more
- Get **sunrise and sunset** time (converted from UNIX time)
- See a **5-day forecast chart** using Matplotlib
- Toggle between light and dark UI themes
- Switch between **°C and °F**

---

## Main Window UI

- A bold header with the app title
- City input field (autofilled after a delay using IP location)
- Buttons for:
  - Getting weather
  - Refresh
  - Theme toggle
  - Temperature unit toggle
- Weather icon with temperature, description, and details
- 5-Day forecast in text format
- Line chart showing temperature trend using Matplotlib

---

## Preview

![Screenshot 2025-06-21 223023](https://github.com/user-attachments/assets/980a4fb1-a76a-49ea-9749-54ef6c8ca59a)

---

## Usage Guide

1. **Enter a city** or wait for it to autofill (via your IP location)
2. Click **"Get Weather"**
3. View real-time:
   - Temperature
   - Weather condition
   - Wind speed
   - Humidity
   - Pressure
   - Sunrise/Sunset
4. View 5-day forecast + temperature trend chart
5. Use:
   - "Switch to °C/°F"
   - "Toggle Theme"
   - "Refresh"

---

## Functional Modules

### Weather Fetcher
- Validates input
- Calls OpenWeatherMap API for:
  - `/weather` (current data)
  - `/forecast` (5-day forecast)

### Forecast Display
- Shows 5-day summary with temperature and condition
- Extracts every 8th forecast (1 per day)
- Uses Matplotlib to plot a temperature line chart

### Image Handling
- Dynamically fetches and displays weather icons
- Uses `CTkImage` for DPI-safe scaling

---

## Technical Stack

- `Python 3.10+`
- `customtkinter` for UI
- `requests` for API calls
- `Pillow` for weather icon handling
- `matplotlib` for plotting temperature charts
- `OpenWeatherMap API` for live weather data

---

## Weather API

We use OpenWeatherMap’s `weather` and `forecast` endpoints.

**Example API Call:**

bash
http://api.openweathermap.org/data/2.5/weather?q=Chennai&appid=YOUR_API_KEY&units=metric

---

## Features

- Real-time weather updates
- Light/Dark theme support
- °C / °F toggle
- Wind speed and pressure display
- Sunrise/Sunset conversion
- 5-day forecast text + chart
- Image icon for weather condition
- Clean and responsive UI

---

## Possible Enhancements

- Add hourly forecast section
- Add humidity & UV index meters with color coding
- Add animated weather backgrounds (GIFs/video)
- Text-to-speech summary of weather
- Export forecast to PDF or CSV
- Add loading spinner during API calls
- Convert into .exe using PyInstaller

--- 

## Features video

https://github.com/user-attachments/assets/1e8d2f13-ca4a-44fc-9bcb-ae430fbffe91

---

## License

This project is licensed under the MIT License.

---

## Show Your Support

If you like this project, please Star it on GitHub! Contributions and feedback are welcome.
