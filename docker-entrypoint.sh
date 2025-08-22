#!/bin/bash

mkdir -p /app/log
rm -rf /app/staticfiles
pip install --upgrade pip

# Clear Django cache after build/start
python manage.py shell -c "from django.core.cache import cache; cache.clear()"

if [ "$ENVIRONMENT" = "dev" ]; then
    python manage.py migrate
    python manage.py runserver 0.0.0.0:${PORT}
else
    python manage.py migrate
    python manage.py collectstatic --noinput
    gunicorn config.wsgi:application --bind 0.0.0.0:${PORT} --workers 3
fi