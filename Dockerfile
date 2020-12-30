FROM python:3.9.1

RUN mkdir -p /usr/src/flask_app/
COPY requirements.txt /usr/src/flask_app/

WORKDIR /usr/src/flask_app/
RUN pip install -r requirements.txt

COPY . /usr/src/flask_app

EXPOSE 5000
RUN chmod +x ./entrypoint.sh
# ENTRYPOINT ["sh", "entrypoint.sh"]
CMD ["flask", "run", "--host", "0.0.0.0"]