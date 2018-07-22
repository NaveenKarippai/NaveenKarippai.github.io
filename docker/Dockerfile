FROM python:2.7-alpine
COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apk update && apk add git tmux
