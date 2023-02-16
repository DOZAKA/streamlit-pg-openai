# app/Dockerfile

FROM python:3.9-slim

ARG OPEN_AI_ORG
ARG OPEN_AI_API_KEY

WORKDIR /app

ENV PYTHONPATH=/app \
    OPEN_AI_ORG=${OPEN_AI_ORG} \
    OPEN_AI_API_KEY=${OPEN_AI_API_KEY}

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit_pg/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
