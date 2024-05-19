FROM python:3.12.2-slim

ENV PYTHONUNBUFFERED=1 \
	PYTHONDONTWRITEBYTCODE=1 \
	PIP_NO_CACHE_DIR=off \
	PIP_DEFAULT_TIMEOUT=100 \
	POETRY_VERSION=1.8.2\
	POETRY_HOME="/opt/poetry" \
	POETRY_VIRTUALENVS_CREATE=false

ENV	PATH="$PATH:$POETRY_HOME/bin"

RUN pip install -U pip
RUN apt update && apt upgrade -y && apt install --no-install-recommends -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /home
COPY . /home

RUN groupadd app && useradd -g app app
RUN chown -R app:app /home

RUN poetry install --no-root

USER app

WORKDIR /home/api
CMD ["fastapi", "run", "main.py", "--host", "0.0.0.0","--port", "8000"]

