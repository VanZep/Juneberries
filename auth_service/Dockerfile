FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install poetry==2.1.3 --no-cache-dir

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock .

RUN poetry install

COPY app .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]