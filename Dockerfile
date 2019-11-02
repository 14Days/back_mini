# 基础镜像
FROM python:3.7

WORKDIR /app

ADD . /app

RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD ["gunicorn", "main:app", "-c", "gunicorn.conf.py"]