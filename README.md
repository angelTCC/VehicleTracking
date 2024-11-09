# 🚗 Vehicle Tracking 🛣️

This project leverages a fine-tuned YOLO model for vehicle detection and tracking, enabling 
automated counting of various vehicle types as they cross a designated line using a single camera or 
video feed. By replacing manual tracking methods with advanced computer vision techniques, the system 
provides accurate real-time data on traffic flow, which can be used to inform transportation control 
decisions. This automation enhances efficiency, improves data accuracy, and supports smarter transportation management.

![image](Isolated.png "Title")


## ✨ Features
- **🚙 Vehicle Detection**: Detects multiple types of vehicles (e.g., cars, trucks, motorcycles).
- **🔢 Vehicle Counting**: Counts vehicles as they cross a specific line in the frame.
- **📊 Classification**: Classifies vehicles into predefined categories.

### Metrics


| Metric       | Definition                                          | Acceptable Range       | Good Performance                  |
|--------------|-----------------------------------------------------|------------------------|-----------------------------------|
| **mAP@50**   | Mean Average Precision at 50% IoU (Intersection over Union); measures detection accuracy with 50% overlap | 60-80% or higher       | Above 80%                         |
| **mAP@50-95**| Mean Average Precision across IoU thresholds from 50% to 95%; assesses accuracy at various overlap levels | Above 50%              | 60-70% or higher                  |
| **Precision**| Ratio of true positives to total positive predictions; indicates accuracy of detections | Above 70%              | 80-90%                            |
| **Recall**   | Ratio of true positives to total actual positives; measures detection coverage | At least 70%           | Above 80%                         |

### Hardward

| Computer    | GPU              | CPU                                                    | NVIDIA                 | MEMORY  | Observation |
| ----- |---| ------- | -------- | ---------  | ----|
| fc | Dedicada 4GB, compartida 16GB| AND Ryzen Thraddripper 3960X 24-core (48 CPUs), 3.8GHz | NVIDIA Quadro P1000   | 32GB |             |



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

Data:
- Dataset 1: 0.2 terst 0.2 val 3965train 897test 793val stratief
- Dataset 2:                                           random

### Summary of Acceptable Ranges
- **mAP@50**: 60-80% (Good: 80%+)
- **mAP@50-95**: 50-60% (Good: 60-70%+)
- **Precision**: 70-80% (Good: 80-90%+)
- **Recall**: 70-80% (Good: 80%+)

| model    |name#             | mAP50   | mAP50-95 | Presicion | Recall | freeze | lr0-lrf    |  bacth | epoch | time      | %GPU | Computer | Data      |
| -------- |--------------    | ------- | -------- | --------- | ------ | -----  |-----       |-----   | ----- | ----         | ---- |----      |----       |
| yolov11n | yolov11_runs7    |   -     |  -       | -         |  -     | 5      | 0.01-0.005 | 8      | 100   | 4.506 hours  |  35% |  fc      | dataset1 |
| yolov11n | yolov11_runs12   |   -     |  -       | -         |  -     | 20     | 0.01-0.005 | 16     | 200   | -            |  20% |  fc      | dataset1 |
| yolov11m | yolov11_runs13   |   -     |  -       | -         |  -     | 20     | 0.01-0.005 | 16     | 300   | 2 dias       |  25% |  fc      | dataset1 |
| yolov8m  | yolov8_runs4     |   -     |  -       | -         |  -     | 20     | 0.01-0.005 | 16     | 300   | 1.14 dias    |  20% |  fc      | dataset1 |
| model  | - |   -          |  -      | -         |  -     | - |- |-|


## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

---

## 📜 License
This project is licensed under the MIT License.


You can replace your-username with your actual GitHub username and adjust paths or descriptions as needed. This structure is ready to paste directly into a README.md file for a polished, professional look!
ChatGPT said:
ChatGPT
