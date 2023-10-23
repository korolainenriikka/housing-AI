import pandas as pd
import os
from typing import Dict 

def get_populations_data() -> Dict:
    dataframes = {}
    files = os.listdir("./data/gold")
    for file in files:
        district_name = file.split("_")[0]
        df = pd.DataFrame(
            pd.read_csv(f'./data/gold/{file}').rename(columns={'Unnamed: 0': 'Year'})
        )
        df["Year"] = df["Year"].astype(str)
        dataframes[district_name] = df
    return dataframes

def get_population_data() -> pd.DataFrame:
    df = list()
    data = get_populations_data()
    for key, val in data.items():
        df.append(val[val.columns[0, 1]])
    return pd.concat(df)

result = get_population_data()
print(result)