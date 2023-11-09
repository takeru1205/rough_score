ARG PYTHON_VERSION='3.11'
FROM python:${PYTHON_VERSION}

ENV PYTHONUNBUFFERED=1

WORKDIR /workspace

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "./src/main.py"]
