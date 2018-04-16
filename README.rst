Dr. Down
========

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django

.. image:: https://api.codeclimate.com/v1/badges/d15319efe86e7cda99aa/maintainability
     :target: https://codeclimate.com/github/fga-gpp-mds/2018.1-Dr-Down/maintainability
     :alt: Maintainability

.. image:: https://api.codeclimate.com/v1/badges/d15319efe86e7cda99aa/test_coverage
     :target: https://codeclimate.com/github/fga-gpp-mds/2018.1-Dr-Down/test_coverage
     :alt: Test Coverage

.. image:: https://travis-ci.org/fga-gpp-mds/2018.1-Dr-Down.svg?branch=develop
     :target: https://travis-ci.org/fga-gpp-mds/2018.1-Dr-Down
     :alt: Build

.. image:: https://img.shields.io/badge/License-MIT-blue.svg
     :target: https://github.com/fga-gpp-mds/2018.1-Dr-Down/blob/develop/LICENSE
     :alt: License


Ferramenta de informação e união de pessoas que convivem com a Síndrome de Down.

O Dr. Down é um sistema direcionado a auxiliar o cuidado de pessoas com Síndrome de Down realizado atualmente pelo Hospital Regional da Asa Norte, localizado em Brasília - DF, em um centro de tratamento especializado chamado Cris Down.

Documentação:
-------------

Toda a documentação e artefatos produzidos pela equipe do Dr. Down pode ser encontrado na página:

https://fga-gpp-mds.github.io/2018.1-Dr-Down/

Contribuindo:
-------------

.. _CONTRIBUTING: https://github.com/fga-gpp-mds/2018.1-Dr-Down/blob/develop/.github/CONTRIBUTING.md

Para contribuir com o projeto, por favor, leia o CONTRIBUTING_, nele contém algumas informações importantes de como contribuir, um link para o nosso código de conduta e alguns dos nossos padrões!

Comandos Básicos (Em desenvolvimento):
--------------------------------------

Rodando a aplicação:
^^^^^^^^^^^^^^^^^^^^
**Observação**: Recomendamos, e o processo abaixo foi executado, uma máquina Ubuntu/Linux com a distribuição ``Ubuntu 16.04.4 LTS``.

O primeiro passo é fazer o clone do projeto pelo GitHub (tenha certeza de ter o ``git`` instalado em sua máquina)::

    $ git clone https://github.com/fga-gpp-mds/2018.1-Dr-Down.git

Para rodar a aplicação tenha certeza de ter algumas dependências instaladas. Existem dois scripts que auxiliam o você nessa etapa.
Para fazer a instalação basta rodar (partindo que está na pasta base após clone) os seguintes ``shell scripts``::

    $ sudo bash utility/install_os_dependencies.sh arg
    $ sudo bash utility/install_python_dependencies.sh

No primeiro script será necessário dizer qual é o ``arg`` da operação que deseja fazer, as funções disponíveis são:

    * list
    * help
    * install
    * upgrade

Certifique de ter instalado também:

    * docker
    * docker-compose

E por fim, agora para rodar a aplicação basta rodar o seguinte comando no seu terminal::

    $ docker-compose -f local.yml up --build

Com isso as imagens serão baixadas e geradas na sua máquina e você poderá acessar a aplicação pelo seu navegador no endereço ``127.0.0.1:8000``.

**Observação**: Caso deseje parar os containers basta usar a combinação **CTRL+C** no terminal que está rodando a aplicação, ou, caso esteja rodando em *backgroud* executar o comando::

    $ docker-compose -f local.yml down

Configurando seu usuário:
^^^^^^^^^^^^^^^^^^^^^^^^^

* Para criar um **conta de usuário normal**, vá em Criar Conta e preencha os campos. Assim que você submeter suas informações, você verá uma página de "Verificar seu endereço de E-mail". Vá no seu terminal, no seu console você verá uma mensagem de email de verificação. Copie o link para seu negador. Agora o E-mail do usuário deve ser verificado e pronto para ser usado.

* Para criar uma **conta super usuário**, use esse comando::

    $ docker-compose -f local.yml run --rm django python manage.py createsuperuser

Por conveniência, você pode manter o seu usuário normal logado no Chrome e seu super usuário (administrador) logado no Firefox (ou similar), assim você consegue ver como o site se comporta em ambos usuários.

Teste de cobertura:
^^^^^^^^^^^^^^^^^^^^

Para verificar a cobertura do seu código, assim como rodar a suíte de testes da sua aplicação, basta rodar os seguintes comandos abaixo::

    $ docker-compose -f local.yml run --rm django coverage run -m py.test
    $ docker-compose -f local.yml run --rm django coverage html
    $ firefox htmlcov/index.html

.. _coverage: https://coverage.readthedocs.io/en/coverage-4.5.1/

**Observação**: Será gerada uma pasta ``htmlcov/`` que conterá o ``index.html``, este arquivo contem o relatório extraído dos testes rodados, no exemplo acima foi utilizado o navegador *Mozilla Firefox* para a abertura do arquivo HTML gerado. Outras configurações, *flags* e modos de uso do coverage podem ser verificadas na documentação do coverage_.

Rodando os testes com py.test:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para apenas rodar a suíte de testes com o py.test basta executar o seguinte comando::

    $ docker-compose -f local.yml run --rm django py.test

.. _py.test: https://docs.pytest.org/en/latest/contents.html

**Observação**: No próprio terminal será mostrado o *output* dos testes rodados. Outras configurações, *flags* e modos de uso do py.test podem ser verificadas na documentação do py.test_.


*Live Reloading* e Compilação SASS CSS:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html

Caso queira usar a compilação de SASS/CSS ou fazer o uso do *Live Reloading* leia a documentação do cookiecutter acerca em `Live reloading and SASS compilation`_.

Outras Configurações:
^^^^^^^^^^^^^^^^^^^^^

.. _`configurações django`: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

O projeto se apoia em configurações por meio de arquivos de configuração de ambiente, caso deseje neste, link é possível ver o mapa das variáveis de ambiente das `configurações django`_ do projeto.

*Deploy*:
---------

Os detalhes a seguir mostram como implantar esse aplicativo.

Docker
^^^^^^

.. _`deploy com docker`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html

O projeto se apoia em containers para utilização dos serviços e o seu *deploy*.
Veja mais detalhes de como fazer o deploy na documentação do cookiecutter acerca de `deploy com docker`_.

Outras informações
------------------

Caso queira rodar o serviço de documentação do projeto em sua máquina local, com o projeto já clonado, basta rodar::

    $ mkdocs serve

Makefile para desenvolvimento:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _Makefile: https://github.com/fga-gpp-mds/2018.1-Dr-Down/blob/develop/Makefile

Para auxiliar os desenvolvedores foi criado um arquivo ``Makefile`` com alguns comandos docker que agilizam a execução de tarefas durante o desenvolvimento do software, caso se interesse em usar verique os comandos disponíveis do Makefile_.
