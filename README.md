Kaizen IoT Challenge
==============

This is a Docker (with docker-compose) environment for Kaizen IoT Challenge.

# Installation

1. First, clone this repository:

```bash
$ git clone https://github.com/nietzscheson/raizen-iot-challenge
```
2. Copy the environment vars:

```bash
$ cp .env.dist .env
```
3. Init project
```bash
$ make
```
4. Show containers:
```bash
$ make ps
```
This results in the following running containers:
```bash
> $ docker-compose ps
               Name                              Command                  State                        Ports
------------------------------------------------------------------------------------------------------------------------------
core                                  /bin/sh -c gunicorn --bind ...   Up             0.0.0.0:8000->8000/tcp,:::8000->8000/tcp
postgres                              docker-entrypoint.sh postgres    Up (healthy)   0.0.0.0:5432->5432/tcp,:::5432->5432/tcp
raizen-iot-challenge_default-core_1   python3                          Exit 0
```
4. Testing features:
```bash
$ make test
```
4. Import the dataset:
```bash
$ make import
```
The resources are:

- http://localhost:8000/highest-co2
- http://localhost:8000/hottest-temperature
- http://localhost:8000/highest-humidity