.PHONY: init 

init: 
	@make down
	@make up
	@make ps
	@make logs
down:
	docker-compose down --volumes --remove-orphans
pull:
	docker-compose pull
build:
	docker-compose build
up: 
	make pull 
	make build
	docker-compose up -d
ps:
	docker-compose ps
logs:
	docker-compose logs core
test:
	docker-compose run --rm core python -m unittest
prune:
	make down
	docker volume prune -f
	docker system prune -f
format:
	docker-compose run --rm core black .
lint:
	docker-compose run --rm core black . --check