FROM python:latest
RUN apt-get update && apt-get upgrade
RUN ln -sf /usr/share/zoneinfo/Europe/Madrid /etc/localtime

COPY ../src/ /app
WORKDIR app

RUN pip install Flask Flask-Login Flask-SQLAlchemy mysql-connector-python gunicorn  

EXPOSE 80

# Especifica el comando para ejecutar la aplicación con Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:80", "main:app"]
#CMD ["bash", "-c", "app:app --host 0.0.0.0 --port 80"]