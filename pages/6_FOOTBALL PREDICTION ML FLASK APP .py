import streamlit as st
st.set_page_config(
    page_title="PERSONAL WEBSITE"
)
if st.button("Go to Project"):
    redirect_link = "https://github.com/sudhanshu976/FOOTBALL-PLAYER-TRANSFER-FEE-PREDICTION-ML-APP"  # Replace with the URL you want to redirect to
    st.markdown(f"[Click here to go to this project code]({redirect_link})")

st.title("FOOTBALL PLAYER TRANSFER FEE PREDICTION ML APP ")
st.header("1. Data Exploration and Preparation")
st.write("All the data collection, data preparation, and data analysis have been meticulously performed in this notebook.")

# Section 2: Feature Engineering and Selection
st.header("2. Feature Engineering and Selection")
st.write("The notebook covers detailed explanations of feature engineering and the selection process to enhance model performance.")

# Section 3: Model Selection and Training
st.header("3. Model Selection and Training")
st.write("Various models were considered, and the selected model was trained using the prepared data.")

# Section 4: Flask App Development
st.header("4. Flask App Development")
st.write("After extracting the trained model, it was integrated into a Flask App for user-friendly predictions.")


video_path = "videos/ml_app.mp4"
st.video(video_path)