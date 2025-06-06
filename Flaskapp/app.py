from flask import Flask, request, jsonify
from ultralytics import YOLO
import cv2
import numpy as np


app = Flask(__name__)


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
    app.run(host='0.0.0.0', port=5000)
