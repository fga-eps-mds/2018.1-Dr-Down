## Inicializando projeto para desenvolvimento

* De um ```git clone <url-do-repositorio>```

* Instale o docker e o docker-compose em seu computador para usar com o sudo (administrador) - padrão

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
