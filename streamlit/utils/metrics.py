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

    # Apartments build metrics
    apartments_build = housing_data[housing_data.Year <= 2019]
    total_build_Apartments = int(apartments_build["Pred_Num_Apartments"].sum()) # This is a number.
    agg_apartments_build = apartments_build.groupby("District")["Pred_Num_Apartments"].sum()
    greatest_num_Apartments_build = int(agg_apartments_build.max()) # This is a number.
    district_greatest_num_Apartments_build = districts_names[agg_apartments_build.argmax()] # This is a string.
    lowest_num_Apartments_build = int(agg_apartments_build.min()) # This is a number.
    district_lowest_num_Apartments_build = districts_names[agg_apartments_build.argmin()] # This is a string.

    # Apartments predictions metrics
    apartments_prediction = housing_data[housing_data.Year >= 2020]
    total_predicted_Apartments = int(apartments_prediction["Pred_Num_Apartments"].sum()) # This is a number.
    agg_apartments_prediction = apartments_prediction.groupby("District")["Pred_Num_Apartments"].sum()
    lowest_num_Apartments_prediction = int(agg_apartments_prediction.min()) # This is a number.
    district_lowest_num_Apartments_prediction = districts_names[agg_apartments_prediction.argmin()] # This is a string.
    greatest_num_Apartments_prediction = int(agg_apartments_prediction.max()) # This is a number.
    district_greatest_num_Apartments_prediction = districts_names[agg_apartments_prediction.argmax()] # This is a string.

    # Return metrics.
    return (
        total_build_Apartments,
        greatest_num_Apartments_build,
        district_greatest_num_Apartments_build,
        lowest_num_Apartments_build,
        district_lowest_num_Apartments_build,
        total_predicted_Apartments,
        lowest_num_Apartments_prediction,
        district_lowest_num_Apartments_prediction,
        greatest_num_Apartments_prediction,
        district_greatest_num_Apartments_prediction
    )
   