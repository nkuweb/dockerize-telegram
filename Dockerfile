FROM python:latest
COPY /web /web
WORKDIR /web
RUN apt-get update -y
RUN apt-get install -y python3-setuptools
RUN pip3 install -r req-web.txt

