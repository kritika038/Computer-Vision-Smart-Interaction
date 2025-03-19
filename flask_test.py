from flask import Flask, render_template, Response
import cv2
import threading
from yolo_model import detect_objects

app = Flask(__name__)

camera = None  # Camera should be initialized only when needed

latest_frame = None
lock = threading.Lock()

def capture_frames():
    """Capture frames only when video is accessed."""
    global camera, latest_frame
    camera = cv2.VideoCapture(0)  # Initialize camera only when function runs
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    camera.set(cv2.CAP_PROP_FPS, 30)

    while True:
        success, frame = camera.read()
        if not success:
            continue
        with lock:
            latest_frame = detect_objects(frame)  # Process frame asynchronously

def generate_frames():
    """Stream processed frames to the Flask web app."""
    global camera
    if camera is None:
        threading.Thread(target=capture_frames, daemon=True).start()  # Start camera when video is accessed

    while True:
        with lock:
            if latest_frame is not None:
                ret, buffer = cv2.imencode('.jpg', latest_frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
                frame = buffer.tobytes()

                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    print("Flask YOLO App Running at http://127.0.0.1:5000")
    app.run(debug=True, threaded=True)
