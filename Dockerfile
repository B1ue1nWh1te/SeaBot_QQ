FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /seabot_qq

COPY ./requirements.txt .

RUN python3 -m pip config set global.index-url https://mirrors.aliyun.com/pypi/simple

RUN python3 -m pip install -r requirements.txt

ENTRYPOINT ["python3", "./bot.py"]