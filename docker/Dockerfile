FROM python:3.11
RUN apt-get update && apt-get upgrade
RUN ln -sf /usr/share/zoneinfo/Europe/Madrid /etc/localtime

COPY ../src/ /app
WORKDIR app

RUN pip install Flask Flask-Login Flask-SQLAlchemy mysql-connector-python

EXPOSE 80
CMD ["bash", "-c", "app:app --host 0.0.0.0 --port 80"]