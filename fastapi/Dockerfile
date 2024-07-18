FROM python AS base

WORKDIR /app

RUN apt update && \
    apt -y full-upgrade

COPY ./requirements.txt /cstm/requirements.txt

RUN python3 -m pip install --no-cache-dir -r /cstm/requirements.txt

COPY ./entrypoint.sh /scripts/entrypoint.sh

ENTRYPOINT [ "/scripts/entrypoint.sh" ]

CMD "fastapi run"

# --------------------------------

FROM base AS dev

# disable .pyc files generation
ENV PYTHONDONTWRITEBYTECODE=1
# disable buffering for easier container logging
ENV PYTHONBUFFERED=1
# disable frozen modules
ENV PYDEVD_DISABLE_FILE_VALIDATION=1
