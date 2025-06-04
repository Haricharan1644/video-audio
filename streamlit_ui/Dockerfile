FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install streamlit requests
EXPOSE 8501
CMD ["streamlit", "run", "login.py", "--server.port=8501", "--server.address=0.0.0.0"]