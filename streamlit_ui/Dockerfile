FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y \
    build-essential gcc curl \
    && rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "login.py", "--server.port=8501", "--server.address=0.0.0.0"]
