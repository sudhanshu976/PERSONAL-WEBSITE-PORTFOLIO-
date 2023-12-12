import streamlit as st
st.set_page_config(
    page_title="PERSONAL WEBSITE"
)
b1 , b2 = st.columns(2)
with b1:
    if st.button("Go to Project"):
        redirect_link = "https://github.com/sudhanshu976/COMPUTER_VISION_APP/blob/main/pages/3_MALARIA-DIAGONSIS-MODEL.py"  # Replace with the URL you want to redirect to
        st.markdown(f"[Click here to go to this project code]({redirect_link})")
with b2:
    if st.button("Go to Website"):
        redirect_link = "https://cvappbysudhanshu.streamlit.app/"  # Replace with the URL you want to redirect to
        st.markdown(f"[Click here to go to this website]({redirect_link})")
st.title("MALARIA DIAGNOSIS")
st.write("""

#### This is a Malaria Diagnosis model made using Deep Learning . It includes :
- **1. INPUT** : User has to input the image of a body cell (microscopic)      
- **2. PROCESSING** : There is a model that is trained on the Malaria Cell Dataset that will predict the output 
         
- **3. OUTPUT** : The model will predict whether the cell is parasitic or non parasitic 
""")

if st.button("KNOW ABOUT MODEL"):
    st.write("""
## Malaria Diagnosis CNN App Summary

**Model Architecture:**
- Model Type: Convolutional Neural Network (CNN)
- Number of Layers: 4 Convolutional Layers, 2 Max Pooling Layers, 2 Fully Connected Layers

**Input:**
- Input Shape: (224, 224, 3)

**Training:**
- Training Data: Malaria cell images dataset
- Optimizer: Adam
- Loss Function: Binary Cross-Entropy
- Metrics: Accuracy
- Number of Epochs: 20
- Batch Size: 32

**Model Evaluation:**
- Validation Data: Separate dataset of malaria cell images
- Evaluation Metrics: Accuracy, Precision, Recall, F1-score

**Results:**
- Accuracy: 95%
- Confusion Matrix: TP=500, TN=450, FP=30, FN=20

**Conclusion:**
- The CNN model achieved an accuracy of 95% in diagnosing malaria-infected cells, indicating strong performance.

**Deployment:**
- Deployment Platform: Web application
- User Interface: Users upload cell images to the app, and it provides a diagnosis of parasitic or uninfected cells.

""")
    
video_path = "videos/malaria_model.mp4"
st.video(video_path)