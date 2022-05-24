FROM python as base

# disable .pyc files generation
ENV PYTHONDONTWRITEBYTECODE=1
# disable buffering for easier container logging
ENV PYTHONBUFFERED=1

WORKDIR /app

RUN apt update && \
  apt -y full-upgrade

RUN apt install -y vim

COPY ./requirements.txt /cstm/requirements.txt

RUN python3 -m pip install --no-cache-dir -r /cstm/requirements.txt

COPY ./entrypoint.sh /scripts/entrypoint.sh

ENTRYPOINT [ "/scripts/entrypoint.sh" ]

# --------------------------------

FROM base as dev

RUN mkdir /helpers
RUN python3 -m pip install debugpy -t /helpers
RUN  echo 'alias start-debugger="python3 /helpers/debugpy --listen 0.0.0.0:5678 -m uvicorn --reload --reload-dir /app/api api.main:app --host 0.0.0.0 --port 8001 --log-level debug"' >> /etc/bash.bashrc
