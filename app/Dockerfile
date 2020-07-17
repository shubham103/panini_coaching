FROM python:3

RUN pip install flask

RUN pip install mariadb

WORKDIR /usr/src/app

COPY app.py .

EXPOSE 5001

ENV FLASK_APP=app

ENV FLASK_ENV=development

ENV FLASK_RUN_PORT=5001

CMD ["flask", "run", "--host", "0.0.0.0"]
