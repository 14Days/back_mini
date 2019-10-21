FROM python:3.7

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD ["gunicorn", "main:init_app", "-c", "gunicorn.conf.py"]