FROM python:3.11.4-slim

WORKDIR /api

COPY pyproject.toml .
COPY poetry.lock .

RUN apt-get update
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

ENV PORT 4444

COPY . .

CMD [ "python3", "run.py" ]