Dr. Down
========

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


Ferramenta de informação e união de pessoas que convivem com a Síndrome de Down.

O Dr. Down é um sistema direcionado a auxiliar o cuidado de pessoas com Síndrome de Down realizado atualmente pelo Hospital Regional da Asa Norte, localizado em Brasília - DF, em um centro de tratamento especializado chamado Cris Down. 

:License: MIT


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ py.test

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html



Celery
^^^^^^

This app comes with Celery.

To run a celery worker:

.. code-block:: bash

    cd drdown
    celery -A drdown.taskapp worker -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.





Sentry
^^^^^^

Sentry is an error logging aggregator service. You can sign up for a free account at  https://sentry.io/signup/?code=cookiecutter  or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.


Deployment
----------

The following details how to deploy this application.



Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html


## Inicializando projeto para desenvolvimento

* De um ```git clone <url-do-repositorio>```

* Instale o docker e o docker-compose em seu computador para usar com o sudo (administrador) - padrão

* Para rodar o serviço de documentação: ```mkdocs serve```

* Execute o comando ```make up``` para gerar a imagem do projeto e o container do ambiente de desenvolvimento,
ao finalizar você pode acessar a aplicação utilizando a seguinde URL: ```0.0.0.0:8000```

* Assim que o ambiente tiver gerado crie um superusuário com os seguintes comandos:

  ```
  make bash - Para entrar dentro do container
  python3 manage.py createsuperuser
  ```

* Com isso você pode modificar os arquivos localmente em sua máquina que ele serão automaticamente modificados dentro do container, possibilitando assim ter um ambiente de desenvolvimento sem a necessidade de muita configuração do mesmo.

* **Observação**: Os comandos (make up, start, logs, stop, rm, ps) são comandos para manipulação de containers e tem como parâmetro opcional o **file** que pode passar o compose que deseja utilizar, por padrão é utilizado o **docker-compose-dev.yml** para gerar o ambiente de desenvolvimento. O de deploy é o arquivo **docker-compose-prod.yml** e o de teste é o arquivo **docker-compose-test.yml**.

* **Observação**: Os comandos relacionados ao django tem como parâmetro opcional o **container** de execução do mesmo e alguns comandos tem parâmetros obrigatórios como é o caso o **test** e **app**.

* **Observação**: Se o comando passado como parâmetro tiver espaço, utilize aspas duplas sobre ele, caso contrario não.

* **Comandos de desenvolvimento**:

  - ```make logs```: Gera a log do servidor.

  - ```make start```: Inicializa os containers.

  - ```make stop```: Para a execução dos containers.

  - ```make ps```: Usado para ver quais containers estão em execução no momento.

  - ```make rm```: Remove os containers.

  - ```make app name=<nome-do-app>```: Cria uma aplicação django, com o parâmetro **name** que é obrigatório.

  - ```make bash```: Entra no terminal de comandos do container do ambiente de desenvolvimento.

  - ```make run container=<container-de-execução> command=<comando-django>```: Executa um comando dentro do
    container especificado, o parâmetro container é opcional, por padrão é o container de desenvolvimento,
    já o parâmetro **command** é obrigatório.

  - ```make test```: Comando para rodar os testes automatizados do projeto, os testes por padrão deve estar em uma
    pasta chamada **tests** dentro de cada aplicação criada, tem como parâmetros opcionais o **container** e o **local**
    onde estão os testes.

  - ```make migrations```: Gera todas as migrações da aplicação.

  - ```make migrate```: Executa as migrações no banco de dados.

  - ```make messages```: Cria os arquivos de tradução dentro das aplicações django que tiverem a pasta **locale** criadas.

  - ```make compilemessages```: Gera as traduções especificadas no arquivo dentro da pasta **locale** de cada aplicação.

  - ```make staticfiles```: Gera uma pasta que irá englobar todos os arquivos estáticos da aplicação.
