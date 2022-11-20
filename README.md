# IntegrApp
Execute the following commands from the IntegrApp root directory

First set up a virtual environment
> $ python3 -m venv venv
> $ . venv/bin/activate

Install requirements
> $ pip3 install -r server/requirements.txt

To run the DB:
> $ flask --app server/src/ init-db

To run the server:
> $ flask --app server/src --debug run 
