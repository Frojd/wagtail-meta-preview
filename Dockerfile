FROM python:3.14

WORKDIR /srv

ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    PYTHONDONTWRITEBYTECODE=1 \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    PYTHONPATH=/srv/ \
    DJANGO_SETTINGS_MODULE=settings_dev

RUN apt-get update \
        && apt-get install -y netcat-traditional \
        gettext libpq-dev build-essential \
        --no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN useradd --create-home --uid 1000 app \
        && mkdir /srv/media \
        && chown app:app /srv /srv/media

COPY --chown=app:app . /srv/

RUN pip install psycopg2-binary~=2.9.0  -e .[testing]

USER app

ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["runserver"]
