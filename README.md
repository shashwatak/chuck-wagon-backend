# chuck-wagon-backend

## Design Goals

This app will serve Food Truck information (as JSON) on REST Endpoints. All the Food Truck data is, obtained from [Data SF](https://data.sfgov.org/Economy-and-Community/Mobile-Food-Facility-Permit/rqzj-sfat?)

For the purpose of learning, I chose to re-host and serve all the data from Data SF myself.
In other words, I copy all the data from Data SF and load it into my own DB. Then I serve the data on the below REST endpoints, without making calls to Data SF.

Thus, I have properly implemented a stand-alone REST backend.

## REST Endpoints

    GET '/trucks'
Returns full list of Food Trucks as JSON

    GET '/trucks/near/<lat>/<long>'
Returns list of Food Trucks around 1 sq mile from specified lat-long, as JSON

JSON responses are in the form of:
`json
    [
        {
            "name" : "Truck Name A",
            "latitude"  : "0.0",
            "longitude"  : "0.0",
        },
        {
            "name" : "Truck Name B",
            "latitude"  : "1.0",
            "longitude"  : "1.0",
        },
        ...
    ]
`

## Design Overview
Going into the project, my biggest concern was hosting and actually serving the data. I chose Heroku for hosting, because it is very simple to set up and the documentation is solid. This was the main driver of many of my subsequent framework/library decisions: does it pair well with Heroku.

Django (with Postgres) provides the backend, exposing the trucks through rendered JSON. Apps can GET from the endpoints and receive the locations and names of trucks. I chose Django because I have some familiarity with Python, and the Heroku sample app was quite helpful. Django also provides Testing out of the box, so there is no need to integrate a seperate testing framework.


## Files of interest

`chuck-wagon-backend/__init__.py` Copies data from Data SF, and converts it into our Model, and persists it in our DB, when the backend is first launched. Checks and ignores duplicate and ill-formed data.

`chuck-wagon-backend/urls.py` Handles the URL routing, as well as argument passing, that the clients will use to get our data. Essentially codifies the REST Endpoints themselves. Clients access URLs, and this file dictates which View they will get.

`trucks/models.py` Defines the data model, a singular Truck class, and all its fields.

`trucks/views.py` Views are usuall used with Templates to generate HTML responses, but we generate pure JSON for our Clients.

`trucks/templates/trucks.html` The JSON Schema we will return to the Client, will be filled in with data when a Client requests it.


## 'Getting Started with Python on Heroku'

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

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
