# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the app
COPY . .

# Expose the port Render expects
EXPOSE 8080

# Run the app
CMD ["python", "app.py"]
