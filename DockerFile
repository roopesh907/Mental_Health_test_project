# Use a stable base image with Python 3.10
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Expose port for Render
EXPOSE 10000

# Start your app
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]
