from dotenv import dotenv_values
import googlemaps
import joblib 
import pandas as pd
import numpy as np 

config = dotenv_values(".env")


API_KEY = config["API_KEY"]
gmaps = googlemaps.Client(key=API_KEY)

areas = [
    {"name": "Eteläinen", "address": "Finland, Helsinki, Eteläinen"}, 
    {"name": "Itäinen", "address": "Finland, Helsinki, Itäinen"}, 
    {"name": "Kaakkoinen", "address": "Finland, Helsinki, Kaakkoinen"}, 
    {"name": "Keskinen", "address": "Finland, Helsinki, Keskinen"}, 
    {"name": "Koillinen", "address": "Finland, Helsinki, Koillinen"}, 
    {"name": "Läntinen", "address": "Finland, Helsinki, Läntinen"}, 
    {"name": "Östersundomin", "address": "Finland, Helsinki, Östersundomin"}, 
    {"name": "Pohjoinen", "address": "Finland, Helsinki, Pohjoinen"}, 
]

def get_places_coordinates():
    for area in areas:
        name_site = area["address"]
        geocode_result = gmaps.geocode(name_site)
        file_name = f"./data/bronze/coordinates/{area['name']}_geocode_result.pkl"
        joblib.dump(geocode_result, file_name)

def process_places_coordinates():
    lats = list()
    lngs = list()
    districts = list()
    for area in areas:
        file_name = f"./data/bronze/coordinates/{area['name']}_geocode_result.pkl"
        data = joblib.load(file_name)
        data = data[0]
        location = data["geometry"]["location"]
        lat = location["lat"]
        lng = location["lng"]
        districts.append(area['name'])
        lats.append(lat)
        lngs.append(lng)
    pd.DataFrame({"district": districts, "lat": lats, "lng": lngs}).to_csv("./data/silver/housing/areas_coordinates.csv")

process_places_coordinates()
