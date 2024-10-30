import streamlit as st
import cv2
import os
import time
from ultralytics import YOLO

st.set_page_config(layout='wide')

model = YOLO("../models/yolov8n.pt")

options = ['airplane', 'apple', 'backpack', 'banana', 'baseball bat', 'baseball glove', 'bear', 'bed', 'bench', 'bicycle', 
           'bird', 'boat', 'book', 'bottle', 'bowl', 'broccoli', 'bus', 'cake', 'car', 'carrot', 'cat', 'cell phone', 
           'chair', 'clock', 'couch', 'cow', 'cup', 'dining table', 'dog', 'donut', 'elephant', 'fire hydrant', 'fork', 
           'frisbee', 'giraffe', 'hair drier', 'handbag', 'horse', 'hot dog', 'keyboard', 'kite', 'knife', 'laptop', 
           'microwave', 'motorcycle', 'mouse', 'orange', 'oven', 'parking meter', 'person', 'pizza', 'potted plant', 
           'refrigerator', 'remote', 'sandwich', 'scissors', 'sheep', 'sink', 'skateboard', 'skis', 'snowboard', 'spoon', 
           'sports ball', 'stop sign', 'suitcase', 'surfboard', 'teddy bear', 'tennis racket', 'tie', 'toaster', 'toilet', 
           'toothbrush', 'traffic light', 'train', 'truck', 'tv', 'umbrella', 'vase', 'wine glass', 'zebra']

# Number of columns for layout
num_columns = 8  

# Create a header
st.header("Select Classes")

# Create a reset button
if st.button('Reset Checkboxes'):
    # When reset is clicked, we set a session state flag to force rerun with all checkboxes unchecked
    for i in range(len(options)):
        st.session_state[f"checkbox_{i}"] = False

# Create an expander to hold all the checkboxes
with st.expander("Expand to select options"):
    # Create columns inside the expander
    cols = st.columns(num_columns)

    # Create a list to store selected classes
    selected_classes = []

    # Loop through options and create checkboxes in the specified layout
    for i, option in enumerate(options):
        col_index = i % num_columns  # Determine which column to use
        # Use a unique key for each checkbox
        if cols[col_index].checkbox(option, value=False, key=f"checkbox_{i}"):
            selected_classes.append(option)

# Display selected classes
st.write("You selected:", selected_classes)

# Processing YOLO model names
my_dict = model.names

# Create a list to store keys for selected classes
keys_for_values = []

# Find keys for each selected class
for key, value in my_dict.items():
    if value in selected_classes:
        keys_for_values.append(key)

# Display the corresponding keys for the selected classes
#st.write("Corresponding keys:", keys_for_values)



# Function to display video frame by frame with bounding boxes and reduced quality
def show_video_frame_with_boxes(video_path, reduction_factor=1):
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        st.error("Error: Could not open video.")
        return
    
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    current_frame = 0

    # Create a button to control playback
    play_button = st.button("Play")

    # Container for displaying the frames
    frame_placeholder = st.empty()

    while current_frame < frame_count:
        if play_button:
            ret, frame = cap.read()
            if not ret:
                st.error("Error: Could not read frame.")
                break
            
            # Convert frame from BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Reduce quality by resizing the frame
            if reduction_factor > 1:
                frame = cv2.resize(frame, 
                                   (frame.shape[1] // reduction_factor, 
                                    frame.shape[0] // reduction_factor))

            # Example of adding bounding boxes (Modify as needed)
            results = model(frame)#, classes=selected_classes)
            for x,y,w,h in results[0].boxes.xywh:
                x, y, w, h = int(x.item()), int(y.item()), int(w.item()), int(h.item())
                dummy = cv2.rectangle(frame, (int(x-w/2), int(y-h/2)), (int(x + w/2), int(y + h/2)), (255, 0, 0), 2) 

            # Display the frame in the placeholder
            frame_placeholder.image(dummy, channels='RGB')
            current_frame += 1
            time.sleep(0.03)  # Adjust delay as needed
        else:
            break

    cap.release()

# Specify the video path
video_path = '../data/video1.mp4'

# Check if the file exists
if os.path.exists(video_path):
    # Set a reduction factor (1 means original quality, 2 means half size, etc.)
    reduction_factor = st.slider("Select Quality Reduction Factor", min_value=1, max_value=10, value=1, step=1)
    
    show_video_frame_with_boxes(video_path, reduction_factor)
else:
    st.error("Error: Video file not found.")
