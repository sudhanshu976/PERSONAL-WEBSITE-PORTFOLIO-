import streamlit as st
st.set_page_config(
    page_title="PERSONAL WEBSITE"
)
if st.button("Go to Project"):
    redirect_link = "https://github.com/sudhanshu976/CV-3-REAL-OR-FAKE-PERSON-DETECTOR"  # Replace with the URL you want to redirect to
    st.markdown(f"[Click here to go to this project code]({redirect_link})")

st.title("CUSTOM TRAINED YOLOv5 PERSON DETECTOR : Real or Fake")

st.write("""

#### This is a CUSTOM TRAINED YOLOv5 PERSON DETECTOR made using Pytorch , YOLO and OpenCV  :
- **1. INPUT** : It takes realtime webcam as input       
- **2. PROCESSING** : There is a custom trained  model that is trained to detect whther a person in webcam is real or phone-copy or virtual copy of that person.
         
- **3. OUTPUT** : It labels the faces as real or fake in realtime . """)

if st.button("KNOW ABOUT MODEL"):
    st.write("""

1. **Clone YOLOv5 Repository and Install Requirements:**
   - Clones the YOLOv5 repository from Ultralytics.
   - Installs the required dependencies using the `requirements.txt` file.

   ```python
   !git clone https://github.com/ultralytics/yolov5
   !cd yolov5 && pip install -r requirements.txt
   ```

2. **Image Collection:**
   - Captures images from the webcam for two classes: "real" and "fake".
   - Saves the captured images in the `data/images` directory.

   ```python
   # ... (Image collection code)
   ```

3. **Labeling Tool Setup (LabelImg):**
   - Clones the LabelImg repository and installs required dependencies.

   ```python
   !git clone https://github.com/HumanSignal/labelImg
   !pip install pyqt5 lxml --upgrade
   !cd labelImg && pyrcc5 -o libs/resources.py resources.qrc
   ```

4. **YOLOv5 Training:**
   - Trains the YOLOv5 model using the collected and labeled images.
   - Uses the `train.py` script from YOLOv5 repository with specified parameters.

   ```python
   !cd yolov5 && python train.py --img 320 --batch 16 --epochs 50 --data dataset.yml --weights yolov5m.pt
   ```

5. **Load and Use Trained YOLOv5 Model:**
   - Loads the trained YOLOv5 model using `torch.hub.load`.
   - Captures video from the webcam and performs real-time object detection using the trained model.

   ```python
   model = torch.hub.load("ultralytics/yolov5", "custom", path="yolov5/runs/train/exp4/weights/best.pt", force_reload=True)
   cap = cv2.VideoCapture(0)
   
   while cap.isOpened():
       ret, frame = cap.read()
       results = model(frame)
       cv2.imshow("YOLO", np.squeeze(results.render()))
   
       if cv2.waitKey(10) & 0xff == ord('q'):
           break
   cap.release()
   cv2.destroyAllWindows()
   ```

In summary, this code collects images for two classes, "real" and "fake," trains a YOLOv5 model on these images, and then uses the trained model for real-time object detection on webcam frames. The LabelImg tool is used for image labeling, and the YOLOv5 model is loaded and applied using PyTorch.
""")
    
video_path = "videos/spoof_detector.mp4"
st.video(video_path)


st.error("The model is trained for just 20 EPOCHS . If it will be trained for some more epochs it will perform really good and fast " )