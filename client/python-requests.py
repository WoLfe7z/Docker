import requests
from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def get_image():
    while True:
        try:
            response = requests.get('http://server:5000/slika')
            if response.status_code == 200:
                with open("static/slika.jpg", "wb") as f:
                    f.write(response.content)   #Shrani sliko
        except requests.exceptions.RequestException as e:
            print(f"Napaka pri pridobicanju slike: {e}")
        time.sleep(10)

if __name__ == '__main__':
    from threading import Thread
    thread = Thread(target=get_image)
    thread.daemon = True
    thread.start()
    
    #Zazeni Flask
    app.run(host='0.0.0.0', port=5001)