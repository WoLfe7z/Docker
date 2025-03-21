FROM python:3.11-slim

#Ustvari delovno mapo
WORKDIR /app

#Kopira vse datoteke v delovno mapo
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "python-flask.py"]