# Start from an official Python image
FROM python:3.14-slim

# Everything below happens inside /app
WORKDIR /app

# Copy requirements first, so Docker can
# cache the install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script
COPY hello.py .

# What runs when the container starts
CMD ["python", "hello.py"]
