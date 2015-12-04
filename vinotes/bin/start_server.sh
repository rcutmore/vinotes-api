#!/usr/bin/env bash
project_dir=/home/rc/projects/vinotes-api
gunicorn_location=$project_dir/env/bin/gunicorn
gunicorn_config=$project_dir/vinotes/config/gunicorn.py
$gunicorn_location \
    --config=$gunicorn_config \
    vinotes.wsgi
