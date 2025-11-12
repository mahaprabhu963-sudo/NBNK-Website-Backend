# Use official Python 3.11 slim image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Copy only requirements first for faster builds
COPY Backend/requirements.txt /app/requirements.txt

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install Python dependencies
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

# Copy the rest of the project
COPY . /app

# Expose the port that Railway will map
EXPOSE 8080

# Start the Django server using Railway's PORT
CMD ["python3", "Backend/manage.py", "runserver", "0.0.0.0:8080"]
