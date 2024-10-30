import streamlit as st
import cv2
from ultralytics import YOLO
import os
import time

st.set_page_config(layout='wide')

options = [
    '1_Auto Privado', 
    '13_Bus',
    '11_Camioneta rural',
    '12_Microbus', 
    '4_Mototaxi', 
    '5_Moto lineal', 
    '9_Omnibus Interprovincial',
    '10_Auto colectivo', 
    '14_Articulado', 
    '2_Cam. PickUp', 
    '3_Taxi',
    '6_Bicicletas',
    '7_Scooter',
    '8_TransportenEscolar Personal',
    '15_TC_Ligeros',
    '16_TC Pesados',
    '17_TC SemiTrailler Trailer',
    '18_Triciclo',
    '19_Ambulancia',
]

st.header("Split Train-Test dataset")
st.image("../data/train_test.png")

st.header("Select Classes")

cols = st.columns(4)

# Display selected options
st.write("Selected options:")

selected_classes = []

checkbox_states = {}
for i,option in enumerate(options):
    col_index = i % 4
    checkbox_states[option] = cols[col_index].checkbox(option, value=True, key=option)

# me falta actualizar las clases selceccionadas


st.write(checkbox_states.keys())

# CUSTOM THE LINES #####################################################
st.header('Custom the lines')



# TEST MODEL COUNT ######################################################33333333
st.header('Test model count')
# select the model
model = YOLO('../models/best.pt')

# select the video
video_path = '../data/video1.mp4'


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
            results = model(frame)
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


# Check if the file exists
if os.path.exists(video_path):
    # Set a reduction factor (1 means original quality, 2 means half size, etc.)
    reduction_factor = st.slider("Select Quality Reduction Factor", min_value=1, max_value=10, value=1, step=1)

    show_video_frame_with_boxes(video_path, reduction_factor)
else:
    st.error("Error: Video file not found.")

