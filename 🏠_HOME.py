import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie


st.set_page_config(
    page_title="PERSONAL WEBSITE"
)

#---------------------LOTTIE  ANIMATION ------------------------
def load_lottie(url):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

lottie_coding = load_lottie("https://lottie.host/e0a6d7e0-6b3d-428f-addc-aa44a746d653/MImt8ecbMs.json")


st.sidebar.success("Select a page above")



# -------------- HEADER ----------------------------
with st.container():
    st.subheader("Hi , I am Sudhanshu :wave:")
    st.title("A Data Scientist and Computer Vision Engineer from INDIA")
    st.write("I am passionate about finding ways to solve real life problems through my skills of ML , DL and Computer Vision")
    st.write("[Know more about me  >> ](www.linkedin.com/in/sudhanshu-gusain976))")

# --------------------WHAT I DO --------------------------
with st.container():
    st.write("-----")
    left_column ,center, right_column = st.columns(3)
    with left_column:
        st.header("MY SKILLS")
        st.write("##")
        st.write("""  
                📊 **Data Science Explorer**: Over the past year, I've dedicated myself to understanding and harnessing the power of data. I've translated my knowledge into tangible projects, gaining expertise in a wide range of skills, including:

- **SQL and Python**
- **POWER BI DASHBOARDS**
- **Machine Learning**
- **Deep Learning**
- **NLP (Natural Language Processing)**
- **CV (Computer Vision)**
- **Flask / Streamlit**
- **Web Services**

                    """)
        
        with center:
            st.write("")
        with right_column:
            st.header("MY PROJECTS")
            st.write("##")
            st.write("""
                     1. ATM APP 
                     2. POWER BI DASHBOARDS
                     3. NLP PROJECTS
                     4. POTATO DISEASE CLASSIFIER
                     5. MALARIA DIAGNOSIS
                     6. HUMAN EMOTIONS DETECTOR
                     7. CAR COUNTER APP
                     8. FACE ATTENDANCE SYSTEM""")

with st.container():
    st.write("--------------------------------------------------------------------------------------------------")           
with st.container():
    st_lottie(lottie_coding)          
            

        


        

