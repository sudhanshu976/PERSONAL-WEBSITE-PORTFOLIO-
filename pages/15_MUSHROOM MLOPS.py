import streamlit as st
st.set_page_config(
    page_title="PERSONAL WEBSITE"
)
if st.button("Go to Project"):
    redirect_link = "https://github.com/sudhanshu976/MUSHROOM-CLASSIFIER-MLOPS-PROJECT"  # Replace with the URL you want to redirect to
    st.markdown(f"[Click here to go to this project code]({redirect_link})")

st.title("MUSHROOM CLASSIFIER MLOPS PROJECT")
video_path = "videos/mushroom.mp4"
st.video(video_path)

if st.button("KNOW MORE"):
    st.write("""
    Great job on building the components of your mushroom classifier app! Now, you can integrate these components into a Flask app to make it interactive. Here are the steps to create an interactive Flask app for your mushroom classifier:

    ### Step 1: Flask App Setup

    1. **Install Flask:**
    - Make sure Flask is installed in your environment. You can install it using:
        ```
        pip install Flask
        ```

    2. **Create Flask App:**
    - Create a new Python file (e.g., `app.py`) for your Flask application.

    3. **Import Dependencies:**
    - Import necessary libraries, including Flask.

    ### Step 2: Create Flask Routes

    1. **Define Routes:**
    - Create routes for different pages of your app. For example:
        ```python
        from flask import Flask, render_template, request

        app = Flask(__name__)

        @app.route('/')
        def home():
            return render_template('index.html')

        @app.route('/predict', methods=['POST'])
        def predict():
            # Extract input from the form
            # Call your prediction function
            # Render the result template
        ```

    ### Step 3: Create HTML Templates

    1. **Create Templates Folder:**
    - Create a folder named `templates` in the same directory as your Flask app.

    2. **HTML Templates:**
    - Create HTML templates for your app. For example, `index.html` for the home page and `result.html` for displaying predictions.

    ### Step 4: Implement Prediction Function

    1. **Prediction Function:**
    - Implement a function that takes input from the user, calls the model for prediction, and returns the result.

    ### Step 5: Integrate Components

    1. **Integrate Data Ingestion, Transformation, and Model Loading:**
    - Ensure that your Flask app can load the necessary data, perform transformations, and load the trained model.

    2. **Call Prediction Function:**
    - In the `/predict` route, call the prediction function with user input.

    ### Step 6: Run Flask App

    1. **Run the App:**
    - In your terminal, run the Flask app:
        ```
        python app.py
        ```
    - Access the app in your web browser at `http://localhost:5000`.

    ### Step 7: Enhance User Interface (Optional)

    1. **Form for User Input:**
    - Enhance the HTML templates to include a form for users to input mushroom features.

    2. **Styling:**
    - Apply CSS styles to make your app visually appealing.

    ### Step 8: Deploy to Production (Optional)

    1. **Choose a Deployment Platform:**
    - Choose a platform to deploy your Flask app, such as Heroku, AWS, or GCP.

    2. **Update Configuration:**
    - Update configurations for production, such as setting `debug=False` and using a production-ready web server (e.g., Gunicorn).

    3. **Deploy:**
    - Deploy your Flask app to the chosen platform.

    ### Step 9: Testing

    1. **Test the App:**
    - Test your interactive Flask app by providing different inputs and verifying the predictions.

    Congratulations! You've now created an interactive Flask app for your mushroom classifier. Users can input mushroom features, and your app will provide predictions on whether they are edible or poisonous. Remember to continually test and improve your app based on user feedback and any issues that arise.
    """)