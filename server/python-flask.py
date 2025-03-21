from flask import Flask, send_file
import time
import cv2 as cv
import threading

app = Flask(__name__)

#funkcija za zajem slike
def capture_image():
    kamera = cv.VideoCapture(0)
    while True:
        ret, slika = kamera.read()
        if ret:
            cv.imwrite("slika.jpg", slika)
        time.sleep(10)
    
@app.route('/image', methods=['GET'])
def get_image():
    return send_file("slika.jpg", mimetype='image/jpeg')
    
if __name__ == '__main__':
    #Uporaba niti za zajem slike v ozadju
    threading.Thread(target=capture_image, daemon=True).start()
    
    app.run(host='0.0.0.0', port=5000)