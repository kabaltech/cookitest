web: gunicorn config.wsgi:application
worker: celery worker --app=letsbook.taskapp --loglevel=info
