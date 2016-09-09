import forecastio
from geopy.geocoders import Nominatim
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

#api_key = os.environ['FORECASTIO_API_KEY']
#latitude = 44.2726
#longitude = -121.1739
#address = input("Enter an address: ")

#forecast = forecastio.load_forecast(api_key, lat, lng).currently()

#print("{} and {}°".format(forecast.summary, forecast.temperature))

#geolocator = Nominatim()

def get_weather(address):
    api_key = os.environ['FORECASTIO_API_KEY']
    geolocator = Nominatim()
    #address = input("Location: ")
    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude
    forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
    summary = forecast.summary
    temperature = forecast.temperature
    return "{} and {}° in {}".format(summary, temperature, location.address)

#print(get_weather(api_key))
