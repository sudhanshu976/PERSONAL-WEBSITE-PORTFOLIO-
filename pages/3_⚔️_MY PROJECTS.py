import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="PERSONAL WEBSITE"
)

# Main content
st.title("My Projects")

# List of projects
projects = [
    {"name": "ATM APP", "description": "Python and SQL Project", "link": "ATM-APP"},
    {"name": "BLOG WEBSITE", "description": "Website purely made with CHATGPT", "link": "https://sudhanshu976.github.io/"},
    {"name": "POWER BI DASHBOARDS", "description": "Data Cleaning / Power BI Dashboards", "link": "POWER-BI_PROJECTS"},
    {"name": "ML-APP", "description": "ML-MODEL FLASK APP", "link": "FOOTBALL_PREDICTION_ML_FLASK_APP"},
    {"name": "MLOPS PROJECT 1 (Regression)", "description": "MLOPS / Python / CI-CD Pipeline", "link": "MLOPS_PROJECT"},
    {"name": "MLOPS PROJECT 2 (Classification)", "description": "MLOPS / Python / Azure / Github Actions", "link": "MUSHROOM_MLOPS"},
    {"name": "NLP PROJECTS", "description": "4 NLP projects", "link": "NLP_PROJECTS"},
    {"name": "POTATO DISEASE CLASSIFIER", "description": "CNN APP for Image Classification", "link": "POTATO_DISEASE_CLASSIFIER"},
    {"name": "MALARIA DIAGNOSIS", "description": "Image Classification", "link": "MALARIA_DIAGNOSIS"},
    {"name": "HUMAN EMOTIONS DETECTOR", "description": "Image-Classification", "link": "HUMAN_EMOTIONS_DETECTOR"},
    {"name": "CAR COUNTER APP", "description": "Object-Detection / Tracking / YOLO", "link": "CAR_COUNTER_APP_(_CV-1_)"},
    {"name": "FACE ATTENDANCE SYSTEM", "description": "OpenCV / Face-recognition library", "link": "FACE_ATTENDANCE_SYSTEM_(_CV-2_)"},
    {"name": "REAL OR FAKE PERSON DETECTOR", "description": "OpenCV / Custom Model Object Detection / Model ZOO", "link": "REAL_OR_FAKE_PERSON_DETECTOR_(CV-3)"},
    {"name": "INVOICE EXTRACTOR USING GEMINI AI", "description": "  Streamlit | Langchain | Geminni-Pro-Vision ", "link": "INVOICE_EXTRACTOR_GENAI"},
    {"name": "MULTIPLE PDF QUERY USING GEMINI AI", "description": "  Streamlit | CASSANDRA |Langchain | Geminni-Pro-Vision ", "link": "CHAT_WITH_MULTIPLE_PDF_GEMINI"},
    {"name": "CAR ANALYZER USING GEMINI AI", "description": "  Streamlit | Geminni-Pro-Vision ", "link": "CAR_ANALYZER_USING_GEMINI"},
    {"name": "POTATO DISEASE DETECTOR USING CNN AND MLOPS", "description": " MLOPS | CNN | Tensorflow | MLFLOW | Flask ", "link": "POTATO_DISEASE_DETECTOR_MLOPS"},
    {"name": "BLOG GENERATOR USING LLAMA", "description": "Streamlit | Langchain | LLAMA-2", "link": "BLOG_GENERATOR_USING_LLAMA"},
    {"name": "FAKE NEWS CLASSIFIER USING LSTM", "description": " Flask| Tensorflow | LSTM  ", "link": "FAKE_NEWS_CLASSIFIER_USING_LSTM"},
    {"name": "MOVIE RECOMMENDER SYSTEM", "description": " Content Based Recommendation | Cosine Similarity | Flask | Streamlit ", "link": "MOVIE_RECOMMENDER_SYSTEM"}
]

# Display project list with numbers and links
for index, project in enumerate(projects, start=1):
    st.markdown(f"{index}. **{project['name']}**: {project['description']} - [Link to Project]({project['link']})")
