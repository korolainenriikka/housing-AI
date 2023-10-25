import pandas as pd 
from typing import List, Tuple, Dict
import altair as alt
import os 
import numpy as np


def get_housing_predictions_chart(df: pd.DataFrame, district_name: str) -> alt.Chart:
    # Create an Altair plot
    df_district = df[df["District"] == district_name]
    df_district = df_district.reset_index(drop=True)
    df_district = df_district[["Year", "Pred_Num_Houses"]]
    df_district["Pred_Num_Houses"] = df_district["Pred_Num_Houses"].astype(int)
   
    # Generate confident intervals.
    df_district["h"] = df_district.reset_index().index
    df_district["h"] = df_district["h"].shift(periods = 4)
    df_district["h"] = df_district["h"].fillna(0)
    column = "Pred_Num_Houses"
    standard_error = (df_district[column][df_district.Year <= 2019].std() / 
                      np.sqrt(len(df_district[column][df_district.Year <= 2023])))
    df_district[f"{column}_Low_CI"] = df_district[column] - 1.959964 * (np.sqrt(df_district["h"]) * standard_error)
    df_district[f"{column}_High_CI"] = df_district[column] + 1.959964 * (np.sqrt(df_district["h"]) * standard_error)
    df_district["Year"] = df_district["Year"].astype(str)

    chart = alt.Chart(df_district).mark_circle().encode(
        x='Year',
        y=alt.Y("Pred_Num_Houses", title = "Num. Houses"),
    )
    chart += alt.Chart(df_district).mark_line(opacity=0.3).encode(
        x='Year',
        y = alt.Y('Pred_Num_Houses_Low_CI', title = None),        #y2 = alt.Y2(f'{district_name}_High_CI', axis=alt.Axis(labels=False)),
    )
    chart += alt.Chart(df_district).mark_line(opacity=0.3).encode(
        x='Year',
        y = alt.Y(f'Pred_Num_Houses_High_CI', title = None),        #y2 = alt.Y2(f'{district_name}_High_CI', axis=alt.Axis(labels=False)),
        #y2 = alt.Y2(f'{district_name}_High_CI', axis=alt.Axis(labels=False)),
    )

    # Customize the chart appearance
    chart = chart.properties(
        title=f'{district_name} No. New Houses Per Year',
        width=500,
        height=300, 
        
    ).encode(
        y=alt.Y(f'Pred_Num_Houses', title='No. New Houses')
    )


    return chart

def get_population_chart(df: pd.DataFrame, district_name: str) -> alt.Chart:

    # Create an Altair plot
    chart = alt.Chart(df).mark_line().encode(
        x='Year',
        y=alt.Y(f'{district_name}', title = "Population"),
    )

    # Add confidence intervals as a shaded area
    chart += alt.Chart(df).mark_line(opacity=0.3).encode(
        x='Year',
        y = alt.Y(f'{district_name}_Low_CI', title = None),        #y2 = alt.Y2(f'{district_name}_High_CI', axis=alt.Axis(labels=False)),
    )

    # Add confidence intervals as a shaded area
    chart += alt.Chart(df).mark_line(opacity=0.3).encode(
        x='Year',
        y = alt.Y(f'{district_name}_High_CI', title = None),        #y2 = alt.Y2(f'{district_name}_High_CI', axis=alt.Axis(labels=False)),
        #y2 = alt.Y2(f'{district_name}_High_CI', axis=alt.Axis(labels=False)),
    )


    # Customize the chart appearance
    chart = chart.properties(
        title=f'{district_name} Population Over Time',
        width=500,
        height=300, 
        
    ).encode(
        y=alt.Y(f'{district_name}', title='Population')
    )

 
    rules = alt.Chart(pd.DataFrame({
            'Year': ['2023'],
            'color': ['red']
        })).mark_rule().encode(
            x='Year',
            color=alt.Color('color:N', scale=None)
        )
    chart += rules

    return chart
