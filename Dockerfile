FROM python:3.11-slim-bookworm

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY main.py main.py
COPY side.py side.py
