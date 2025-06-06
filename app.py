from flask import Flask, request, jsonify
from ultralytics import YOLO
import os
import gdown
import cv2
import numpy as np


app = Flask(__name__)

MODEL_PATH = "best.pt"
FILE_ID = "1nYH6pXaatkiX8mcYIE6SQOIVryd6sEeV" 

if not os.path.exists(MODEL_PATH):
    print("Downloading model...")
    gdown.download(f"https://drive.google.com/uc?id={FILE_ID}", MODEL_PATH, quiet=False)

model = YOLO("best.pt")

@app.route('/count', methods=['POST'])
def count_people():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400

    # Read image from file into OpenCV format
    file_bytes = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    results = model(img)
    result = results[0]

    person_class = 0
    count = sum(1 for cls in result.boxes.cls if int(cls) == person_class)

    return jsonify({'person_count': count})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
