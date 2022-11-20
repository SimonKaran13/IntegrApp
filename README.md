# IntegrApp
Execute the following commands from the IntegrApp root directory

First set up a virtual environment
```sh
python3 -m venv venv
. venv/bin/activate
```

Install requirements
```sh
pip3 install -r server/requirements.txt
```

Add root module to Python path
```sh
export PYTHONPATH=$PYTHONPATH:.server/src
```

To run the DB:
```sh
flask --app server/src/ init-db
```

To run the server:
```sh
flask --app server/src --debug run 
```
