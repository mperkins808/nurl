FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

# PACKAGES
RUN apt-get -y update; apt-get -y install curl vim jq 


COPY *.py . 

EXPOSE 5000
EXPOSE $PORT

CMD [ "python3", "main.py"]