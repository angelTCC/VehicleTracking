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
