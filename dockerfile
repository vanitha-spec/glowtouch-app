FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y supervisor && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# supervisord config: run both FastAPI and Streamlit
RUN echo '[supervisord]\n\
nodaemon=true\n\
\n\
[program:fastapi]\n\
command=uvicorn main:app --host 0.0.0.0 --port 8000\n\
directory=/app\n\
autostart=true\n\
autorestart=true\n\
\n\
[program:streamlit]\n\
command=streamlit run frontend.py --server.port=8501 --server.address=0.0.0.0\n\
directory=/app\n\
autostart=true\n\
autorestart=true\n' > /etc/supervisor/conf.d/supervisord.conf

EXPOSE 8501

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]