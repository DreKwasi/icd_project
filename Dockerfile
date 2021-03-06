FROM python:3.9-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /icd
COPY requirements.txt requirements.txt
COPY . .
RUN pip3 install -r requirements.txt
