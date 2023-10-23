import streamlit as st 
import pandas as pd
import numpy as np
import altair as alt
import time 
import os
from PIL import Image
from utils import charts, data, metrics

# Configuration 
st.set_page_config(page_title="Population 🧑‍🤝‍🧑", page_icon = "")

# Title of the app
st.header("🏡🤖 Housing AI ")

#st.markdown("🏡🤖 Housing AI embarks on an innovative mission: to forecast the future demand for residential properties in the Helsinki Region, aiming to support the region's flourishing population growth. Utilizing cutting-edge predictive models, we're dedicated to this cause.")

st.markdown("🏡📈 Welcome to Housing AI! The project's goal is to forecast future housing demand in the Helsinki Region. By estimating the number of potential urban residents and pinpointing their preferred locations, we enable data-driven urban planning and efficient housing development. 📊 In this section, we present the current (2023) and projected (2026) population figures for each of Helsinki's districts, helping to shape the city's future.")

st.subheader("Helsinki Population 🧑‍🤝‍🧑")

# Show metrics.
col1, col2 = st.columns(2)
total_population = data.get_total_population_data()

(helsinki_current_population,
helsinki_expected_population,
helsinki_growth_rate) = metrics.get_total_population_metrics(total_population)
col1.metric(
   label="📊 Helsinki Current Population (2023)", 
   value=helsinki_current_population
)
col2.metric(
   label="📈 Helsinki Expected Population (2036)", 
   value=helsinki_expected_population,
   delta=f"{helsinki_growth_rate}%"
)

# Show helsinki map districts
image = Image.open("images/helsinki_districts.jpg")
st.image(image, caption = "District map of Helsinki")


# Get aggregated metrics
(average_district_growth_rate, 
district_highest_growth_rate, 
max_growth_rate,
district_lowest_growth_rate,
min_growth_rate,
average_district_growth_absolute,
district_highest_growth_absolute,
max_growth_absolute,
district_lowest_growth_absolute,
min_growth_absolute) = metrics.get_aggregated_metrics(total_population)


col1, col2, col3 = st.columns(3)
col1.metric(
   label="📈 District Highest Growth Rate",
   value = district_highest_growth_rate, 
   delta=f'{max_growth_rate}%'
)
col2.metric(
   label="📈 District Lowest Growth Rate",
   value = district_lowest_growth_rate, 
   delta=f'{min_growth_rate}%'
)
col3.metric(
   label="📊 District Average Growth Rate", 
   value=f'{average_district_growth_rate}%'
)


col1, col2, col3 = st.columns(3)
col1.metric(
   label = "📈 District Highest Absolute Growth",
   value = district_highest_growth_absolute, 
   delta=f'{max_growth_absolute}'
)
col2.metric(
   label = "📈 District Lowest Absolute Growth",
   value = district_lowest_growth_absolute, 
   delta=f'{min_growth_absolute}'
)
col3.metric(
   label = "📈 District Average Absolute Growth", 
   value=f'{average_district_growth_absolute}'
)

# Show populaiton graphs
dataframes = data.get_populations_data()
districts_names = list(dataframes.keys())
option = st.selectbox(
   "Select Helsinki district",
   districts_names,
   index=1,
   placeholder="Select district..."
)
if option:
   
   dataframes[option].to_csv(f"option_{option}.csv")
   current_population, expected_population, growth_rate = metrics.get_population_metrics(dataframes[option], option)
   
   col1, col2 = st.columns(2)
   col1.metric(label=f"📊 {option} Current Population (2023)", value=current_population)
   col2.metric(label=f"📈 {option} Expected Population (2026)", value=expected_population, delta = f"{growth_rate}%")

   chart = charts.get_population_chart(dataframes[option], option)
   st.altair_chart(chart, use_container_width=True)
   
st.markdown("### ➡️ Next Page: [🏠 Housing](/Housing)", unsafe_allow_html=False)