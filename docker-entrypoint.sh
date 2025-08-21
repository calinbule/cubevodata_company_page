#!/bin/bash

# Clear Django cache after build/start
python manage.py shell -c "from django.core.cache import cache; cache.clear()"

if [ "$ENVIRONMENT" = "dev" ]; then
    python manage.py migrate
    python manage.py runserver 0.0.0.0:8000
else
    python manage.py migrate
    python manage.py collectstatic --noinput
    gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3
fi