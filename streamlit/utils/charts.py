import pandas as pd 
from typing import List, Tuple, Dict
import altair as alt
import os 

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
