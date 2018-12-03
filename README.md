# Bowling Game

This project is a bowling game written in Python/Flask, Docker, and React. It was written with a lean production environment in mind.
<br>
[![Build Status](https://travis-ci.org/testdrivenio/testdriven-app-2.3.svg?branch=master)](https://travis-ci.org/testdrivenio/testdriven-app-2.3)

## Getting Started

Clone this repo: https://github.com/sarapearce/bowling-game

Most changes will be made in the users directory.

To play the game:

`git clone git@github.com:sarapearce/bowlingGame.git`

`cd bowling-game`

`docker-compose -f docker-compose-dev.yml up -d --build`

These commands will spin up the Docker containers and the servers within. You should be able to see the front-end at http://localhost

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


Set 1 environment variable:
```
export REACT_APP_USERS_SERVICE_URL=http://localhost/users
```

## Running the tests

`docker exec -it bowlinggame_user_1 bash`

`cd /usr/src/app/project/tests`

`pytest`

You will then see the output in terminal for those tests

## Deployment

Run the command below in the root directory, and a Production secure Docker container set will spin up

`docker-compose -f docker-compose-prod.yml up -d --build`

## Built With

* [Docker](https://docs.docker.com/)

* [Python 3.7](https://docs.python.org/3/)
* [Flask](http://flask.pocoo.org/)
* [Postgres](https://www.postgresql.org/docs/)
* [Pytest](https://docs.pytest.org/en/latest/contents.html)

* [React](https://reactjs.org/)
* [Jest] (https://jestjs.io/)

## Authors

* **Sara Pearce** - *[Portfolio](http://sarapearce.net)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
