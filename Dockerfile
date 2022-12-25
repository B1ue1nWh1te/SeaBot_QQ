FROM python:3.8

ENV LANG zh_CN.UTF-8

ENV LANGUAGE zh_CN.UTF-8

ENV LC_ALL zh_CN.UTF-8

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /seabot

COPY ./sources.list /etc/apt/sources.list

COPY ./requirements.txt .

RUN apt update && apt install -y libzbar0 locales locales-all fonts-noto

RUN apt-get install -y libnss3-dev libxss1 libasound2 libxrandr2 libatk1.0-0 libgtk-3-0 libgbm-dev libxshmfence1

RUN python3 -m pip config set global.index-url https://mirrors.aliyun.com/pypi/simple

RUN python3 -m pip install -r requirements.txt

RUN playwright install chromium firefox && playwright install-deps 

ENTRYPOINT ["python3", "./bot.py"]