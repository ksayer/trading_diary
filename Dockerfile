FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV APP_HOME=/opt

ARG DEBUG=${DEBUG}

WORKDIR $APP_HOME

RUN apk update \
    && apk add freetype-dev gcc python3-dev musl-dev libffi-dev

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY . .

RUN sh -c "if [ -n $DEBUG ] && [ $DEBUG == True ] ; then poetry install --no-root ;  \
    else poetry install --no-root --only main ; fi"

ENTRYPOINT ["chmod", "+x", "/opt/scripts/entrypoint.sh"]