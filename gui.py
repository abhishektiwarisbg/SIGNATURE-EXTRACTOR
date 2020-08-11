from flask import *
from main import main_func
import cv2
import matplotlib as plt
import numpy as np
import pickle

app = Flask(__name__)


@app.route('/')
def message():
    return render_template('welcome.html')

@app.route('/upload', methods = ['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save("input.jpg")
        b=main_func()
        filename = 'output.jpg'
        return send_file(open(filename, 'rb'),mimetype="image/jpg")


@app.route('/upload2', methods = ['POST'])
def success2():
    if request.method == 'POST':
        f = request.files['file']
        f.save("input.jpg")
        b=main_func()
        img=cv2.imread("output.jpg")
        small = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, bw = cv2.threshold(small, 0.0, 255.0, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 1))
        connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)
        contours, hierarchy = cv2.findContours(connected.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        l1=list([])
        for idx in range(len(contours)):
            x, y, w, h = cv2.boundingRect(contours[idx])
            l1.extend([((x + w - 1, y + h - 1))])
            # else:
            #     print(type(l1))
            cv2.rectangle(img, (x, y), (x + w - 1, y + h - 1), (0, 255, 0), 2)

        response = jsonify(str(l1))
        response.status_code=200
        return response

if __name__ == '__main__':
    app.run(debug=True)