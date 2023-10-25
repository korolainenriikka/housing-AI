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

fig, ax = plt.subplots(figsize=(20, 10))

df.to_csv(f"./data/gold/total_population_per_district.csv")
import sys
sys.exit()

for column in df.columns:
    data = df[column].to_frame()
    data["h"] = data.reset_index().index
    data["h"] = data["h"].shift(periods = 8)
    data["h"] = data["h"].fillna(0)
    standard_error = data[column][data.index <= 2023].std() / np.sqrt(len(data[column][data.index <= 2023]))
    #print(standard_error)
    #data[f"{column}_Low_CI"] = data[column] - 1.959964 * (np.sqrt(data["h"]) * standard_error)
    #data[f"{column}_High_CI"] = data[column] + 1.959964 * (np.sqrt(data["h"]) * standard_error)
    data = data.drop("h", axis = 1)
    data.to_csv(f"./data/gold/total_population_per_district.csv")

    #ax.plot(data.index, data[column], marker='o', label=column)
    #ax.fill_between(data.index, data[f'{column}_lower_ci'], data[f'{column}_upper_ci'], alpha=0.3, label=f'{column} 95% CI')

    #for i, value in enumerate(data[column]):
    #    ax.text(i, value, str(value), ha='center', va='bottom', fontsize=30)
        
    #dataframes.append(data[[column, f'{column}_lower_ci', f'{column}_upper_ci']])

# Add labels and legend
#ax.vlines(x=2023, ymin=0, ymax=140000, colors='red', linestyles='dashed', label='Current year')
#ax.set_xlabel('Year')
#ax.set_ylabel('Value')
#ax.set_xticks(df.index)
#ax.set_title('Time Series Plot with Confidence Intervals')
#ax.legend(title='District')

#plt.savefig("running.png")


#population = pd.concat(dataframes, axis = 1)
#print(population)
#population.to_csv('data/gold/population.csv')

# Plot each district as a time series
#df.plot(marker='o')

# Add labels and legend
#plt.xlabel('Year')
#plt.ylabel('Value')
#plt.title('Time Series Plot by District')
#plt.legend(title='District')
#plt.savefig("timeseries.png")
# Display the plot
#plt.show()
#plt.legend()

# Display the plot
#plt.show()