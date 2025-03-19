# Computer Vision for Smart Interaction

## 📌 Overview
This project implements **real-time object detection** using **YOLOv8m** and **OpenCV**, integrated with a Flask web application.  
Users can detect multiple objects in a live webcam feed and view results through a web-based interface.

## 🎯 Features
- **Real-time Object Detection**: Detects multiple objects using a webcam.
- **Flask Web Interface**: View detections through a web-based dashboard.
- **Optimized for Speed & Accuracy**: Uses **YOLOv8m** for the best balance.
- **Multi-threaded Processing**: Ensures smooth and efficient video streaming.

---

## 🚀 **Setup & Installation**
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/kritika038/Computer-Vision-Smart-Interaction.git
cd Computer-Vision-Smart-Interaction
```

### 2️⃣ Install Dependencies
Ensure you have Python **3.8 or later** installed. Then, run:
```bash
pip install -r requirements.txt
```

### 3️⃣ **Download the YOLOv8m Model**
Since model files are large, they are **not included** in this repository.  
You must download the model manually by running this script:
```python
from ultralytics import YOLO
YOLO('yolov8m.pt')  # This will automatically download the model
```
OR **manually download** `yolov8m.pt` from:  
👉 [YOLOv8 Model Weights](https://github.com/ultralytics/assets/releases)  

After downloading, place the file inside the project folder.

✅ **This ensures anyone who clones your repository knows how to get the model.**

---

## 🔥 **(Optional) Create `download_model.py` for Easy Model Download**
If you want an **automated way to download the model**, create a new Python script named **`download_model.py`** inside your project folder and **paste this code**:
```python
from ultralytics import YOLO

# Download the YOLOv8m model
print("Downloading YOLOv8m model...")
YOLO('yolov8m.pt')
print("Download complete! Model saved in default directory.")
```
### **How to Use It**
Now, after installing dependencies, users can simply run:
```bash
python download_model.py
```
✅ **This automatically downloads the model for them.**

---

## 🎬 **How to Run the Project**
Once all dependencies and the YOLO model are ready, run:
```bash
python flask_test.py
```
Then, open **http://127.0.0.1:5000** in your browser.

---

## 📊 **Performance Analysis**
- **FPS (Speed):** ~25-30 FPS (real-time processing)
- **Accuracy:** Confidence threshold set at 70%
- **Inference Time:** ~200ms per frame
- **Latency Reduction:** Uses multi-threading to optimize speed.

---

## 📂 **Project Structure**
```
📂 Computer-Vision-Smart-Interaction/
│── flask_test.py        # Main Flask application
│── yolo_model.py        # YOLO model processing
│── templates/
│   └── index.html       # Web UI for viewing detections
│── static/
│   └── style.css        # Styling for web interface
│── requirements.txt     # Dependencies list
│── README.md            # Documentation & setup guide
│── Project_Report.pdf   # Final project report
```

---

## 📌 **Future Enhancements**
- **Train YOLO on a custom dataset** (e.g., detecting specific objects like chargers, remote controllers).
- **Deploy as a cloud-based API** for mobile/web integration.
- **Optimize inference speed using TensorRT or OpenVINO**.

---

## 📩 **Contact**
📌 **For any queries, feel free to reach out!**  
📧 Email: kritikabansal386@gmail.com 
🔗 GitHub: https://github.com/kritika038/Computer-Vision-Smart-Interaction