FROM python:3.8-buster

RUN apt-get update \
    && apt-get install -y wget \
    && rm -rf /var/lib/apt/list/* 

WORKDIR /
COPY . .

RUN pip install -r requirements.txt

CMD ['streamlit', 'run', 'app.py']
