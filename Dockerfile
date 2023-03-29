FROM python:3.9-slim-bullseye

WORKDIR /seabot

COPY ./requirements.txt .

RUN python3 -m pip config set global.index-url https://mirrors.aliyun.com/pypi/simple

RUN python3 -m pip install -r requirements.txt

ENTRYPOINT ["nb", "run"]
