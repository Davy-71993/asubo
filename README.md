# Asubo API

A barebones Django app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

```sh
$ git clone https://github.com/Davy-71993/asubo.git
$ cd asubo

## Create a virtual environment and activate it
$ python3 -m venv env
$ .\env\Scripts\activate

## Install the requirements
$ pip install -r requirements.txt

## Make migrations
$ python manage.py migrate
```sh
