@echo off
echo activating pyenv
source ../../fabres-env/scripts/activate
echo pyenv activated
echo runing django server
py manage.py runserver
