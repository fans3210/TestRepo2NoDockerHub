FROM python:3.7.1
WORKDIR /app

ENV PYTHONUNBUFFERED=0
ENV PYTHONIOENCODING=UTF-8

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN chmod +x ./scripts/*.sh
