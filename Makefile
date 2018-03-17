# DOCKER -------------------------------------------------------
up:
	# Create the image and container
	sudo docker-compose up

exec:
	# Get in the bash of tlb container
	sudo docker exec -it drdown_dev bash

# DJANGO -------------------------------------------------------

app: manage.py
	# Create a new app
	sudo docker exec drdown_dev python manage.py startapp ${name}

# DATABASE -----------------------------------------------------

migrations: manage.py
	# Create all migrations from models
	sudo docker exec drdown_dev python3 manage.py makemigrations

migrate: manage.py
	# Migrate all migrations on database
	sudo docker exec drdown_dev python3 manage.py migrate

superuser: manage.py
	# Create a super user on system.
	sudo docker exec drdown_dev python3 manage.py createsuperuser

sql: manage.py
	# Show SQL commands
	sudo docker exec drdown_dev python3 manage.py sqlmigrate ${app_label} ${migration_name}

# TRANSLATION --------------------------------------------------
#
files := "tbl/*.py"

messages:
	# Create a django.po to insert translations (pt-BR)
	sudo docker exec drdown_dev django-admin makemessages -l pt_BR -i ${files}

compilemessages:
	# Create translations
	sudo docker exec drdown_dev django-admin compilemessages

# STATIC FILES -------------------------------------------------

staticfiles: manage.py
	# Collect all static files
	sudo docker exec drdown_dev python3 manage.py collectstatic
