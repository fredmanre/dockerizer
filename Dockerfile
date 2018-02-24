FROM python:3.4-slim
LABEL maintainer="fredmanre <fredmanre@gmail.com>"

ENV INSTALL_PATH /strategies
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:5000 --access-logfile - "strategies.app:create_app()" 
