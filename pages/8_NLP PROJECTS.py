import streamlit as st
st.set_page_config(
    page_title="PERSONAL WEBSITE"
)
st.error("NLP is not my expertise. These are just basic projects and to showcase that I am familiar with NLP  ")
b1 , b2 = st.columns(2)
with b1:
    if st.button("Go to Project"):
        redirect_link = "https://github.com/sudhanshu976/ALL-NLP-PROJECTS"  # Replace with the URL you want to redirect to
        st.markdown(f"[Click here to go to this project code]({redirect_link})")
with b2:
    if st.button("Go to Website"):
        redirect_link = "https://nlpappbysudhanshu.streamlit.app/"  # Replace with the URL you want to redirect to
        st.markdown(f"[Click here to go to this website]({redirect_link})")

st.title("NLP PROJECTS")
st.write("""

#### There are 4 NLP projects . This include :
- **1. LANGUAGE DETECTOR MODEL** : Made using Machine learning and NLP Concepts         
- **2. SMS SPAM CLASSIFIER** : Made using Machine learning and NLP Concepts
         
- **3. SENTIMENT ANALYZER** : Made using Hugging Face Transformers  
         
- **4. NEXT WORD PREDICTOR** : Made using LSTM(Deep Learning) and NLP Concepts
""")

st.write("-------------------------------------------------------------------------------------------------------")

video_path1 = 'videos/language_detector.mp4'
st.video(video_path1)
st.write("-------------------------------------------------------------------------------------------------------")

video_path2 = 'videos/spam.mp4'
st.video(video_path2)