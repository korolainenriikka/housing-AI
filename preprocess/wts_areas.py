# note: also shx file required for this to work!
import matplotlib.pyplot as plt
import geopandas as gpd 
import time 
import googlemaps
from datetime import datetime
import pandas as pd
import numpy as np
from dotenv import dotenv_values
import geopy.distance


config = dotenv_values(".env")
API_KEY = config["API_KEY"]
gmaps = googlemaps.Client(key=API_KEY)

#plt.figure(figsize=(8, 6))
#ax = plt.subplot(111)
#greater_regions = gpd.read_file('./data/raw/suurpiirit_WFS_areas.shp')
#greater_regions.plot(ax=ax, color="lightgray")

df = gpd.read_file("./data/bronze/housing_data/valmistuneetasunnotmal2016_2019.shp")
df.columns = ["id", "municipality_name", "municipality_number", 
              "building_type", "number_of_apartments", "funding_type", 
              "year_of_completion", "geometry"]
df = df[df.municipality_name == 'Helsinki']
df = df.to_crs(4326)

df['lat'] = df['geometry'].y
df['lon'] = df['geometry'].x

drop_columns = ["id", "municipality_name", "municipality_number", "funding_type", 
                "geometry", "building_type"]
df = df.drop(drop_columns, axis=1)
#print(df)

districts_coordinates = pd.read_csv("./data/silver/housing/total/areas_coordinates.csv", index_col=0)
districts_coordinates = districts_coordinates.to_dict(orient = "records")
#print(districts_coordinates)

def get_closest_district(lat, lng):
    distances = []
    for district_info in districts_coordinates:
        coords_1 = (district_info["lat"], district_info["lng"])
        coords_2 = (lat, lng)
        distance = geopy.distance.geodesic(coords_1, coords_2)
        distances.append(distance)
    return districts_coordinates[distances.index(min(distances))]["district"]

df["closest_district"] = df.apply(lambda x: get_closest_district(x["lat"], x["lon"]), axis=1)

#print(df)
#import matplotlib.pyplot as plt
#plt.scatter(x=df['lat'], y=df['lon'])

#for district in districts_coordinates:
#    plt.scatter(x=district['lat'], y=district['lng'], c = 'r')


#plt.show()

#print(df["closest_district"].unique())
df = df.groupby(["closest_district", "year_of_completion"])["number_of_apartments"].sum().reset_index(name="count")
df.to_csv("./data/silver/housing/total/areas_count.csv")

# Generate a csv for each district
datasets = list()
test_datasets = list()
for district in districts_coordinates:
    df_district = df[df["closest_district"] == district["district"]]
    df_district = df_district.reset_index(drop = True)
    #df_district = df.drop(["closest_district"], axis = 1)
    df_district = df_district.rename(columns = {"count": district["district"], "year_of_completion": "year"})

    df_district.index = df_district["year"]
    df_district = df_district.rename(columns = {"count": "num_houses", "closest_district": "district"})

    df_district = df_district.drop(["year"], axis = 1)
    df_population = pd.read_csv(f"./streamlit/data/gold/populations/{district['district']}_population.csv", index_col=0)
    df_population = df_population[[district['district']]]
    df_population = df_population.rename(columns = {district['district']: "population"})

    new_df = df_population.merge(df_district, how = "left", left_index = True, right_index = True)
    new_df.columns = ["population", "district", "num_houses"]

    new_df_test = new_df.copy()
    new_df_test["district"] = new_df["district"].fillna(district["district"])
    test_datasets.append(new_df_test)

    new_df = new_df.dropna()
    new_df.to_csv("./data/silver/housing/districts/{}_houses_count.csv".format(district["district"]))

    datasets.append(new_df)

df = pd.concat(datasets)
df = df.reset_index(drop = True)
df.to_csv("./streamlit/data/gold/dataset/dataset.csv")

test_dataset = pd.concat(test_datasets)
test_dataset = test_dataset.reset_index()
test_dataset.columns = ["year","population","district","num_houses"]
test_dataset.to_csv("./streamlit/data/gold/dataset/test_dataset.csv")
#print(df)
#print(len(df[["lat", "lon"]].drop_duplicates()))

#loc0 = df[["lat", "lon"]].drop_duplicates().values[0]
#print(loc0)
#drop_columns = ["id", "municipality_name", "municipality_number", "funding_type"]
#name_site = "Finland, Helsinki, Eteläinen"
#geocode_result = gmaps.geocode(name_site)
#import joblib
#joblib.dump(geocode_result, "geolocation_result.pkl")
#reverse_geocode_result = gmaps.reverse_geocode(loc0)
#import joblib
#joblib.dump(reverse_geocode_result, "reverse_geocode_result.pkl")

#df_plot = df.drop(drop_columns, axis=1)
#df_plot.to_csv("./data.csv")
#print(df.head())
#df_plot.plot(ax=ax, column="building_type", legend=True, cmap="Set1")

#plt.show()
#time.sleep(10)
#plt.savefig("fig.png")