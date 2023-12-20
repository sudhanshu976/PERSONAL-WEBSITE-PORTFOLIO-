import streamlit as st
st.set_page_config(
    page_title="PERSONAL WEBSITE"
)
if st.button("Go to Project"):
    redirect_link = "https://github.com/sudhanshu976/CV-1-CAR-COUNTER"  # Replace with the URL you want to redirect to
    st.markdown(f"[Click here to go to this project code]({redirect_link})")

st.title("CAR COUNTER APP")

st.write("#### This is a Basic Car Counter App made using OpenCV and some additional python libraries like cv-zone , a tracker git file named sort")
st.write("##### It detects the car or any other vehicles using YOLO V8 NANO model and then sort is used to give id to each car . Mask is added to detect cars in specific regions only and then there is a counter which detects how many carr pass by a specific line .")

if st.button("KNOW ABOUT MODEL"):
    st.write("""
The provided Python app is designed for object detection, tracking, and counting in a video using the YOLO (You Only Look Once) model from the Ultralytics library and the SORT (Simple Online and Realtime Tracking) algorithm. Here's a short explanation of the code:

- Import necessary libraries such as OpenCV, Ultralytics, cvzone, SORT, and NumPy.

- Load a YOLOv5 model ('yolov8n.pt') using Ultralytics. This model is capable of detecting various objects in images and video frames.

- Set up a video capture to read frames from a video file ('footage.mp4').

- Define a list of object class names that the YOLO model can detect.

- Create a mask image ('mask.png') to overlay on the video frames. This mask is used to restrict the detection region in the video.

- Initialize a SORT tracker to assign unique IDs to tracked objects.

- Loop through each frame of the video:

a. Read the next frame from the video.

b. Apply the mask to the frame to limit the detection region.

c. Use the YOLO model to detect objects within the masked region.

d. Track the detected objects and assign unique IDs using SORT.

e. Draw bounding boxes around the detected and tracked objects.

f. Check if any objects cross a specific line (defined by 'limits') and count them.

g. Display the frame with bounding boxes, object IDs, and the count.

h. Continue looping through the video frames until the user presses 'q' to quit.

This code combines object detection, tracking, and counting to analyze objects in a video, making it useful for applications such as traffic monitoring or object counting in surveillance videos.


""")
    
video_path = "videos/car_counter.mp4"
st.video(video_path)