FROM python:3.10-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .
RUN chmod +x ./docker-entrypoint.sh \
    && python -m pip install --upgrade pip \
    && pip install -r requirements.txt
ENTRYPOINT ["./docker-entrypoint.sh"]