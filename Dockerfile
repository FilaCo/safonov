FROM python:3.13-slim as builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get upgrade && \
    apt-get install -y --no-install-recommends gcc

COPY requirements.txt .

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

FROM python:3.13-slim as final

WORKDIR /app

COPY --from=builder /app/wheels ./wheels
COPY --from=builder /app/requirements.txt .

RUN pip install --no-cache ./wheels/*