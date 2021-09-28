FROM python:3.9.0

WORKDIR /home/

RUN echo "asdasdfasdfddfasdf"

RUN git clone https://github.com/yangsunkang/second_project.git

WORKDIR /home/second_project/


RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash","-c","python manage.py collectstatic --noinput --settings=second_project.settings.deploy && python manage.py migrate --settings=second_project.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=second_project.settings.deploy second_project.wsgi --bind 0.0.0.0:8000"]