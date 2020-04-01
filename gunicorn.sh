#!/bin/bash

NAME="covid_gandaki"                              #Name of the application (*)
DJANGODIR=/home/covid/deploy/covid_gandaki             # Django project directory (*)
SOCKFILE=/home/covid/deploy/run/gunicorn.sock        # we will communicate using this unix socket (*)
USER=covid                                        # the user to run as (*)
GROUP=covid                                     # the group to run as (*)
NUM_WORKERS=1                                     # how many worker processes should Gunicorn spawn (*)
DJANGO_SETTINGS_MODULE=covid_gandaki.settings             # which settings file should Django use (*)
DJANGO_WSGI_MODULE=covid_gandaki.wsgi                     # WSGI module name (*)
VENV_DIR=/home/covid/deployment_venv                      #VirtualEnv directory

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /home/covid/deployment_venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /home/covid/deployment_venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --bind=unix:$SOCKFILE