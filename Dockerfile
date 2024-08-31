# Use a specific version of Python as the base image
FROM python:3.9-slim-buster

# Install system dependencies and Chrome as root
RUN apt-get update && apt-get install -y \
    wget \
    gnupg2 \
    ca-certificates \
    && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb || apt-get -fy install \
    && rm google-chrome-stable_current_amd64.deb

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the application code into the container
COPY . /app/

# Set up ChromeDriver using webdriver-manager
RUN pip install webdriver-manager

# Create a non-root user and switch to it
RUN useradd -m myuser
USER myuser

# Set the working directory
WORKDIR /app

# Expose port 5000
EXPOSE 5000

# Command to run the application
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "5000", "--workers", "4"]
