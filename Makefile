build:
	docker-compose up --build

run:
	docker-compose up

destroy:
	docker-compose down -v

rebuild: destroy build

makemigrations:
	docker-compose run web python manage.py makemigrations

migrate:
	docker-compose run web python manage.py migrate

bash:
	docker-compose run web bash

data:
	docker-compose run web python manage.py seed_data
	
shell:
	docker-compose run web python manage.py shell_plus

lint:
	isort .
	black .
