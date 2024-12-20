#!/bin/bash
echo "Waiting for postgres to be ready..."
./wait-for-it.sh postgres:5432 --timeout=10 --strict -- echo "PostgreSQL is ready!"

echo "Running migrations..."
alembic upgrade head
if [ $? -eq 0 ]; then
  echo "Migrations applied successfully."
else
  echo "Migrations failed."
  exit 1
fi

if [ "$1" == "cli" ]; then
    echo "Starting CLI..."
    python app.py
else
    echo "Starting the application..."
    python app.py
fi