Creditas Challenge
==============

This is a Docker (with docker-compose) environment for Creditas Challenge.

# Installation

1. First, clone this repository:

```bash
$ git clone https://github.com/nietzscheson/creditas-api-challenge
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
                Name                               Command                  State               Ports
--------------------------------------------------------------------------------------------------------------
core                                    /bin/sh -c gunicorn --bind ...   Up             0.0.0.0:8000->8000/tcp
creditas-api-challenge_default-core_1   python3                          Exit 0
postgres                                docker-entrypoint.sh postgres    Up (healthy)   0.0.0.0:5432->5432/tcp
```
5. Testing features:
```bash
$ make test
```
The resources are:

- http://localhost:8000/leads -> GET

To be able to create resources, please use:

  - Lead Auto:

    - Request: 
    ```bash 
    curl -X POST localhost:8000/leads -H 'Content-Type: application/json' -d '{ "type": "AUTO", "name": "Isabella Angulo", "telephone": "123456789", "email": "isabella@angulo.com", "rfc": "ABCD1234567890", "address": "Calle 1", "auto": { "model": "Ford", "price": "500000.00"}}'
    ```
    - Response:
    ```bash
    {"message": "The Lead 1 record has been created!", "data": {"id": 1, "type": "AUTO", "status": "APROVE", "name": "Isabella Angulo", "telephone": "123456789", "email": "isabella@angulo.com", "rfc": "ABCD1234567890", "address": "Calle 1", "auto": {"id": 1, "model": "Ford", "price": 500000.0}}}
    ```
  - Lead House
    - Request:
    ```bash
    curl -X POST localhost:8000/leads -H 'Content-Type: application/json' -d '{ "type": "HOUSE", "name": "Emmanuel Angulo", "telephone": "123456789", "email": "emmanuel@angulo.com", "rfc": "ABCD1234567890", "address": "Calle 2", "house": { "address": "CDMX", "price": "200000.00"}}'
    ```
    - Response:
    ```bash
    {"message": "The Lead 1 record has been created!", "data": {"id": 1, "type": "HOUSE", "status": "APROVE", "name": "Emmanuel Angulo", "telephone": "123456789", "email": "emmanuel@angulo.com", "rfc": "ABCD1234567890", "address": "Calle 2", "house": {"id": 1, "address": "CDMX", "price": 200000.0}}}
    ```
  - Lead Payroll
    - Request:
    ```bash
    curl -X POST localhost:8000/leads -H 'Content-Type: application/json' -d '{ "type": "PAYROLL", "name": "Dulce Agar", "telephone": "123456789", "email": "isabella@angulo.com", "rfc": "ABCD1234567890", "address": "Calle 3", "payroll": { "company": "ABCD inc.", "admission_at": "15"}}'
    ```
    - Response:
    ```bash
    {"message": "The Lead 2 record has been created!", "data": {"id": 2, "type": "PAYROLL", "status": "APROVE", "name": "Dulce Agar", "telephone": "123456789", "email": "isabella@angulo.com", "rfc": "ABCD1234567890", "address": "Calle 3", "payroll": {"id": 1, "company": "ABCD inc.", "admission_at": "15"}}}
    ```
    