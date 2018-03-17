#!/bin/sh


# Esperando o Postgres inicializar
postgres_ready() {
python3 << END
import sys
import psycopg2
try:
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="", host="db")
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "Postgresql está indisponível - Esperando..."
  sleep 1
done

echo "Deletando migrações"
find . -path "*/migrations/*.pyc"  -delete
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

echo "Deletando diretorio de arquivos estáticos"
find . -path "tbl/staticfiles/*"  -delete

echo "Criando migrações e tabelas do banco de dados"
python3 manage.py makemigrations
python3 manage.py migrate
