#!/usr/bin/env bash
echo "Building the project..."
python -m pip install --upgrade pip
pip install -r requirements.txt

echo "Make migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collect static..."
python manage.py collectstatic --noinput --clear 