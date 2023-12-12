import streamlit as st
st.set_page_config(
    page_title="PERSONAL WEBSITE"
)
import streamlit as st

# Main content
st.title("My Projects")

# List of projects
projects = [
    {"name": "ATM APP", "description": "Python and SQL Project", "link": "https://personalsudhanshu.streamlit.app/ATM-APP"},
    {"name": "BLOG WEBSITE", "description": "Website purely made with CHATGPT ", "link": "https://sudhanshu976.github.io/"},
    {"name": "POWER BI DASHBOARDS", "description": "Data Cleaning / Power BI Dashboards.", "link": "https://personalsudhanshu.streamlit.app/POWER-BI_PROJECTS"},
    {"name": "ML-APP", "description": " ML-MODEL FLASK APP ", "link": "https://personalsudhanshu.streamlit.app/FOOTBALL_PREDICTION_ML_FLASK_APP"},
    {"name": "NLP PROJECTS", "description": "4 NLP projects", "link": "https://personalsudhanshu.streamlit.app/NLP_PROJECTS"},
    {"name": "POTATO DISEASE CLASSIFIER", "description":"CNN APP for Image Classification", "link": "https://personalsudhanshu.streamlit.app/POTATO_DISEASE_CLASSIFIER"},
    {"name": "MALARIA DIAGNOSIS", "description": "Image Classification", "link": "https://personalsudhanshu.streamlit.app/MALARIA_DIAGNOSIS"},
    {"name": "HUMAN EMOTIONS DETECTOR", "description": "Image-Classification", "link": "https://personalsudhanshu.streamlit.app/HUMAN_EMOTIONS_DETECTOR"},
    {"name": "CAR COUNTER APP", "description": "Object-Detection / Tracking / YOLO ", "link": "https://personalsudhanshu.streamlit.app/CAR_COUNTER_APP_(_CV-1_)"},
    {"name": "FACE ATTENDANCE SYSTEM", "description": "OpenCV / Face-recognition library ", "link": "https://personalsudhanshu.streamlit.app/FACE_ATTENDANCE_SYSTEM_(_CV-2)"},
    {"name": "REAL OR FAKE PERSON DETECTOR", "description": "OpenCV / Custom Model Object Detection / YOLO / Model ZOO", "link": "https://personalsudhanshu.streamlit.app/REAL_OR_FAKE_PERSON_DETECTOR_(CV-3)"},
]

# Display project list with links
for project in projects:
    st.write(f"**{project['name']}**: {project['description']} - [Link to Project]({project['link']})")

