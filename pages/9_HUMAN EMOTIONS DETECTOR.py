import streamlit as st
st.set_page_config(
    page_title="PERSONAL WEBSITE"
)
b1 , b2 = st.columns(2)
with b1:
    if st.button("Go to Project"):
        redirect_link = "https://github.com/sudhanshu976/COMPUTER_VISION_APP/blob/main/pages/5_HUMAN_EMOTION_DETECTOR.py"  # Replace with the URL you want to redirect to
        st.markdown(f"[Click here to go to this project code]({redirect_link})")
with b2:
    if st.button("Go to Website"):
        redirect_link = "https://cvappbysudhanshu.streamlit.app/"  # Replace with the URL you want to redirect to
        st.markdown(f"[Click here to go to this website]({redirect_link})")
st.title("HUMAN EMOTIONS DETECTOR")
st.write("""

#### This is a Human Emotions Detector made using Deep Learning . It includes :
- **1. INPUT** : User has to input the image of a person's face      
- **2. PROCESSING** : There is a model that is trained on the HEFS Dataset that will predict the output 
         
- **3. OUTPUT** : The model will predict whether the person is happy , angry or sad
""")

if st.button("KNOW ABOUT MODEL"):
    st.write("""
The architecture described is a deep learning model designed to classify human emotions (happy, angry, or sad) based on input images. This model leverages the power of the ViT (Vision Transformer) architecture and is deployed using Streamlit for user interaction.

1. **Hugging Face Model**:
   - You start by defining the Hugging Face model `'google/vit-base-patch16-224-in21k'`. This is a pre-trained ViT model by Google, which is capable of processing image data for various tasks.

2. **Custom Configuration**:
   - Next, you create a custom ViT configuration by specifying a hidden size of 144. This allows you to fine-tune the model according to your specific requirements.

3. **ViT Model**:
   - You initialize a ViT model using the custom configuration. This ViT model is designed to handle image data and extract meaningful features.

4. **Data Preprocessing Layers**:
   - Before feeding the image data into the ViT model, you set up a series of data preprocessing layers. These layers include:
      - **Resizing**: Resizes the input image to a standard size of 224x224 pixels.
      - **Rescaling**: Normalizes the pixel values to the range [0, 1].
      - **Permute**: Reorders the dimensions of the data to match the model's expected input format.

5. **Feature Extraction**:
   - You load a pre-trained ViT model using the Hugging Face library. This model has been pre-trained on a large dataset and can extract rich features from input images.

6. **Input Layer**:
   - You define an input layer with a shape of (256, 256, 3), indicating that the model expects RGB images with a resolution of 256x256 pixels and 3 color channels.

7. **Model Forward Pass**:
   - You pass the preprocessed input data through the ViT model by applying the resizing and other preprocessing layers. The ViT model extracts features from the image data.

8. **Output Layer**:
   - After processing the image through the ViT model, you extract the relevant features from the model's output. In this case, you take the first position of the output ([:, 0, :]) and connect it to a dense layer with 3 units, using a softmax activation function. This final dense layer is responsible for classifying the emotions into one of the three categories: happy, angry, or sad.

9. **Keras Model**:
   - You create a Keras model that takes the preprocessed input image and produces an output prediction for the emotion classification task.

10. **Deployment with Streamlit**:
   - After defining the architecture of your model, you can deploy it using Streamlit. Streamlit is a Python library for creating interactive web applications with ease. You can use Streamlit to build a user-friendly interface where users can upload images, and your model will classify the emotions of the people in those images in real-time.

In summary, this architecture combines the power of ViT models for image feature extraction with the flexibility of Keras for building the classification head. It allows you to create an interactive application to classify human emotions based on input images, making it accessible and user-friendly.


""")
    

video_path = "videos/human_emotions_model.mp4"
st.video(video_path)