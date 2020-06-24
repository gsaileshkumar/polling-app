FROM python:3.7-slim-buster

COPY requirements.txt /

COPY src /etc/polling-app/src/
COPY setup.py /etc/polling-app

# Install dependencies
RUN pip install -r /requirements.txt

RUN pip install -e /etc/polling-app

WORKDIR /etc/polling-app/src

ENV PYTHONPATH "/etc/polling-app/src"
ENV FLASK_APP=main.py
ENV FLASK_ENV=development