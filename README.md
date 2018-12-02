# Bowling Game

This project is a bowling game written in Python/Flask, Docker, and React. It was written with a very lean production environment in mind.
[![Build Status](https://travis-ci.org/testdrivenio/testdriven-app-2.3.svg?branch=master)](https://travis-ci.org/testdrivenio/testdriven-app-2.3)

## Getting Started

Clone this repo: https://github.com/sarapearce/bowling-game

Most changes will be made in the users directory.

To play the game:

`git clone git@github.com:sarapearce/bowlingGame.git`

`cd bowling-game`

`docker-compose -f docker-compose-dev.yml up -d --build`

These two commands will spin up the Docker containers and the servers within. You should be able to see the front-end at http://localhost

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

See the Dockerfile inside each of the `services` directories for a list of dependencies.

Major Prerequisites are:
Docker
Python 3.7.1
React 17.1
Nginx

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

These are basic coverage, regression tests written by the Django framework.
https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/

There are also tests in the (filename) that cover the
Score model.


```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

The environment for this project is minimal, and therefore doesn't distinguish between development and deployment environments.

## Built With

* [Python 3.7](https://docs.python.org/3/) - The scripting language
* [Django](https://docs.djangoproject.com/en/2.1/) - The web framework used
* [Tastypie](https://django-tastypie.readthedocs.io/en/latest/) - API framework for Django


## Authors

* **Sara Pearce** - *[Portfolio](http://sarapearce.net)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

https://docs.djangoproject.com/en/2.1
https://codeburst.io/create-a-django-api-in-under-20-minutes-2a082a60f6f3
