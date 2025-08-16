import requests
import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import threading
import time
from datetime import datetime
import os
import json

# Set appearance mode and color theme
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class WeatherApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("WeatherPro - Professional Weather App")
        self.root.geometry("1000x700")
        self.root.minsize(800, 600)
        
        # Initialize variables
        self.current_weather = {}
        self.forecast_data = {}
        self.weather_icons = {}
        self.recent_searches = self.load_recent_searches()
        
        # Create main interface
        self.create_widgets()
        self.load_weather_icons()
        
        # Center window
        self.center_window()
        
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_widgets(self):
        # Main container
        self.main_frame = ctk.CTkFrame(self.root, corner_radius=0)
        self.main_frame.pack(fill="both", expand=True)
        
        # Header
        self.create_header()
        
        # Content area
        self.content_frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Left sidebar
        self.create_sidebar()
        
        # Main weather display
        self.create_weather_display()
        
        # Footer
        self.create_footer()
        
        # Status label
        self.status_label = ctk.CTkLabel(self.main_frame, text="", font=ctk.CTkFont(size=12))
        self.status_label.pack(pady=10)
    
    def create_header(self):
        header_frame = ctk.CTkFrame(self.main_frame, height=80, corner_radius=0)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)
        
        # Title
        title_label = ctk.CTkLabel(
            header_frame, 
            text="WeatherPro", 
            font=ctk.CTkFont(size=28, weight="bold")
        )
        title_label.pack(side="left", padx=30, pady=20)
        
        # Search bar
        search_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        search_frame.pack(side="right", padx=30, pady=20)
        
        self.city_entry = ctk.CTkEntry(
            search_frame,
            placeholder_text="Enter city name...",
            width=250,
            height=40,
            font=ctk.CTkFont(size=14)
        )
        self.city_entry.pack(side="left", padx=5)
        
        search_btn = ctk.CTkButton(
            search_frame,
            text="Search",
            width=100,
            height=40,
            command=self.search_weather,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        search_btn.pack(side="left", padx=5)
    
    def create_sidebar(self):
        sidebar = ctk.CTkFrame(self.content_frame, width=200, corner_radius=10)
        sidebar.pack(side="left", fill="y", padx=(0, 10))
        sidebar.pack_propagate(False)
        
        # Recent searches
        recent_label = ctk.CTkLabel(
            sidebar,
            text="Recent Searches",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        recent_label.pack(pady=10)
        
        # Create scrollable frame for recent searches
        self.recent_searches_frame = ctk.CTkScrollableFrame(
            sidebar,
            fg_color="transparent",
            height=200
        )
        self.recent_searches_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.update_recent_searches_display()
    
    def create_weather_display(self):
        weather_frame = ctk.CTkFrame(self.content_frame, corner_radius=10)
        weather_frame.pack(side="right", fill="both", expand=True)
        
        # Current weather section
        current_frame = ctk.CTkFrame(weather_frame, corner_radius=10)
        current_frame.pack(fill="x", padx=20, pady=20)
        
        # Location and time
        self.location_label = ctk.CTkLabel(
            current_frame,
            text="Enter a city to get weather",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.location_label.pack(pady=10)
        
        self.time_label = ctk.CTkLabel(
            current_frame,
            text=datetime.now().strftime("%A, %B %d, %Y %I:%M %p"),
            font=ctk.CTkFont(size=14)
        )
        self.time_label.pack()
        
        # Weather info container
        info_frame = ctk.CTkFrame(current_frame, fg_color="transparent")
        info_frame.pack(fill="x", pady=20)
        
        # Left side - temperature and condition
        temp_frame = ctk.CTkFrame(info_frame, fg_color="transparent")
        temp_frame.pack(side="left", padx=20)
        
        self.temp_label = ctk.CTkLabel(
            temp_frame,
            text="--°C",
            font=ctk.CTkFont(size=48, weight="bold")
        )
        self.temp_label.pack()
        
        self.condition_label = ctk.CTkLabel(
            temp_frame,
            text="--",
            font=ctk.CTkFont(size=18)
        )
        self.condition_label.pack()
        
        # Right side - details
        details_frame = ctk.CTkFrame(info_frame, fg_color="transparent")
        details_frame.pack(side="right", padx=20)
        
        self.details_labels = {}
        details = ["Humidity", "Wind Speed", "Pressure", "Visibility"]
        
        for detail in details:
            frame = ctk.CTkFrame(details_frame, fg_color="transparent")
            frame.pack(fill="x", pady=5)
            
            label = ctk.CTkLabel(
                frame,
                text=f"{detail}: --",
                font=ctk.CTkFont(size=14)
            )
            label.pack(side="left")
            self.details_labels[detail] = label
    
    def create_footer(self):
        footer = ctk.CTkFrame(self.main_frame, height=40, corner_radius=0)
        footer.pack(fill="x", side="bottom")
        footer.pack_propagate(False)
        
        footer_label = ctk.CTkLabel(
            footer,
            text="WeatherPro v1.0 | © 2024 Shivam Kumar | All rights reserved",
            font=ctk.CTkFont(size=12)
        )
        footer_label.pack(pady=10)
    
    def load_weather_icons(self):
        # Placeholder for weather icons
        pass
    
    def load_recent_searches(self):
        """Load recent searches from file."""
        try:
            if os.path.exists('recent_searches.json'):
                with open('recent_searches.json', 'r') as f:
                    return json.load(f)
            return []
        except Exception:
            return []
    
    def save_recent_searches(self):
        """Save recent searches to file."""
        try:
            with open('recent_searches.json', 'w') as f:
                json.dump(self.recent_searches, f)
        except Exception as e:
            print(f"Error saving recent searches: {e}")
    
    def add_recent_search(self, city):
        """Add a city to recent searches."""
        city = city.strip()
        if city and city not in self.recent_searches:
            self.recent_searches.insert(0, city)
            self.recent_searches = self.recent_searches[:10]  # Keep only last 10 searches
            self.save_recent_searches()
            self.update_recent_searches_display()
    
    def search_weather(self, city=None):
        if city is None:
            city = self.city_entry.get().strip()
        
        if not city:
            messagebox.showwarning("Warning", "Please enter a city name!")
            return
        
        # Run in thread to prevent GUI freezing
        threading.Thread(target=self.fetch_weather_data, args=(city,), daemon=True).start()
    
    def fetch_weather_data(self, city):
        try:
            # Get coordinates
            lat, lon = self.get_coordinates(city)
            if lat and lon:
                weather_data = self.get_weather(lat, lon)
                self.root.after(0, lambda: self.update_weather_display(city, weather_data))
            else:
                self.root.after(0, lambda: messagebox.showerror("Error", "City not found!"))
                
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", f"Failed to fetch weather data: {str(e)}"))
    
    def get_coordinates(self, city):
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"
        params = {"name": city, "count": 1}
        response = requests.get(geo_url, params=params)
        if response.status_code == 200:
            data = response.json()
            if "results" in data and data["results"]:
                return data["results"][0]["latitude"], data["results"][0]["longitude"]
        return None, None
    
    def get_weather(self, lat, lon):
        weather_url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": True,
            "hourly": ["relativehumidity_2m", "surface_pressure", "visibility"],
            "daily": ["temperature_2m_max", "temperature_2m_min", "weathercode"],
            "timezone": "auto"
        }
        response = requests.get(weather_url, params=params)
        if response.status_code == 200:
            return response.json()
        return None
    
    def update_recent_searches_display(self):
        """Update the display of recent searches."""
        # Clear existing buttons
        for widget in self.recent_searches_frame.winfo_children():
            widget.destroy()
        
        # Add recent searches as clickable buttons
        for city in self.recent_searches:
            city_btn = ctk.CTkButton(
                self.recent_searches_frame,
                text=city,
                command=lambda c=city: self.search_weather(c),
                height=35,
                font=ctk.CTkFont(size=12),
                fg_color="transparent",
                text_color=("black", "white"),
                hover_color=("gray80", "gray20")
            )
            city_btn.pack(fill="x", pady=2, padx=5)

    def update_weather_display(self, city, weather_data):
        if not weather_data:
            return
        
        current = weather_data.get('current_weather', {})
        hourly = weather_data.get('hourly', {})
        
        # Update location and time
        self.location_label.configure(text=city)
        self.time_label.configure(text=datetime.now().strftime("%A, %B %d, %Y %I:%M %p"))
        
        # Update temperature and condition
        temp = current.get('temperature', '--')
        self.temp_label.configure(text=f"{temp}°C")
        
        # Update condition
        weather_code = current.get('weathercode', 0)
        condition = self.interpret_weather_code(weather_code)
        self.condition_label.configure(text=condition)
        
        # Update details
        wind_speed = current.get('windspeed', '--')
        self.details_labels["Wind Speed"].configure(text=f"Wind Speed: {wind_speed} km/h")
        
        # Update humidity from hourly data
        humidity_data = hourly.get('relativehumidity_2m', [])
        humidity = '--'
        if humidity_data:
            humidity = int(humidity_data[0])  # Get current hour's humidity
        self.details_labels["Humidity"].configure(text=f"Humidity: {humidity}%")
        
        # Update pressure from hourly data
        pressure_data = hourly.get('surface_pressure', [])
        pressure = '--'
        if pressure_data:
            pressure = int(pressure_data[0])  # Get current hour's pressure
        self.details_labels["Pressure"].configure(text=f"Pressure: {pressure} hPa")
        
        # Update visibility from hourly data
        visibility_data = hourly.get('visibility', [])
        visibility = '--'
        if visibility_data:
            visibility = int(visibility_data[0] / 1000)  # Convert meters to km
        self.details_labels["Visibility"].configure(text=f"Visibility: {visibility} km")
        
        # Add to recent searches
        self.add_recent_search(city)
    
    def interpret_weather_code(self, code):
        weather_conditions = {
            0: "Clear sky ☀️",
            1: "Mainly clear 🌤️",
            2: "Partly cloudy ⛅",
            3: "Overcast ☁️",
            45: "Foggy 🌫️",
            48: "Depositing rime fog 🌫️",
            51: "Light drizzle 🌦️",
            53: "Moderate drizzle 🌦️",
            55: "Dense drizzle 🌧️",
            56: "Light freezing drizzle 🧊🌧️",
            57: "Dense freezing drizzle 🧊🌧️",
            61: "Slight rain 🌦️",
            63: "Moderate rain 🌧️",
            65: "Heavy rain 🌧️",
            66: "Light freezing rain 🧊🌧️",
            67: "Heavy freezing rain 🧊🌧️",
            71: "Slight snow fall 🌨️",
            73: "Moderate snow fall 🌨️",
            75: "Heavy snow fall 🌨️",
            77: "Snow grains 🌨️",
            80: "Slight rain showers 🌦️",
            81: "Moderate rain showers 🌦️",
            82: "Violent rain showers ⛈️",
            85: "Slight snow showers 🌨️",
            86: "Heavy snow showers 🌨️",
            95: "Thunderstorm ⛈️",
            96: "Thunderstorm with slight hail ⛈️",
            99: "Thunderstorm with heavy hail ⛈️"
        }
        return weather_conditions.get(code, "Unknown weather")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = WeatherApp()
    app.run()
