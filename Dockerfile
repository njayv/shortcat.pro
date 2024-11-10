FROM python:3.10-slim

RUN apt-get update && apt-get intsall -y git

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["python", "-u", "main.py"]