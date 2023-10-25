from typing import Dict
import os 
import pandas as pd

def get_populations_data() -> Dict:
    dataframes = {}
    files = os.listdir("./data/gold/populations")
    for file in files:
        district_name = file.split("_")[0]
        df = pd.DataFrame(
            pd.read_csv(f'./data/gold/populations/{file}').rename(columns={'Unnamed: 0': 'Year'})
        )
        df["Year"] = df["Year"].astype(str)
        dataframes[district_name] = df
    return dataframes

def get_population_data() -> pd.DataFrame:
    df = list()
    data = get_populations_data()
    for key, val in data:
        df.append(val)
    return pd.concat(df)

def get_total_population_data() -> pd.DataFrame:
    df = pd.read_csv("./data/gold/total/total_population_per_district.csv", index_col=0)
    return df

def get_housing_predictions() -> pd.DataFrame:
    df = pd.read_csv("./data/gold/dataset/test_dataset_pred.csv", index_col=0)
    return df