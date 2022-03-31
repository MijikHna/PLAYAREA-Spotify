FROM postgres

RUN apt update && \
  apt dist-upgrade -y

RUN apt install -y vim

RUN apt autoremove -y

ENV POSTGRES_PASSWORD=password

RUN echo "en_US.UTF-8 UTF-8" | tee -a /etc/locale.gen && \
  locale-gen

# USER postgres

COPY ./initDB.sql /docker-entrypoint-initdb.d/initDB.sql