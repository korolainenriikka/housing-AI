# note: also shx file required for this to work!
import matplotlib.pyplot as plt
import geopandas as gpd 
import time 

plt.figure(figsize=(8, 6))
ax = plt.subplot(111)

greater_regions = gpd.read_file('./data/raw/suurpiirit_WFS_areas.shp')
greater_regions.plot(ax=ax, color="lightgray")

df = gpd.read_file("./data/raw/valmistuneetasunnotmal2016_2019.shp")
df.columns = ["id", "municipality_name", "municipality_number", 
              "building_type", "number_of_apartments", "funding_type", 
              "year_of_completion", "geometry"]
df = df[df.municipality_name == 'Helsinki']
drop_columns = ["id", "municipality_name", "municipality_number", "funding_type"]
df = df.drop(drop_columns, axis=1)
#print(df.head())
df.plot(ax=ax, column="building_type", legend=True, cmap="Set1")

plt.show()
time.sleep(10)
plt.savefig("fig.png")