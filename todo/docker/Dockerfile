ARG IMAGE
FROM $IMAGE
LABEL maintainer="Denis Sventitsky <denis.sventitsky@gmail.com> / Twisted Fantasy <twisteeed.fantasy@gmail.com>"

ARG APP_PATH

ENV PYTHONUNBUFFERED 1

RUN mkdir -p $APP_PATH
WORKDIR $APP_PATH

ENV SCRIPT_PATH=$APP_PATH/todo/core/systemuser.py
COPY todo/requirements.txt .
RUN pip install -r requirements.txt
COPY todo/ .

CMD python3 manage.py collectstatic --no-input --clear && python3 manage.py migrate && python3 $SCRIPT_PATH && python3 manage.py runserver 0.0.0.0:8000
# FIXME: use uwsgi by default
