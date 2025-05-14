#!/bin/bash
gunicorn --bind 0.0.0.0:9999     --workers ${GUNICORN_WORKERS:-2}     --timeout ${GUNICORN_TIMEOUT:-300}     --worker-class sync     --keep-alive 80     app:app
