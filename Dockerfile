FROM python:3.10.13
#
ENV PYTHONPATH "${PYTHONPATH}:/code/src"
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo '$TZ' > /etc/timezone
#
WORKDIR /code
COPY requirements.txt /code
#
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt --no-cache-dir
#

COPY . /code


# build 成 hub.deri.org.cn/app/vpp_ops_base:latest
