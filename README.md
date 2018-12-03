# Bowling Game

This project is a bowling game written in Python/Flask, Docker, and React. It was written with a lean production environment in mind.
<br>

## Getting Started

Clone this repo: https://github.com/sarapearce/bowling-game

Most changes will be made in the `users` directory.

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
<br>
Python 3.7.1
<br>
React 17.1
<br>
Nginx

### Installing

Set 1 environment variable:
```
export REACT_APP_USERS_SERVICE_URL=http://localhost/users
```

## Running the tests

`docker exec -it bowlinggame_user_1 bash`

`cd /usr/src/app/project/tests`

`pytest`

You will then see the output in terminal for the unit tests

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


## Acknowledgments

https://testdriven.io/
