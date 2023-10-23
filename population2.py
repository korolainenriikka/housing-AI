import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair
dataframes = list()
previous_population = pd.read_csv('data/silver/past_population_clean.csv')
#previous_population.colums = ["Alue","2015","2016","2017","2018","2019","2020","2021","2022"]
future_population = pd.read_csv('data/silver/future_population_clean.csv')
future_population.columns = ["Alue","2023","2024","2025","2026","2027","2028","2029","2030","2031","2032","2033","2034","2035","2036"]


df = pd.concat([previous_population, future_population], axis = 1, join="inner")
df = df.drop("Alue", axis = 1)
df = df.rename(columns = {"Alue/District": "District"})
df = df.set_index('District')
df = df.T
df.index = df.index.astype(int)
df.columns = [column.split(" ")[2] for column in df.columns]
#df = df.reset_index()
#df = df.set_index('index').T
#df = df.reset_index()
#df = df.rename(columns = {"index": "District"})
#df = df.rename(columns = {"index": "Year"})
#df = df.melt(var_name = "Year", value_name = "Population")
df.to_csv("merge.csv")
print(df.describe())

