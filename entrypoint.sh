#!/bin/sh

echo "Applying database migrations..."
python manage.py migrate

echo "Loading initial data..."
python manage.py loaddata users/fixtures/user_data.json
python manage.py loaddata event/fixtures/seed_data.json


# Start the Django development server
echo "Starting server..."
exec "$@"
