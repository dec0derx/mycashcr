#!/bin/bash

set -o pipefail  # Fails if any piped command fails
set -o errexit   # Stops script on error

git fetch origin
sleep 2
git reset --hard origin/main
sleep 2
rm -rf staticfiles/*
sleep 3
python manage.py collectstatic --noinput
sleep 5
sudo supervisorctl restart gunicorn
sleep 5
sudo systemctl reload nginx

echo "Deployed"