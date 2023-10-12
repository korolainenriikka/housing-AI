import geopandas as gpd
import matplotlib.pyplot as plt


df = gpd.read_file("./data/valmistuneetasunnotmal2016_2019.shp")
df.columns = ["id", "municipality_name", "municipality_number", 
              "building_type", "number_of_apartments", "funding_type", 
              "year_of_completion", "geometry"]
df = df[df.municipality_name == 'Helsinki']
drop_columns = ["id", "municipality_name", "municipality_number", "funding_type"]
df = df.drop(drop_columns, axis=1)
print(df.head())
df.plot()
plt.savefig("test.png")

print(df.building_type.unique())
print(df.number_of_apartments.unique())
print(df.year_of_completion.unique())


