FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

ARG SLACK_BOT_TOKEN

ENV SLACK_BOT_TOKEN=$SLACK_BOT_TOKEN

COPY . .