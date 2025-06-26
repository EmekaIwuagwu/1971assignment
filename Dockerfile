# Dockerfile
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY . .

# Expose the port (usually 5000)
EXPOSE 5000

# Run Gunicorn server on container start
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--workers", "3"]
