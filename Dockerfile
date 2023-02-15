# app/Dockerfile

FROM python:3.9-slim

WORKDIR /streamlit_playground

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip3 install -r requirements.txt

RUN export PYTHONPATH="$PYTHONPATH:/streamlit_playground/streamlit_pg"

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "strealit_pg/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
