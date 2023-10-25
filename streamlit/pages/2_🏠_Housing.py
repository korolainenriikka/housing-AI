import streamlit as st 
from utils import charts, data, metrics
from PIL import Image 

st.set_page_config(page_title="🏠 Housing", page_icon = "./images/house-icon.png")
st.title("🏠 Housing")

st.markdown("🏠 Explore the future of housing in Helsinki! 📈 This tab offers insights into the projected number of houses to be constructed in different regions of Helsinki until 2036. 🏘️ You can pick your preferred region for a detailed breakdown and even delve into aggregated statistics. We'll provide you with information on the number of houses constructed between 2015 and 2019, and then we'll make predictions for the years spanning from 2020 to 2036. 🏡🔮 Let's uncover the housing trends together! 🌟")


# Get housing predictions
housing_predictions = data.get_housing_predictions()

# Get housing metrics.
(
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
) = metrics.get_aggregated_housing_metrics(housing_predictions)


col1, col2 = st.columns(2)
col1.metric(
   label="📈 Helsinki number of houses built from 2015 to 2019",
   value = total_build_houses 
)
col2.metric(
   label="📈 Helsinki number of houses predicted from 2019 to 2036",
   value = total_predicted_houses, 
   delta = f"{round(total_predicted_houses / total_build_houses, 2) * 100}%"
)

# Show helsinki map districts
image = Image.open("./images/helsinki_districts.jpg")
st.image(image, caption = "District map of Helsinki")

col1, col2 = st.columns(2)
col1.metric(
   label="🏘️ District with highest # houses built (2015 to 2019)",
   value = district_greatest_num_houses_build, 
   delta = greatest_num_houses_build 
)
col2.metric(
   label="🏘️ District with lowest # houses built (2015 to 2019)",
   value = district_lowest_num_houses_build,
   delta = lowest_num_houses_build
)

col1, col2 = st.columns(2)
col1.metric(
   label="📈 District with highest # houses predicted (2019 to 2036) ",
   value = district_greatest_num_houses_prediction, 
   delta = greatest_num_houses_prediction 
)
col2.metric(
   label="📈 District with lowest # houses predicted (2019 to 2036)",
   value = district_lowest_num_houses_prediction,
   delta = lowest_num_houses_prediction
)


districts_names = housing_predictions["District"].unique()
option = st.selectbox(
   "Select Helsinki district",
   districts_names,
   index=1,
   placeholder="Select district..."
)
if option:
    chart = charts.get_housing_predictions_chart(housing_predictions, option)
    st.altair_chart(chart, use_container_width=True)

st.markdown("### ➡️ Next Page: [🤔 About](/About)", unsafe_allow_html=False)