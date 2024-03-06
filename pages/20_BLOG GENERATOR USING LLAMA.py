import streamlit as st
st.set_page_config(
    page_title="PERSONAL WEBSITE")

if st.button("Go to Project"):
    redirect_link = "https://github.com/sudhanshu976/BLOG-GENERATOR-USING-LLAMA-GEN-AI--4"  # Replace with the URL you want to redirect to
    st.markdown(f"[Click here to go to this project code]({redirect_link})")

st.title(" BLOG GENERATOR USING LLAMA MODEL ")
video_path = "videos/blog_gen.mp4"
st.video(video_path)