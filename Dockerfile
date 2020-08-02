FROM python:3.7-slim

WORKDIR /app

COPY requirements .
RUN pip install -r requirements

COPY . .

ENTRYPOINT [ "sh", "entrypoint.sh" ]