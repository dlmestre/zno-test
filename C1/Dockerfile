FROM python:3.6

ENV URL https://api.localytics.com/v1/exports/analytics/logs/

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY app /app
COPY config /config

WORKDIR /app

ENTRYPOINT ["python","app.py"]
