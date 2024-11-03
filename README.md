# 🚗 Vehicle Tracking 🛣️

This project fine-tunes a YOLO model to detect, classify, and count vehicles as they cross a designated line. It is designed for traffic monitoring and vehicle analytics, providing real-time insights into vehicle flow.

- **Hardward**

| Computer    | GPU | CPU   | NVIDIA | MEMORY | Recall | Observation |
| ----- |---| ------- | -------- | --------- | ------ | ----|
| fc |---| ------- | -------- | --------- | ------ |

- **yolov11 for detection**

| model    |Run#| mAP50   | mAP50-95 | Presicion | Recall |*| freeze | lr0-lrf |  bacth | epoch| time(m) | %GPU | Computer | Observation |
| -------- |---| ------- | -------- | --------- | ------ |--| ----- |----- |-----| -----| ----| ---- |----|----|
| yolov11n | - |   -     |  -       | -         |  -     |*| 5 | 0.01-0.005 | 8 | 100 | --|  35% |  fc |
| yolo11s | - |   -     |  -       | -         |  -     |*|  - |- |-|-|
| yolo11m | - |   -     |  -       | -         |  -     |*| - |- |-|
| yolo11l | - |   -     |  -       | -         |  -     |*| - |- |-|
| yolo11x | - |   -     |  -       | -         |  -     |*| - |- |-|

## ✨ Features
- **🚙 Vehicle Detection**: Detects multiple types of vehicles (e.g., cars, trucks, motorcycles).
- **🔢 Vehicle Counting**: Counts vehicles as they cross a specific line in the frame.
- **📊 Classification**: Classifies vehicles into predefined categories.


## 📁 Project Structure

- **data/**: Dataset configurations and preprocessing scripts
- **models/**: YOLO model configuration and weights
- **notebooks/**: Jupyter notebooks for model training and testing
- **streamlit_app/**: App with streamlit
- **README.md**: Project overview and usage instructions


## ⚙️ Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/angelTCC/VehicleTracking.git
    ```
   
2. **Install Dependencies**:
bash
   pip install -r requirements.txt
    ```bash
    cd VehicleTracking
    python3.10 -m venv .env
    pip install -r requeriments.txt
    ```

3. **Download YOLO Weights**:
   Download pretrained weights and place them in the `models/` directory.

4. **Run the application**:
    ```bash
    cd streamlit_app
    streamlit run Home.py
    ```

## 📈 Results

The model outputs:
- Real-time vehicle detection and classification.
- Vehicle counts as they cross a designated line in the frame.


## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

---

## 📜 License
This project is licensed under the MIT License.


You can replace your-username with your actual GitHub username and adjust paths or descriptions as needed. This structure is ready to paste directly into a README.md file for a polished, professional look!
ChatGPT said:
ChatGPT





1. **Clone the repository and set the enviroment**:

2. **Run the app**

## Result


Acceptable values for these metrics depend on the use case, but here’s a general guideline for evaluating your YOLO vehicle detection model:

### 1. **mAP@50** 
   - **Acceptable range**: Typically, an mAP@50 of **60-80%** or higher is considered good for many object detection tasks. If your application demands high accuracy (like traffic monitoring or autonomous driving), aim for 75% or above.
   - **Good performance**: Above **80%** is excellent, indicating the model is detecting vehicle classes well with a reasonable overlap.

### 2. **mAP@50-95**
   - **Acceptable range**: mAP@50-95 is generally more challenging to optimize, so values above **50%** are often considered good. For high-stakes applications, **60%** or more would be preferred.
   - **Good performance**: Anything around **60-70%** and higher for mAP@50-95 is excellent. It shows the model can detect vehicles with high precision across varying overlap thresholds.

### 3. **Precision**
   - **Acceptable range**: Precision above **70%** is typically considered acceptable, meaning the model’s detections are largely accurate, with minimal false positives.
   - **Good performance**: Precision above **80-90%** indicates that the model is confidently and accurately identifying vehicles without much misclassification.

### 4. **Recall**
   - **Acceptable range**: For recall, aim for at least **70%** to ensure the model is catching most vehicles present in each image.
   - **Good performance**: Recall values above **80%** suggest that the model is identifying nearly all vehicles, even if it occasionally makes mistakes.

### Summary of Acceptable Ranges
- **mAP@50**: 60-80% (Good: 80%+)
- **mAP@50-95**: 50-60% (Good: 60-70%+)
- **Precision**: 70-80% (Good: 80-90%+)
- **Recall**: 70-80% (Good: 80%+)

These values can vary based on the dataset, model architecture, and application requirements. If your model’s metrics fall within these ranges, you’re likely on track! However, if any metric is significantly below these values, further tuning or additional training data might be needed.