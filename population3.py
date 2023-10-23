import pandas as pd
import numpy as np

total_population = pd.read_csv("./data/gold/total_population_per_district.csv", index_col=0)
current_population = total_population[total_population.index == 2023].values #.sum()
last_year = total_population.index[-1]
expected_population = total_population[total_population.index == last_year].values
#expected_population = np.sum(expected_population)
growth_rate = (expected_population / current_population) - 1
#print(total_population)

average_district_growth_rate = np.mean(growth_rate)
district_highest_growth_rate = total_population.columns[np.argmax(growth_rate)]
district_lowest_growth_rate = total_population.columns[np.argmin(growth_rate)]

print(growth_rate, np.argmax(growth_rate), district_highest_growth_rate, district_lowest_growth_rate, average_district_growth_rate)