FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install pika
CMD ["python", "receive.py"]
