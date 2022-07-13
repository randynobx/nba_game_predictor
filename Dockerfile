# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

WORKDIR /nba_game_predictor

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP=predictor_app

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
