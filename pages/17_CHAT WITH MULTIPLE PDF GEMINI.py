import streamlit as st
st.set_page_config(
    page_title="PERSONAL WEBSITE")

if st.button("Go to Project"):
    redirect_link = "https://github.com/sudhanshu976/CHAT-WITH-MULTIPLE-PDF-GEN-AI---2-"  # Replace with the URL you want to redirect to
    st.markdown(f"[Click here to go to this project code]({redirect_link})")

st.title("CHAT WITH MULTIPLE PDF USING GEMINI")
video_path = "videos/multiple_pdf.mp4"
st.video(video_path)


if st.button("KNOW MORE"):
    st.write("""
Certainly! Here's a comprehensive summary of the provided code:

1. **Imports and Setup:**
   - The code begins by importing necessary libraries and modules, such as Streamlit, PyPDF2, os, Google's generative AI, and others.
   - It also configures the Google generative AI with the provided API key.

2. **PDF Processing Functions:**
   - The `get_pdf_text` function extracts text from PDFs using PyPDF2, concatenating text from all pages of each PDF.
   - The `get_chunks` function splits the extracted text into chunks using a RecursiveCharacterTextSplitter.

3. **Vector Store Generation:**
   - The `get_vector_store` function uses GoogleGenerativeAIEmbeddings to embed text chunks and creates a FAISS vector store from these embeddings. The vector store is then saved locally.

4. **Conversation Chain Setup:**
   - The `get_conversation` function sets up a conversation chain for question answering using Google's Gemini Pro model. It defines a template for prompts with context and question placeholders.

5. **User Input Processing:**
   - The `user_input` function takes a user's question as input, performs a similarity search using the vector store, and initiates a conversation chain to generate a response. The response is then printed and displayed using Streamlit.

6. **Main Streamlit Application:**
   - The `main` function configures the Streamlit page, sets a title, and creates a user interface.
   - Users can input questions, click the "Ask" button to generate responses, and upload multiple PDFs using the sidebar. PDFs are processed to create a vector store for subsequent question answering.

7. **Execution:**
   - The `if __name__ == "__main__":` block ensures that the `main` function is executed when the script is run.

In summary, this code creates a Streamlit application that allows users to ask questions based on uploaded PDFs. It utilizes Google's generative AI for question answering and employs techniques like text chunking and vector stores to enhance performance.
""")
