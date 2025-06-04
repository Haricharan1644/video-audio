FROM python:3.9

WORKDIR /app
COPY . .
COPY app.py .

# Install ffmpeg and system packages
RUN apt-get update && apt-get install -y ffmpeg

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install flask moviepy==1.0.3 imageio imageio-ffmpeg numpy

EXPOSE 5002
CMD ["python", "app.py"]
