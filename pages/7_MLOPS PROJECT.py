import streamlit as st
st.set_page_config(
    page_title="PERSONAL WEBSITE"
)
if st.button("Go to Project"):
    redirect_link = "https://github.com/sudhanshu976/MLOPS-PROJECT"  # Replace with the URL you want to redirect to
    st.markdown(f"[Click here to go to this project code]({redirect_link})")

st.title("MLOPS PROJECT")
st.write("""
### ✨ MLOps Project Highlights! ✨

1. **Custom Logger & Exception Handling**
   - Implemented a robust logging system for effective monitoring.
   - Developed custom exception files for seamless error handling.

2. **Modular Components**
   - Created modules: data_ingestion, data_transformation, best_model_finder, model_trainer.
   - Each module contributes to a specific step in the ML pipeline.

3. **Unified Training Pipeline**
   - Integrated modules into a cohesive train_pipeline for end-to-end model training.
   - Centralized logs for comprehensive tracking and analysis.

4. **Scalable Predict Pipeline**
   - Expanded capabilities with a predict_pipeline for streamlined predictions.
   - Integrated into a user-friendly Flask app for interactive experiences.

5. **Azure Deployment with GitHub Actions**
   - Deployed the project on Microsoft Azure for scalability and accessibility.
   - Automated deployment through GitHub Actions for seamless integration.

""")
video_path = "videos/mlops_video.mp4"
st.video(video_path)
st.image("images/mlops_dir.png", width=250)
