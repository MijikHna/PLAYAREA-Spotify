FROM node:slim

WORKDIR /app

RUN apt update && \
  apt -y upgrade

RUN apt install -y vim

ENV PATH "/app/node_modules/.bin:$PATH"

COPY entrypoint.sh /scripts/entrypoint.sh

ENTRYPOINT [ "/scripts/entrypoint.sh" ]