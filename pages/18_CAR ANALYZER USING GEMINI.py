import streamlit as st
st.set_page_config(
    page_title="PERSONAL WEBSITE")

if st.button("Go to Project"):
    redirect_link = "https://github.com/sudhanshu976/CAR-ANALYZER-USING-GEMINI-GEN-AI-3-"  # Replace with the URL you want to redirect to
    st.markdown(f"[Click here to go to this project code]({redirect_link})")

st.title("CHAT WITH MULTIPLE PDF USING GEMINI")
video_path = "videos/car_analyzer.mp4"
st.video(video_path)


if st.button("KNOW MORE"):
    st.write("""

---

### Car Analyzer using GEMINI

#### Overview

The "Car Analyzer using GEMINI" is a Streamlit application designed to predict car models, estimate prices, and provide specifications based on uploaded car images. It leverages Google's GEMINI-Pro Vision model for image analysis and content generation.

#### Key Features

1. **Input and Image Setup:**
   - Users can input a prompt describing the desired information about the car model, price, and specifications.
   - An image uploader allows users to upload images of cars in JPEG, JPG, or PNG format.

2. **GEMINI Interaction:**
   - GEMINI-Pro Vision model is utilized to generate content based on the provided input, image, and prompt.
   - The application configures GEMINI with the provided API key using the `google.generativeai` library.

3. **User Interface:**
   - Streamlit is used to create a user-friendly interface.
   - The uploaded image is displayed with a width of 350 pixels for visual inspection.

4. **Response Display:**
   - Upon clicking the "ANALYZE THE CAR" button, the application processes the input and displays the generated response.
   - The response includes predicted car details, estimated price, and a format for additional specifications.

#### How to Run

1. Install required dependencies: `streamlit`, `pillow`, `google.generativeai`, `python-dotenv`.
2. Set up a `.env` file with the Google API key.
3. Run the Streamlit app: `streamlit run car_analyzer.py`.

#### Notes

- Ensure a secure handling of the API key, especially in production environments.
- The application assumes availability of the GEMINI API key as an environment variable.

---

This application provides a straightforward and interactive way for users to analyze and retrieve information about cars based on uploaded images. The combination of Streamlit and GEMINI makes it easy to use and deploy.
""")