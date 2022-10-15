#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

# migrate
python manage.py migrate

echo "Populating city, region, subregion, country data..."
# python manage.py cities_light

echo "Seeding artist, song, album, record label data, etc..."
python manage.py seed_data

# collect static files
python manage.py collectstatic --no-input

# run app
uvicorn stg_djangocon.asgi:application --host 0.0.0.0 --reload --reload-include '*.py,*.html,*.css'
