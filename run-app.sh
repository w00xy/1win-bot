#!/bin/bash
cd app
gunicorn --workers 3 --bind 0.0.0.0:5000 wsgi:app