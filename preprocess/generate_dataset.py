import pandas as pd
df = pd.read_csv("./data/silver/housing/total/areas_count.csv", index_col=0)
df = df.rename(columns =
    {
        "closest_district": "district", 
        "year_of_completion": "year", 
        "count": "num_houses"
    }
)
#df = 
print(df)