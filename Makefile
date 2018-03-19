#!/bin/bash

# DOCKER -------------------------------------------------------
file := "docker-compose-dev.yml"

up:
# Create the image and container
ifeq (${file}, "docker-compose-dev.yml")
	sudo docker-compose -f ${file} up -d
else
	sudo docker-compose -f ${file} up
endif

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

rm:
	# Remove containers
	sudo docker-compose -f ${file} rm

# DJANGO -------------------------------------------------------

container := "drdown-dev"
bash:
	# Get in the bash of container
	sudo docker exec -it ${container} bash

run:
	# Run a command inside docker
	sudo docker exec ${container} ${command}

app: manage.py
	# Create a new app
	sudo docker exec ${container} python3 manage.py startapp ${name}

# DATABASE -----------------------------------------------------

migrations: manage.py
	# Create all migrations from models
	sudo docker exec ${container} python3 manage.py makemigrations

migrate: manage.py
	# Migrate all migrations on database
	sudo docker exec ${container} python3 manage.py migrate

sql: manage.py
	# Show SQL commands
	sudo docker exec ${container} python3 manage.py sqlmigrate ${app_label} ${migration_name}

# TESTS --------------------------------------------------------
local := "**/tests/"

test: manage.py
	# Run all tests
	sudo docker exec ${container} python3 manage.py test ${local}

# TRANSLATION --------------------------------------------------
files := "**/*.py"

messages:
	# Create a django.po to insert translations (pt-BR)
	sudo docker exec ${container} django-admin makemessages -l pt_BR -i ${files}

compilemessages:
	# Create translations
	sudo docker exec ${container} django-admin compilemessages

# STATIC FILES -------------------------------------------------

staticfiles: manage.py
	# Collect all static files
	sudo docker exec ${container} python3 manage.py collectstatic
