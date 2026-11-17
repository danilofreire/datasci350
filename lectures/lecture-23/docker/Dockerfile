# Start from an official Python image on Docker Hub
FROM python:3.14-slim

# Create /app inside the image and move into it
WORKDIR /app

# Copy requirements.txt from your folder to /app
# First, so editing hello.py won't reinstall
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy hello.py from your folder into /app
COPY hello.py .

# The command that runs when the container starts
CMD ["python", "hello.py"]
