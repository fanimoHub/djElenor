# متغیرهای پروژه
PROJECT_NAME=DjElenor

# -------------------------- Django --------------------------
mk:
	python3 manage.py makemigrations

mi:
	python3 manage.py migrate


# -------------------------- Docker Compose --------------------------
build:
	docker-compose up --build

up:
	docker-compose up

upd:
	docker-compose up -d

down:
	docker-compose down

downr:
	docker-compose down -v
