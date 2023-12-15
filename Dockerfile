FROM debian:sid-slim
FROM python:3.10

WORKDIR /game
COPY . /game

RUN pip install pygame
RUN apt-get update
RUN apt-get install -y alsa-utils

CMD ["python3", "main.py"]
