Instalando
==========

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


**Observação**: O tutorial acima mostra como instalar e rodar a máquina em ambiente de desenvolvimento, para ambiente de produção, verifique o deploy.
