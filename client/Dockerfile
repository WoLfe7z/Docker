FROM python:3.11-slim

#Ustvari delovno mapo
WORKDIR /app

#Kopira vse datoteke v delovno mapo
COPY . .

#Zazeni odvisnosti
RUN pip install --no-cache-dir -r requirements.txt

#Odpri vrata za Flask
EXPOSE 5001

CMD ["python", "python-requests.py"]