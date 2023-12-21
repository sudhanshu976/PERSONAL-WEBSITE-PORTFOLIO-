import streamlit as st
st.set_page_config(
    page_title="PERSONAL WEBSITE"
)
import streamlit as st

# Main content
st.title("My Projects")

# List of projects
projects = [
    {"name": "ATM APP", "description": "Python and SQL Project", "link": "ATM-APP"},
    {"name": "BLOG WEBSITE", "description": "Website purely made with CHATGPT ", "link": "https://sudhanshu976.github.io/"},
    {"name": "POWER BI DASHBOARDS", "description": "Data Cleaning / Power BI Dashboards.", "link": "POWER-BI_PROJECTS"},
    {"name": "ML-APP", "description": " ML-MODEL FLASK APP ", "link": "FOOTBALL_PREDICTION_ML_FLASK_APP"},
    {"name": "MLOPS PROJECT 1", "description": "MLOPS / Python / CI-CD Pipeline", "link": "MLOPS_PROJECT"},
    {"name": "NLP PROJECTS", "description": "4 NLP projects", "link": "NLP_PROJECTS"},
    {"name": "POTATO DISEASE CLASSIFIER", "description":"CNN APP for Image Classification", "link": "POTATO_DISEASE_CLASSIFIER"},
    {"name": "MALARIA DIAGNOSIS", "description": "Image Classification", "link": "MALARIA_DIAGNOSIS"},
    {"name": "HUMAN EMOTIONS DETECTOR", "description": "Image-Classification", "link": "HUMAN_EMOTIONS_DETECTOR"},
    {"name": "CAR COUNTER APP", "description": "Object-Detection / Tracking / YOLO ", "link": "CAR_COUNTER_APP_(_CV-1_)"},
    {"name": "FACE ATTENDANCE SYSTEM", "description": "OpenCV / Face-recognition library ", "link": "FACE_ATTENDANCE_SYSTEM_(_CV-2)"},
    {"name": "REAL OR FAKE PERSON DETECTOR", "description": "OpenCV / Custom Model Object Detection / Model ZOO", "link": "REAL_OR_FAKE_PERSON_DETECTOR_(CV-3)"},
]

# Display project list with links
for project in projects:
    st.write(f"**{project['name']}**: {project['description']} - [Link to Project]({project['link']})")

