# Use a lightweight Python image
FROM python:3.9-slim

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    xvfb \
    x11-utils \
    x11vnc \
    wget \
    ca-certificates \
    fonts-liberation \
    --no-install-recommends

# Install Chromium
RUN apt-get update && apt-get install -y chromium && \
    rm -rf /var/lib/apt/lists/*

# Install pyautogui and its dependencies
RUN pip install pyautogui pillow

# Set up environment variables
ENV DISPLAY=:99
ENV XAUTHORITY=""

# Start Xvfb and then run the command
CMD ["sh", "-c", "Xvfb :99 -screen 0 1024x768x16 & tail -f /dev/null"]
