FROM python:latest
COPY /web /web
WORKDIR /web

RUN pip3 install -r req-web.txt
