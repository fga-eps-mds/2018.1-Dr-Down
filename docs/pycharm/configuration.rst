Docker Debug Remoto
=======================

Para conectar um interpretador remoto de python dentro da docker, você deve primeiro garantir que o seu *Pycharm* está ciente da sua docker.

Vá em *Settings > Build, Execution, Deployment > Docker*. Se você está em um ambiente linux você pode usar o docker diretamente usando o *socket* `unix:///var/run/docker.sock`, se você está em um Windows ou Mac, certifique-se de ter o *docker-machine instalado, e então você pode simplesmente importar suas credencias (*Import credentials from Docker Machine*). 

.. image:: images/1.png

Configurar Interpretador Remoto Python
--------------------------------------

Esse repositório já vem preparado para com "Configurações de Executar/Debugar" para *docker*.

.. image:: images/2.png

Mas como vocẽ pode ver, no começo há algo de errado com as configurações. Elas them um X vermelho no ícone do django, e elas não podem ser usadas sem a configuração do interpretador remoto python. Para isso você deve ir em *Settings > Build, Execution, Deployment* primeiro.


Agora, você deve adicionar um novo interpretador remoto python, com base nas configurações de implantação já testadass. Vá para *Settings > Project > Project Interpreter*. Clique na engrenagem e então em *Add Remote*.

.. image:: images/3.png

Troque para *Docker Compose* e selecione o arquivo `local.yml` do diretório do seu projeto, em seguida configure o *Service name* para `django`

.. image:: images/4.png

Feito isso, clique *OK*. Feche o painel de configuração e espere alguns segundos...

.. image:: images/7.png

Depois de alguns segundos, todas as *Run/Debug Configurations* devem estar pronta para uso.

.. image:: images/8.png

**Coisas que você pode fazer com a configuração fornecida**:

* executar e debugar código python
.. image:: images/f1.png
* executar e debugar testes
.. image:: images/f2.png
.. image:: images/f3.png
* executar e debugar migrações ou comandos do *django management*
.. image:: images/f4.png
* e vários outros..

Known issues
------------

* Pycharm trava em "Connecting to Debugger"

.. image:: images/issue1.png

Isso pode ser algum problema com o seu firewall. Dê uma olhada neste ticket - https://youtrack.jetbrains.com/issue/PY-18913

* Arquivos modificados no diretório `.idea` 

A maioria dos arquivos do diretório `.idea` foram adicionados ao `.gitignore` com algumas exceções, o qual foram feitos, para fornecer uma configuração *"ready to go"*. Depois de adicionar o interpretador remoto alguns desses arquivos serão alterados pelo PyCharm: 

.. image:: images/issue2.png

Em teoria você pode removê-los do repositório, mas então, outras pessoas perderão a capacidade de inicializar um projeto a partir das configurações como você fez. Para se livrar deste estado incoveniente, você pode rodar o comando::

    $ git update-index --assume-unchanged drdown.iml
