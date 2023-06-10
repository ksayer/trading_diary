python src/manage.py migrate --no-input &
python src/manage.py collectstatic --no-input &

gunicorn --bind 0.0.0.0:8000 --chdir /opt/src settings.wsgi:application --workers 2 --timeout 300
