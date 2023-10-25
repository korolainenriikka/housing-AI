import pandas as pd
import numpy as np 

def get_population_metrics(population: pd.DataFrame, option: str):
    df = population[["Year", option]]

    current_population = df[df.Year == "2023"][option] #.values
    expected_population =  df.iloc[-1][option] #.values
    growth_rate = (expected_population / current_population) - 1
    growth_rate = round(growth_rate * 100, 3)
    growth_rate = growth_rate.values[0]
    return current_population, expected_population, growth_rate
    
def get_total_population_metrics(total_population: pd.DataFrame):
    #total_population = pd.read_csv("./data/gold/total_population_per_district.csv", index_col=0)
    current_population = np.sum(total_population[total_population.index == 2023].values) #.sum()
    last_year = total_population.index[-1]
    expected_population = total_population[total_population.index == last_year].values
    expected_population = np.sum(expected_population)
    growth_rate = (expected_population / current_population) - 1
    growth_rate = round(growth_rate * 100, 3)
    return current_population, expected_population, growth_rate

def get_aggregated_metrics(total_population:pd.DataFrame):

    current_population = total_population[total_population.index == 2023].values #.sum()
    last_year = total_population.index[-1]
    expected_population = total_population[total_population.index == last_year].values
    growth_rate = (expected_population / current_population) - 1

    average_district_growth_rate = np.mean(growth_rate)
    district_highest_growth_rate = total_population.columns[np.argmax(growth_rate)]
    district_lowest_growth_rate = total_population.columns[np.argmin(growth_rate)]

    average_district_growth_absolute = np.mean(expected_population - current_population)
    district_highest_growth_absolute = total_population.columns[np.argmax(expected_population - current_population)]
    district_lowest_growth_absolute = total_population.columns[np.argmin(expected_population - current_population)]

    return (
        round(average_district_growth_rate * 100, 2), 
        district_highest_growth_rate, 
        round(np.max(growth_rate) * 100, 2), 
        district_lowest_growth_rate,
        round(np.min(growth_rate) * 100, 2), 
        average_district_growth_absolute, 
        district_highest_growth_absolute, 
        np.max(expected_population - current_population),
        district_lowest_growth_absolute,
        np.min(expected_population - current_population)
    )

def get_aggregated_housing_metrics(housing_data: pd.DataFrame):

    # Get districts names.
    districts_names = housing_data["District"].unique()

    # Houses build metrics
    houses_build = housing_data[housing_data.Year <= 2019]
    total_build_houses = int(houses_build["Pred_Num_Houses"].sum()) # This is a number.
    agg_houses_build = houses_build.groupby("District")["Pred_Num_Houses"].sum()
    greatest_num_houses_build = int(agg_houses_build.max()) # This is a number.
    district_greatest_num_houses_build = districts_names[agg_houses_build.argmax()] # This is a string.
    lowest_num_houses_build = int(agg_houses_build.min()) # This is a number.
    district_lowest_num_houses_build = districts_names[agg_houses_build.argmin()] # This is a string.

    # Houses predictions metrics
    houses_prediction = housing_data[housing_data.Year >= 2020]
    total_predicted_houses = int(houses_prediction["Pred_Num_Houses"].sum()) # This is a number.
    agg_houses_prediction = houses_prediction.groupby("District")["Pred_Num_Houses"].sum()
    lowest_num_houses_prediction = int(agg_houses_prediction.min()) # This is a number.
    district_lowest_num_houses_prediction = districts_names[agg_houses_prediction.argmin()] # This is a string.
    greatest_num_houses_prediction = int(agg_houses_prediction.max()) # This is a number.
    district_greatest_num_houses_prediction = districts_names[agg_houses_prediction.argmax()] # This is a string.

    # Return metrics.
    return (
        total_build_houses,
        greatest_num_houses_build,
        district_greatest_num_houses_build,
        lowest_num_houses_build,
        district_lowest_num_houses_build,
        total_predicted_houses,
        lowest_num_houses_prediction,
        district_lowest_num_houses_prediction,
        greatest_num_houses_prediction,
        district_greatest_num_houses_prediction
    )
   