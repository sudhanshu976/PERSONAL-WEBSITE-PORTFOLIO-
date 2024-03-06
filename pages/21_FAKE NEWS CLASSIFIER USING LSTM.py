import streamlit as st
st.set_page_config(
    page_title="PERSONAL WEBSITE")

if st.button("Go to Project"):
    redirect_link = "https://github.com/sudhanshu976/-FAKE-NEWS-CLASSIFIER-USING-LSTM-WITH-WEB-APP"  # Replace with the URL you want to redirect to
    st.markdown(f"[Click here to go to this project code]({redirect_link})")

st.title(" FAKE NEWS CLASSIFIER USING LSTM ")
video_path = "videos/fake_news.mp4"
st.video(video_path)