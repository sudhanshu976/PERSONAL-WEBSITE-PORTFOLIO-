import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="PERSONAL WEBSITE",
    page_icon=":computer:",
    layout="wide"
)

#---------------------LOTTIE  ANIMATION ------------------------
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottie("https://lottie.host/e0a6d7e0-6b3d-428f-addc-aa44a746d653/MImt8ecbMs.json")

st.sidebar.success("Select a page above")

# -------------- HEADER ----------------------------
with st.container():
    st.subheader("Hi, I am Sudhanshu :wave:")
    st.title("A Data Scientist and Computer Vision Engineer from INDIA")
    st.write("I am passionate about finding ways to solve real-life problems through my skills in ML, DL, and Computer Vision.")
    st.write("[Know more about me >>](https://www.linkedin.com/in/sudhanshu-gusain976))")

    st.write("[My Blog Website >>](https://sudhanshu976.github.io/))")
    st.write("[My NLP Website >>](https://nlpappbysudhanshu.streamlit.app/))")
    st.write("[My Computer Vision Website >>](https://cvappbysudhanshu.streamlit.app/))")

    st.write("All above mentioned websites are already mentioned in the Project section of this Portfolio Website")

# -------------- MY EXPERTISE ----------------------------

# Function to create a skill card
def create_skill_card(title, description):
    card = f"""
    <div style="
        background-color: #343a40; /* Dark background color */
        color: #ffffff; /* Light text color */
        border: 1px solid #55595c; /* Border color */
        border-radius: 8px;
        padding: 15px;
        margin: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        overflow: hidden; /* Add overflow to prevent shadow clipping */
        text-align: center; /* Center text */
    ">
        <h3 style="margin-bottom: 10px;">{title}</h3>
        <p>{description}</p>
    </div>
    """
    return card

# Main content
st.title("My Skills")

# List of skills
skills = [
    {"title": "Python ans SQL", "description": "Proficient in Python programming language and intermediate in SQL"},
    {"title": "Machine Learning", "description": "Experience in building ML models and Deeep Lnowledge of ML algorithms"},
    {"title": "Data Visualization", "description": "Creating interactive visualizations with tools like Power-BI, Matplotlib and Seaborn."},
    {"title": "ML OPS", "description": "In love with ML-OPS"},
    {"title": "Deep Learning", "description": "Working with neural networks and frameworks like TensorFlow."},
    {"title": "Natural Language Processing", "description": "Recommender System , LLM , Transfer Learning , Generative AI"},
    {"title": "Computer Vision", "description": "Object Detection , Posture Detection , GAN , Image Classification"},
    {"title": "CHATGPT", "description": "Good at utilizing CHATGPT and Other AI tools .  Even made a website with zero knowledge of HTML,CSS and JS"},
]

# Display skill cards in two columns
col1, col2 = st.columns(2)
for i, skill in enumerate(skills):
    if i % 2 == 0:
        with col1:
            st.markdown(create_skill_card(skill["title"], skill["description"]), unsafe_allow_html=True)
    else:
        with col2:
            st.markdown(create_skill_card(skill["title"], skill["description"]), unsafe_allow_html=True)
    

# ----------------- LOTTIE ANIMATION -----------------------
with st.container():
    st.write("--------------------------------------------------------------------------------------------------")

with st.container():
    st_lottie(lottie_coding)


    