import streamlit as st 


st.set_page_config(page_title="🤔 About ", page_icon = "./images/house-icon.png")

st.title("🤔 About Housing AI")

st.header("🤓 Goal")

st.markdown("The project aims to predict future housing demand in the city by estimating the number of prospective city dwellers and identifying their preferred areas. This data-driven approach supports informed urban planning and efficient housing development.")

st.header("🧑‍🔬 Methodology")

st.markdown("The methodology involves gathering and analyzing historical data on migration, population, and housing trends. Predictive models, utilizing machine learning and statistical tools, will be created to forecast future housing demand based on demographic, economic, and social factors.")

st.header("💥 Impact")

st.markdown("City planners benefit from accurate long-term predictions, enabling resource allocation and informed decision-making. Building companies reduce business risk and allocate resources optimally. Environmentally, it minimizes ecological impact by directing development to areas with existing infrastructure.")

st.header("🏢 How can this benefit my company?")

st.markdown("If your organization is involved in city planning, real estate, or housing development, this initiative offers benefits like strategic project planning, risk reduction, and competitive advantage. It aligns with sustainable development goals, enhancing your reputation and ecological responsibility.")


st.header("🧑‍🤝‍🧑 Collaborators")
col1, col2, col3 = st.columns(3)

col1.markdown("🐢 [Riikka Korolainen](https://www.linkedin.com/in/riikka-korolainen-127555197/)")
col2.markdown("🐶 [Gayanath Chandrasena](https://www.linkedin.com/in/gayanathchandrasena/)")
col3.markdown("🐯 [Juan Esteban Cepeda](https://www.linkedin.com/in/juan-e-cepeda-gestion/)")
#st.markdown("### ➡️ Next Page: [🚀 Datapalooza](/Datapalooza)", unsafe_allow_html=False)