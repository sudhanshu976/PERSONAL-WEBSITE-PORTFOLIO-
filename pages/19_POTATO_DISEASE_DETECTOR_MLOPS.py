import streamlit as st
st.set_page_config(
    page_title="PERSONAL WEBSITE")

if st.button("Go to Project"):
    redirect_link = "https://github.com/sudhanshu976/PLANT-DISEASE-DETECTOR-CNN-MLOPS"  # Replace with the URL you want to redirect to
    st.markdown(f"[Click here to go to this project code]({redirect_link})")

st.title("POTATO DISEASE DETECTOR USING CNN MLOPS VERSION ")
video_path = "videos/potato_mlops.mp4"
st.video(video_path)


if st.button("KNOW MORE"):
    st.write("""

Certainly! Here's the information in plain text format:

```
Potato Disease Classifier - Project Readme

## Installation
Install dependencies:
pip install -r requirements.txt
Execute setup:
pip install -e .

## Customization
Tailor the project setup by editing setup.py according to your preferences.

## Project Structure
### Logger and Exception Handling:
Manage logging information and exception handling.
Logs stored in the 'logs' folder.
/logger
/exception

### Main Components (src/components):
Organized steps for data ingestion, preparation, model training, evaluation, and saving.
/src
  /components
    data_ingestion.py
    data_preparation.py
    model_training.py
    model_evaluation.py
    model_saving.py

### Training Pipeline (src/pipeline/training_pipeline.py):
Execute with:
python src/pipeline/training_pipeline.py
Sequentially triggers all component steps.
Generates 'artifacts' folder with unzipped and saved model folders.

### Raw Data (raw_data folder):
Contains a zip file of raw data.
/raw_data
  raw_data.zip

### Web Application (application.py):
Flask app for the user interface.
/application.py

### HTML Template (templates/index.html):
Enhances the look of the webpage.
/templates
  /index.html

### Static Content (static/upload.js):
Manages image uploading on the webpage.
/static
  /upload.js

## Usage
Run the training pipeline:
python src/pipeline/training_pipeline.py
Launch the Flask app:
python application.py
Access the webpage in your browser.
```




""")
