import streamlit as st
st.set_page_config(
    page_title="PERSONAL WEBSITE")

if st.button("Go to Project"):
    redirect_link = "https://github.com/sudhanshu976/DEADLIFT-TRACKER-FITNESS-APP-OPENCV-"  # Replace with the URL you want to redirect to
    st.markdown(f"[Click here to go to this project code]({redirect_link})")

st.title(" DEADLIFT POSE ANLYZER  ")
video_path = "videos/deadlift.mp4"
st.video(video_path)