from flask import Flask, send_file
import time
import cv2 as cv
import threading

app = Flask(__name__)

#funkcija za zajem slike
def capture_image():
    kamera = cv.VideoCapture(0)
    if not kamera.isOpened():
        print("Napaka: Kamera ni odprta!")
        return
        
    while True:
        ret, slika = kamera.read()
        if ret:
            cv.imwrite("slika.jpg", slika)
        else:
            print("napaka pri zajemanju slike.")
        time.sleep(10)
    
@app.route('/slika', methods=['GET'])
def get_image():
    try:
        return send_file("slika.jpg", mimetype='image/jpeg')
    except Exception as e:
        return f"Napaka pri posiljanju slike: {e}", 500
    
if __name__ == '__main__':
    #Uporaba niti za zajem slike v ozadju
    threading.Thread(target=capture_image, daemon=True).start()
    
    app.run(host='0.0.0.0', port=5000)
