#!/bin/bash
# for uwsgi
# uwsgi --wsgi-file action.py --callable app --processes 4 --threads 4 --http :10618
# for gunicorn
gunicorn-c gunicorn_conf.py action:app 
