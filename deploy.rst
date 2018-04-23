Deploy
========

Homologação (*staging*)
-----------------------

.. _`Deploy com Docker`: https://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html

O deploy em ambiente de testes foi feito com o auxílio de algumas documentações, principalmente a que pode ser acessada pelo projeto do cookiecutter, na seção `Deploy com Docker`_, atentado as particularidades, dado ao fato desse ser o ambiente de homologação da ferramenta.

Para o deploy é necessário:

.. _`Digital Ocean`: https://www.digitalocean.com/
.. _`Freenom`: http://www.freenom.com/pt/index.html


    * Um droplet do `Digital Ocean`_ (Ubuntu 16.04.4 LTS);
    * Um domínio (foi usado o provedor Freenom_);

**Observação**: A equipe decidiu por usar as máquinas (droplets) do *Digital Ocean* para o deploy, mas uma máquina com um IP público já é apropriada para o processo.

Configurando o domínio
^^^^^^^^^^^^^^^^^^^^^^

.. _`DigitalOcean DNS`: https://www.digitalocean.com/community/tutorials/an-introduction-to-digitalocean-dns

Com uma máquina em mãos o primeiro passo é configurar o seu domínio para que o nome o qual você registrou possa apontar para a máquina (IP) a qual você irá fazer o deploy da aplicação.
Neste passo foi seguida a documentação do *Digital Ocean*, que apresenta como configurar o `DigitalOcean DNS`_.
Em poucos passos o que foi feito:

    * Adicionado o domínio registrado no *Digital Ocean*;
    * Adicionado os registros do DNS;
    * E configurado os *Nameservers* no site do registro do domínio.

Com isso sua máquina já estará mapeada no domínio registrado e já será possível acessá-la via URL do domínio.

Fazendo o deploy na máquina
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para fazer o deploy na sua máquina, que agora já tem o IP registrado num domínio, se atente em ter as seguintes dependências instaladas:

.. _`passos de instalação`: https://github.com/fga-gpp-mds/2018.1-Dr-Down/blob/develop/docs/install.rst
.. _este: https://linode.com/docs/web-servers/nginx/how-to-configure-nginx/
.. _esta: https://www.nginx.com/resources/wiki/start/topics/examples/full/
.. _Issue: https://github.com/fga-gpp-mds/2018.1-Dr-Down/issues/new

    * Nginx
    * Docker
    * Docker Compose

Acesse sua máquina via SSH e faça os `passos de instalação`_.

Agora é necessário configurar o Nginx para que ele possa mapear as portas e servir os arquivos da sua instalação.
Aconselhamos este_ tutorial ou se preferir esta_ documentação, que é o exemplo encontrado no site oficial do Nginx.
Mas é importante ressaltar que ao instalar o *nginx* na sua máquina, o mesmo cria um arquivo *default* de configuração e a ferramenta do Dr. Down já trabalha automaticamente com essa porta, logo com a configuração *default* a aplicação deve rodar sem problema, caso precise mudar ou especificar algo diferente, leia os documentos supracitados.
Com isto certifique que:

    * Tem as dependências instaladas;
    * As instruções de instalação do software foram seguidas;
    * Os *containers* docker estão rodando em máquina (status *Up*).

Caso todos os passos acima tenham sido feitos, agora, basta acessar a URL do seu domínio que o site Dr. Down deverá estar disponível para o ambiente de homologação.

**Observação**: Caso enfrente algum problema, sempre verique os logs de máquina, e não hesite em nos contatar via Issue_ no GitHub, faremos o possível para ajudar.

**Observação**: Os comandos de máquina como *makemigrations*, *migrate*, *shell*, *createsuperuser* e etc, devem ser feitos na máquina host da aplicação, assim como a verficação de usuários por e-mail deverá ser feita como o padrão em desenvolvimento (pegar o link de verificação gerado pelo *output* do console da aplicação).

Deploy Contínuo
^^^^^^^^^^^^^^^

.. _`Travis CI`: https://travis-ci.org/

A aplicação Dr. Down tem um pipeline de deploy contínuo para o ambiente de homologação, ele é executado junto com os testes e a *build* nos *jobs* do `Travis CI`_, caso queira manter o mesmo pipeline usado por nós modifique o arquivo ``.travis.yml`` que fica na pasta raíz do projeto, se atentando em configurar de acordo com as suas necessidades os seguintes parâmetros:

    * Usuário do Docker Hub;
    * Senha de acesso ao Docker Hub;
    * IP da máquina de deploy;
    * Senha de acesso a máquina de deploy.

Com esses parâmetros devidamente configurados, o deploy contínuo deve funcionar normalmente no seu contexto.

Produção (*production*)
-----------------------

O deploy em ambiente de produção ainda está em fase de teste, portanto ainda não será documentado aqui.
