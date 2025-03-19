from ultralytics import YOLO
import cv2

# Load the YOLO model once
model = YOLO('yolov8n.pt')  # Using the fastest YOLO model

def detect_objects(frame):
    """Runs YOLO on a resized frame for speed improvement and returns the annotated frame."""
    frame = cv2.resize(frame, (480, 360))  # Resize for better speed
    results = model(frame, conf=0.6, iou=0.5)  # Increase confidence for better accuracy
    return results[0].plot()  # Return annotated frame

# ✅ Prevents the script from running when imported in Flask
if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break

        annotated_frame = detect_objects(frame)
        cv2.imshow("YOLO Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
