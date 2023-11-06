import streamlit as st
st.set_page_config(
    page_title="PERSONAL WEBSITE"
)
if st.button("Go to Project"):
    redirect_link = "https://github.com/sudhanshu976/POWER-BI-PROJECTS"  # Replace with the URL you want to redirect to
    st.markdown(f"[Click here to go to this project code]({redirect_link})")

st.title("POWER BI DASHBOARDS")
st.write("""

#### There are 4 Power-BI Dashboards projects . This include :
- **1. COVID-19 DASHBOARD**         
- **2. TITANIC DASHBOARD**
         
- **3. SALES DASHBOARD** 
         
- **4. CRYPTO CURRENCY DASHBOARD** 
""")

st.write("-------------------------------------------------------------------------------------------------------------------------------------")

img1 , img2 = st.columns(2)
with img1:
    st.image("images/covid_1.jpeg" , caption="COVID_1")
with img2:
    st.image("images/covid_2.jpeg",caption="COVID_2")

img3 , img4 = st.columns(2)
with img3:
    st.image("images/covid_3.jpeg",caption="COVID_3")
with img4:
    st.image("images/sales.jpeg",caption="SALES")
img5 , img6 = st.columns(2)
with img5:
    st.image("images/crypto_1.jpeg",caption="CRYPTO_1")
with img6:
    st.image("images/crypto_2.jpeg",caption="CRYPTO_2")
