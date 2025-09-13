FROM python:3.10

WORKDIR /app

COPY ./docker/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

COPY ../requirements.txt ./

RUN apt-get update && \
    apt-get install -y gcc libmariadb-dev && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

EXPOSE 8000

