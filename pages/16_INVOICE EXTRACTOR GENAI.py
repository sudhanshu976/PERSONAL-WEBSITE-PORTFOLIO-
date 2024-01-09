import streamlit as st
st.set_page_config(
    page_title="PERSONAL WEBSITE")

if st.button("Go to Project"):
    redirect_link = "https://github.com/sudhanshu976/INVOICE-EXTRACTOR-GEN-AI-1-"  # Replace with the URL you want to redirect to
    st.markdown(f"[Click here to go to this project code]({redirect_link})")

st.title("INVOICE EXTRACTOR GENAI PROJECT USING GEMINI")
video_path = "videos/invoice.mp4"
st.video(video_path)

if st.button("KNOW MORE"):
    st.write("""
**Importing Libraries:**

The code starts by importing necessary libraries, including Streamlit, the dotenv module for managing environment variables, the os module, the PIL library for working with images, and the google.generativeai module for using the Gemini Pro Vision model.

**Configuring Google API Key:**

The Google API key is loaded from the environment variables using `load_dotenv()` and configured for the Gemini Pro Vision model using `genai.configure()`.

**Defining Functions:**

- `get_gemini_response`: Takes input, an image, and a prompt as parameters, initializes the Gemini Pro Vision model, and generates a response based on the input parameters.
- `input_image_setup`: Takes an uploaded file as a parameter, reads the file into bytes, and returns a list containing the mime type and data of the uploaded file.

**Setting Streamlit Page Configuration:**

`st.set_page_config` is used to set the title of the Streamlit page to "Gemini Image Demo."

**Creating Streamlit Interface:**

- `st.header` is used to display a header for the application.
- `st.text_input` is used to get an input prompt from the user.
- `st.file_uploader` is used to allow users to upload image files (JPEG or PNG).
- If an image is uploaded, it is displayed using `st.image` with a specified width.
- A "Tell me about the image" button (`st.button`) is provided.

**Handling Button Click:**

When the "Tell me about the image" button is clicked, the `input_image_setup` function is called to prepare the image for processing.
The `get_gemini_response` function is then called with the input prompt, processed image data, and the user input.
The response generated by the Gemini Pro Vision model is displayed using `st.subheader` and `st.write`.
""")