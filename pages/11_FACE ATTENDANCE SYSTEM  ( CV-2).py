import streamlit as st
st.set_page_config(
    page_title="PERSONAL WEBSITE"
)
if st.button("Go to Project"):
    redirect_link = "https://github.com/sudhanshu976/CV-2-FACE-ATTENDANCE-SYSTEM-ALONG-WITH-STREAMLIT"  # Replace with the URL you want to redirect to
    st.markdown(f"[Click here to go to this project code]({redirect_link})")

st.title("FACE ATTENDANCE SYSTEM")

st.write("""

#### This is a FACE DETECTION ATTENDANCE SYSTEM made using face-recognition library , Python and OpenCV  :
- **1. INPUT** : It takes realtime webcam as input       
- **2. PROCESSING** : There is a model that is trained to identify the images present in images folder and matches them with images in webcam.
         
- **3. OUTPUT** : If person in webcam matches with person in images folder , it show a bounding box along with name of that person and also stores the name , time in a csv file .
""")

if st.button("KNOW ABOUT MODEL"):
    st.write("""

### Purpose:
The code aims to perform face recognition using the `face_recognition` library in Python. It identifies faces in a live video stream from a webcam, compares them to a set of known images, and marks attendance for recognized individuals.

### Key Components:
1. **Imports:**
    - Libraries like `cv2`, `pandas`, `numpy`, `face_recognition`, `os`, `cvzone`, and `datetime` are imported for image manipulation, data handling, face recognition, file system operations, and time functions.

2. **Attendance Marking:**
    - The `markAttendance` function records the name and current time of recognized individuals in a CSV file (`attendance.csv`).

3. **Image Loading and Encoding:**
    - Images stored in a specified directory (`images_attendance`) are loaded using OpenCV (`cv2`) and their class names are extracted for identification.
    - The `find_encodings` function processes these images to generate their facial encodings using the `face_recognition` library.

4. **Webcam Face Recognition:**
    - The code initializes the webcam (`cv2.VideoCapture`) and continuously captures frames.
    - It identifies faces in the captured frames and generates their encodings.
    - Compares the captured face encodings with the known face encodings.
    - If a match is found, it retrieves the name and marks attendance using the `markAttendance` function.
    - Utilizes `cvzone` for drawing rectangles around detected faces and displaying person information on the screen.

### Processes:
1. **Initialization:**
    - Images are loaded and encoded for known face recognition.
    - The webcam feed is initiated.

2. **Recognition Loop:**
    - The code continuously captures frames from the webcam.
    - It detects faces in the frames and compares them with known faces' encodings.
    - Upon a match, it retrieves the name and marks attendance.
    - Utilizes `cvzone` for visual indications of recognized faces and displaying person information.

### User Interaction:
- The program runs until the user quits by pressing the 'q' key.
- The recognized faces are highlighted and their names are displayed on the screen using rectangles and text.

### Conclusion:
The code achieves real-time face recognition through a webcam feed, comparing detected faces with a set of known images' encodings. When a match is found, it marks the attendance of recognized individuals by logging their names and timestamps in an 'attendance.csv' file. The visual interface provides real-time feedback on recognized faces.
""")
    
video_path = "videos/attendance_system.mp4"
st.video(video_path)


st.error("Sorry for the poor video quality . I don't have a dedicated GPU on my PC that's why this is lagging this much" )