from ultralytics import YOLO

# Download the YOLOv8m model
print("Downloading YOLOv8m model...")
YOLO('yolov8m.pt')
print("Download complete! Model saved in default directory.")
