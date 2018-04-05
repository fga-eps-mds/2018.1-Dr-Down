#!/bin/bash
#
# Purpose: File to configure before starting the vagrant
#
# Creator: João Pedro Sconetto <sconetto.joao@gmail.com>

# DOCKER -------------------------------------------------------
file := "local.yml"

up:
	# Create the image and container
	sudo docker-compose -f ${file} up

rebuild:
	# Create the image, container and force a build
	sudo docker-compose -f ${file} up --build

logs:
	# See the logs from application
	sudo docker-compose -f ${file} logs -f -t

start:
	# Start containers
	sudo docker-compose -f ${file} start

stop:
	# Stop containers
	sudo docker-compose -f ${file} stop

ps:
	# Verify running containers
	sudo docker-compose -f ${file} ps

down:
	# Shutdown containers and remove the images
	sudo docker-compose -f ${file} down

down-force:
	# Shutdown containers, remove the images and remove the volumes
	sudo docker-compose -f ${file} down -v

# DJANGO -------------------------------------------------------

container := "django"
bash:
	# Get in the bash of container
	sudo docker exec -it ${container} /bin/sh

run:
	# Run a command inside docker
	sudo docker-compose -f ${file} run --rm ${container} ${command}

app: manage.py
	# Create a new app
	sudo docker-compose -f ${file} run --rm ${container} python manage.py startapp ${name}

createsuperuser: manage.py
	# Create a project super user
	sudo docker-compose -f ${file} run --rm ${container} python manage.py createsuperuser

shell: manage.py
	# Open an interactive shell to debug
	sudo docker-compose -f ${file} run --rm ${container} python manage.py shell

# DATABASE -----------------------------------------------------

migrations: manage.py
	# Create all migrations from models
	sudo docker-compose -f ${file} run --rm ${container} python manage.py makemigrations

migrate: manage.py
	# Migrate all migrations on database
	sudo docker-compose -f ${file} run --rm ${container} python manage.py migrate

sql: manage.py
	# Show SQL commands
	sudo docker-compose -f ${file} run --rm ${container} python manage.py sqlmigrate ${app_label} ${migration_name}

# TESTS --------------------------------------------------------
local := "**/tests/"

test: manage.py
	# Run tests
	sudo docker-compose -f ${file} run --rm ${container} python manage.py test ${local}

test-all: manage.py
	# Run tests
	sudo docker-compose -f ${file} run --rm ${container} python manage.py test

coverage: coverage
	# Run django coverage (create a covarege page)
	sudo docker-compose -f ${file} run --rm ${container} django coverage html

# TRANSLATION --------------------------------------------------
files := "**/*.py"

messages:
	# Create a django.po to insert translations (pt-BR)
	sudo docker-compose -f ${file} run --rm ${container} django-admin makemessages -l pt_BR -i ${files}

compilemessages:
	# Create translations
	sudo docker-compose -f ${file} run --rm ${container} django-admin compilemessages

# STATIC FILES -------------------------------------------------

staticfiles: manage.py
	# Collect all static files
	sudo docker-compose -f ${file} run --rm ${container} python manage.py collectstatic

# DOCUMENTATION
doc: mkdocs.yml
	# Deploy all documentation
	mkdocs gh-deploy
