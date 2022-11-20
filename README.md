# Crypto Tracker

Track crypto currency price

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Project Overview

This project is developed on the boilerplate provided by cookiecutter django template app.
Main application (crypto_tracker directory) of this project is
 - To fetch different crypto currency prices in USD (using endpoint https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md#symbol-price-ticker) every minute and store it.
 - To provide RESTful APIs to access the stored data.
    - Get list of actively monitored currencies (/api/currencies/)
    - Get prices in paginated format for a given date in DD-MM-YYYY format (/api/price_history?date=20-11-2022)
    [Below are yet to included]
    - Get current price for all crypto currencies monitored
    - Get min, max price ranges for the day or any given date in DD-MM-YYYY
    - API to input "Price Range", "Email Address", and "Currency Name" from users
 [Below features are yet to included]
 - Send email alerts to registered users when currency price moves out of range.

### How to run this application locally
 - Make sure to install, docker, docker-compose
 - Clone this repository and build images using  `docker-compose -f local.yml build`
 - Run application using `docker-compose -f local.yml up -d`
 - Apply migrations using `docker-compose -f local.yml exec django ./manage.py migrate`
 - Setup cronjobs using `docker-compose -f local.yml exec django ./manage.py setup`
 - Add crontab entry so that job runs automatically at scheduled time using `docker-compose -f local.yml exec django ./manage.py crontab add` (Refer https://pypi.org/project/django-crontab/)

### Known Issues:
 - nginx reverse proxy setup not complete
 - django-crontab setup not complete

### Future Improvements:
 - Infra level
    - Scalability using microservices
    - CI/CD pipeline
 - App level
    - Authentication mechanism
    - Exception Handling
    - Logging
    - Rate limit handling for the currency api used to pull data and store
    - Coding standard checks/corrections
    - Unit Tests
    - API Documentation

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy crypto_tracker

### Test coverage [Yet to be implemented]

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment [Yet to be refined]

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
