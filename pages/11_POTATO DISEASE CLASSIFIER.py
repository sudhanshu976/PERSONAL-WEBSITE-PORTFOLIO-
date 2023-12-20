import streamlit as st
st.set_page_config(
    page_title="PERSONAL WEBSITE"
)
b1 , b2 = st.columns(2)
with b1:
    if st.button("Go to Project"):
        redirect_link = "https://github.com/sudhanshu976/COMPUTER_VISION_APP/blob/main/pages/4_POTATO-DISEASE-CLASSIFIER.py"  # Replace with the URL you want to redirect to
        st.markdown(f"[Click here to go to this project code]({redirect_link})")
with b2:
    if st.button("Go to Website"):
        redirect_link = "https://cvappbysudhanshu.streamlit.app/"  # Replace with the URL you want to redirect to
        st.markdown(f"[Click here to go to this website]({redirect_link})")
st.title("POTATO DISEASE CLASSIFIER")
st.write("""

#### This is a Potato Disease Classifier made using Deep Learning . It includes :
- **1. INPUT** : User has to input the image of a potato leaf        
- **2. PROCESSING** : There is a model that is trained on the Potato Disease Dataset that will predict the output 
         
- **3. OUTPUT** : The model will predict whether the potato is healthy , has early-blight disease or has late-blight disease  
""")

if st.button("KNOW ABOUT MODEL"):
     st.write("""
## Potato-Disease Classifier CNN App Summary

**Model Architecture:**
- Model Type: Convolutional Neural Network (CNN)
- Number of Layers: 6 Convolutional Layers, 6 Max Pooling Layers, 2 Fully Connected Layers , Data Augmentation Layer and Data Preprocessing Layer

**Input:**
- Input Shape: (256, 256, 3)

**Training:**
- Training Data: Plant Village images dataset
- Optimizer: Adam
- Loss Function:  Categorical-Cross-Entropy
- Metrics: Accuracy
- Number of Epochs: 100
- Batch Size: 32

**Model Evaluation:**
- Validation Data: Separate dataset of potato leaf images
- Evaluation Metrics: Accuracy, Precision, Recall, F1-score

**Results:**
- Accuracy: 98%

**Conclusion:**
- The CNN model achieved an accuracy of 98% in detecting which potato is healthy , which is sufferiing from early blight disease and which is suffering from late blight disease, indicating strong performance.

**Deployment:**
- Deployment Platform: Web application
- User Interface: Users upload potato leaf images to the app, and it provides a detection of whether a potato is healthy , having late blight or early blight disease.

""")
     
video_path = "videos/potato_model.mp4"
st.video(video_path)