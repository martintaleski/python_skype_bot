# Setup

## Set up virtual environemtn

    virtualenv {{/path/to/your/venv}}

## Activate virtual environment

    source {{/path/to/your/venv}}/bin/activate

## Install requirements

    pip install -r requirements  

## Set up .env file

Copy the `.env_sample` file to `.env` and set up the config variables

    cp .env_sample .env

## Run the script

    python event.py

## Supervisor setup configuration

You can run the script under supervisor, with the following configuration:

    [program:skypebot]
    priority=10
    directory={{/path/to/project/dir}}
    command={{/path/to/your/venv}}/bin/python {{/path/to/project/dir}}/event.py >> /tmp/skypebot.log
    user={{--system-user---}}
    autostart=true
    autorestart=true

Afterwards restart supervisor:

    sudo service surpervisor restart

# SkPy documentation

https://skpy.t.allofti.me/reference/index.html
