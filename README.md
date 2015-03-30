# chuck-wagon-backend

## Initialized with Heroku's python-getting-started/

Provide REST endpoints to get chuck wagon data, obtained from [Data SF](https://data.sfgov.org/Economy-and-Community/Mobile-Food-Facility-Permit/rqzj-sfat?)

## REST Endpoints

    GET '/trucks'
Returns full list of Food Trucks as JSON

    GET '/trucks/near/<lat>/<long>'
Returns list of Food Trucks around 1 sq mile from specified lat-long, as JSON


## Design Overview
Django provides the backend, exposing the trucks through rendered JSON.


This application support the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/).

```sh
$ git clone git@github.com:heroku/chuck-wagon-backend.git
$ cd chuck-wagon-backend
$ pip install -r requirements.txt
$ python manage.py syncdb
$ foreman start web
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master
$ heroku run python manage.py syncdb
$ heroku open
```

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
