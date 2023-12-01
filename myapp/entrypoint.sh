#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput

# version with long timeout for pdb debug
gunicorn rhyme_for_web.wsgi:application --bind 0.0.0.0:8000 --workers 16 --timeout 300

# for deploy
# gunicorn rhyme_for_web.wsgi:application --bind 0.0.0.0:8000
