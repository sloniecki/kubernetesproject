FROM python:3.11-slim-bullseye

RUN apt-get update
RUN apt-get install -y pkg-config
RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential
RUN pip install --upgrade pip


WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --requirement /app/requirements.txt
COPY . /app

EXPOSE 5000

CMD ["python3","service.py"]