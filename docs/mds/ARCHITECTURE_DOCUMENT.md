# Documento de Arquitetura

## Histórico de Revisão

| Data | Versão | Descrição | Autores |
|  ---  |  ---  |  ---  |  ---  |
| 24/03/2018 | 0.0.1 | Abertura do documento | Geovana Ramos |
| 26/03/2018 | 0.1.0 | Tópicos 1 e 2 | Guilherme Guy e Gabriela Medeiros |
| 26/03/2018 | 0.2.0 | Tópicos 3 e 4 | Daniel Maike e Joberth Rogers |
| 26/03/2018 | 0.3.0 | Tópicos 5 e 6 | Elias Bernardo e Geovana Ramos |
| 27/03/2018 | 0.3.1 | Correção de informações histórico de revisão | Daniel Maike, Gabriela Medeiros e Joberth Rogers |
| 27/03/2018 | 0.4.0 | Diagrama de classes | Elias Bernardo, Geovana Ramos e Guilherme Guy |
| 28/03/2018 | 0.5.0 | Alteração no tópico 3 | Daniel Maike e Geovana Ramos |
| 28/03/2018 | 0.6.0 | Modelo Entidade Relacionamento | Daniel Maike e Joberth Rogers |
| 28/03/2018 | 0.6.1 | Revisão geral | Daniel Maike e Joberth Rogers |
| 28/03/2018 | 1.0.0 | Entrega da primeira versão estável | Daniel Maike, Elias Bernardo, Joberth Rogers, Guilherme Guy, Gabriela Medeiros e Geovana Ramos |
| 29/03/2018 | 1.0.1 | Revisões gerais | Daniel Maike, Guilherme Guy e Joberth Rogers |
| 29/03/2018 | 1.1.0 | Adição do tópico 2.4 | Geovana Ramos |
| 01/04/2018 | 1.2.0 | Melhorando o tópico de representação arquitetural | Victor Arnaud |
| 01/04/2018 | 1.2.1 | Corrigindo inconsistências | Victor Arnaud |
| 12/04/2018 | 1.3.0 | Modificando para arquitetura baseada em componentes | Victor Arnaud |
| 15/04/2018 | 1.4.0 | Modificando imagem da arquitetura | Victor Arnaud e Geovana Ramos |

## 1: Introdução

### 1.1	Finalidade

Este documento tem como finalidade apresentar uma visão geral da arquitetura que será usada no desenvolvimento do projeto e permitir um maior entendimento do sistema Dr. Down e de como ele irá se comportar e se comunicar com as outras aplicações que compõem o projeto. Com o maior detalhamento da arquitetura, espera-se deixar explícitas as decisões arquiteturais feitas pela equipe de desenvolvimento em conjunto com os gestores do projeto para o desenvolvimento do software.

### 1.2	Escopo

Dr. Down será uma ferramenta desenvolvida para gerenciar, auxiliar e facilitar a administração do fluxo de pacientes do CRIS DOWN, além de possibilitar a comunicação entre médicos, pacientes e familiares. O documento apresentará toda a parte arquitetural para a confecção do software Dr. Down, a fim de tornar claras as características arquiteturais do projeto.

### 1.3	Definições, acrônimos e abreviações

| Abreviação | Definição |
|--------|------|
| SD | Síndrome de Down |
| CRIS DOWN |Centro de Referência em Síndrome de Down |
| MDS | Métodos de Desenvolvimento de Software |
| EPS| Engenharia de Produto de Software |
| UnB | Universidade de Brasília |
| SES | Secretaría de Estado de Saúde |
| CBV | Class-Based Views |

## 2: Representação Arquitetural

![Arquitetura](https://user-images.githubusercontent.com/14116020/38784325-8dad88ee-40e6-11e8-8746-46ae3034d386.png)

A arquitetura utilizada no projeto será a arquitetura baseada em componentes. O conceito de _Django Application_ é uma das principais inovações do Django e um dos grandes responsáveis por sua flexibilidade e alto reaproveitamento de componentes, ou seja, um aplicação é criada, mantida, executada e distribuída de forma totalmente independente contendo as seguintes características: alta coesão, baixo acoplamento, reutilizável e independente, que representa um contexto de negócio, além de ser externo ao projeto que irá utilizá-lo. Com isso, serão adotadas aplicações que sigam todas essas caractísticas e estejam empacotadas no [pypi](https://pypi.python.org/pypi). Cada aplicação do Django utiliza da arquitetura MVT internamente.

A arquitetura baseada em componentes é um ramo de Engenharia de Software, com ênfase na decomposição dos sistemas em componentes independentes, substituíveis e modulares, elas ajudam a gerenciar a complexidade e encorajam a reutilização.

Alguns benefícios desse modelo de arquitetura:

* **Fácil deploy**: Compatilidade de novas versões quando disponíveis. É possível substituir a versão existente sem impacto em outros componentes do sistema como um todo.

* **Redução de custos**: O uso do componente de terceiros permite a redução do custo do desenvolvimento e manutenção.

* **Fácil desenvolvimento**: Implementar componentes bem como a funcionalidade definida pela interface, permite desenvolvimento sem impacto em outros partes do sistema.

* **Reutilização**: A reutilização de componentes é um meio de agilizar o desenvolvimento e manutenção onde agrega na redução de custo da aplicação.

O projeto terá algumas aplicações externas que serão inseridas e comunicadas com as aplicações do projeto. O framework já disponibiliza toda a estrutura para fazer essa comunicação entre componentes. Porém serão utilizados microsserviços ou APIs quando necessário, com esses sendo comunicados via requisições HTTP.

Abaixo está listado como a arquitetura do projeto será comunicada com outros serviços externos de configuração, como servidor NGINX, banco de dados PostgreSQL entre outros e terá o tópico em que será explicado com mais detalhes o funcionamento da arquitetura de cada aplicação presente no projeto Django (MVT) e uma tabela com os possíveis aplicações selecionados para a inserção ou não no projeto.

### 2.1 NGINX:

O NGINX é um servidor web que pode atuar como um proxy reverso para HTTP, HTTPS, SMTP, POP3 e IMAP, bem como um balanceador de carga. O NGINX é um servidor web rápido e com inúmeras possibilidades de configuração para melhor performace.

No projeto ele é utilizado como um redirecionador de portas utilizando-se de proxy reverso para que ambos os arquivos estáticos e o servidor de produção do Django possam compartilhar da mesma porta 80 servindo os arquivos estáticos separados da aplicação.

### 2.2 Django

O Dr.Down será uma aplicação web desenvolvida a partir do framework Django, o qual é escrito em Python. O padrão arquitetural utilizado pelas aplicações do Django é a MVT (Model, View e Template), que é derivada da do padrão arquitetural MVC (Model, View e Controller). De acordo com o DjangoBook, a parte de controller, em Django, é tratada pelo próprio framework. Portanto a View do MVT desempenha um papel próximo, mas não igual ao controller.

Como citado acima, cada aplicação do Django, pode ser considerada um componente se seguir todas as caracteristicas citadas e estiver empacotado e mantido no **pypi**. Para mais informações: <a href="https://docs.djangoproject.com/pt-br/2.0/intro/reusable-apps/">Tutorial avançado: Como escrever aplicações reutilizáveis</a>

Abaixo está explicado como funciona a arquitetura interna de cada aplicação do Django e quais componentes foram selecionados para complementar o projeto.

#### 2.2.1 Model

É uma representação do banco de dados. Além disso, também inclui características, relações e outros comportamentos que os dados podem assumir.

O Django inclui varias ferramentas para automatizar tanto quanto possível o processo e a manipulação do banco de dados, de forma que o desenvolvedor não precise se preocupar tanto com o banco de dados, o que ajuda no foco do desenvolvimento da aplicação de forma mais rápida.

#### 2.2.2 View

Estabelece uma ponte entre a Models e o Templates. Recebe as requisições do usuário a partir do template, acessa o banco de dados e então retorna a informação solicitada pelo usuário, por meio de HTML, XML e/ou os erros encontrados.

#### 2.2.3 Template

Agrega toda a parte visual que estará visível para os usuários. Inclui os códigos HTML, CSS, javascript, entre outras linguagens que são utilizadas na apresentação da View ao usuário.

#### 2.2.4 Componentes

Critérios de aceitação de um componente:

1. **Alta coesão**: O componente deve realizar uma, e apenas uma tarefa especifica e deve ser pequeno.
2. **Baixo acoplamento**: O componente não deve depender de outra classe ou funcionalidade do projeto na qual está sendo inserido.
3. **Independente**: O componente deve ser criado, mantido, executado e distribuido de forma independente, ou seja, deve ter o mínimo de dependência com outros componentes.
4. **Reutilizavel**: O componente deve ser reutilizavel, ou seja, pode ser inserido em qualquer projeto, independente de seu contexto e fácilmente substituido se for preciso.
5. **Extensibilidade**: Um componente pode ser extendido a partir de outro componente para fornecer um novo comportamento.
6. **Encapsulamento**: O componentes deve expor uma interface dele para os invocadores utilizar suas funcionalidades e não revelar detalhes do seu processo interno ou alguma variável interna e estado.
7. **Externo ao projeto**: O componente deve está disponibilizado no **pypi**.
8. **Qualidade**: O componente deve está testado e ter build funcionando, deve ser completo e em uma versão estável.

A cada sprint do projeto será definido a utilização ou não de cada componente disponibilizado nas tabelas abaixo. Os microserviços e APIs consumidas também serão listadas nas tabelas abaixo.

#### Manter usuário (Médico, Paciente, Parente, Funcionario):

|Aplicação|Descrição da aplicação|Foi utilizado?|Motivo da utilização ou não|
|---------|----------------------|:------------:|---------------------------|
|[django-allauth](https://www.intenct.nl/projects/django-allauth/)|O django-allauth é um aplicativo Django reutilizável que permite autenticação local e social.|Sim|Ele foi utilizado para a criação do usuário base que será a base para todos os outros usuários do sistema|

#### Página de informações e notícias

|Aplicação|Descrição da aplicação|Foi utilizado?|Motivo da utilização ou não|
|---------|----------------------|:------------:|---------------------------|
|[NewsAPI](https://newsapi.org/s/google-news-api)|API que disponibiliza manchetes, artigos, imagens e outros metadados de artigos do Google Notícias via JSON.|A decidir|A API ainda está sendo avaliado pela equipe.|


#### Foruns e discussões

|Aplicação|Descrição da aplicação|Foi utilizado?|Motivo da utilização ou não|
|---------|----------------------|:------------:|---------------------------|
|[django-forum-app](https://github.com/urtzai/django-forum-app)|Um aplicativo muito simples e minimalista para criar fóruns|Não|Foi proposta no meio da implementação do mesmo pela equipe de desenvolvimento, logo foi descartado|

#### Ficha Médica

|Aplicação|Descrição da aplicação|Foi utilizado?|Motivo da utilização ou não|
|---------|----------------------|:------------:|---------------------------|
|||||

#### Fila de espera

|Aplicação|Descrição da aplicação|Foi utilizado?|Motivo da utilização ou não|
|---------|----------------------|:------------:|---------------------------|
|||||

#### Comunicação entre usuários

|Aplicação|Descrição da aplicação|Foi utilizado?|Motivo da utilização ou não|
|---------|----------------------|:------------:|---------------------------|
|[Rocket.Chat](https://github.com/jadolg/rocketchat_API)|É um microserviço de chat open sourcer baseado no Slack e construído em Meteor|A decidir|O projeto ainda está sendo avaliado pela equipe.|
|[Receita-Mais](https://github.com/fga-gpp-mds/2017.2-Receita-Mais)|Software responsável por auxiliar a prescrição de receitas|Não|Não passou em quase todos so critérios definidos acima, a aplicação chat do projeto está bastante acoplado, ou seja, teria dificuldade de desacoplar e empacotar o mesmo, gerando tempo e esforço|
|[django-private-chat](https://github.com/Bearle/django-private-chat)|Chat assíncrono baseado em Websocket|A decidir|O projeto ainda está sendo avaliado pela equipe|
|[django-tawkto](https://github.com/CleitonDeLima/django-tawkto)|Projeto simples integrado com o chat [tawk.to](https://www.tawk.to/)|A decidir|O projeto ainda está sendo avaliado pela equipe|

#### Procedimento médico por faixa etária

|Aplicação|Descrição da aplicação|Foi utilizado?|Motivo da utilização ou não|
|---------|----------------------|:------------:|---------------------------|
|||||

#### Agenda com eventos

|Aplicação|Descrição da aplicação|Foi utilizado?|Motivo da utilização ou não|
|---------|----------------------|:------------:|---------------------------|
|||||

#### Localização

|Aplicação|Descrição da aplicação|Foi utilizado?|Motivo da utilização ou não|
|---------|----------------------|:------------:|---------------------------|
|[GoogleMapsAPI](https://developers.google.com/places/web-service/?hl=pt-br)|API do google maps com informações sobre milhões de locais|A decidir|A API ainda está sendo avaliado pela equipe.|

#### Outros

|Aplicação|Descrição da aplicação|Foi utilizado?|Motivo da utilização ou não|
|---------|----------------------|:------------:|---------------------------|
|[django-role-permissions](https://github.com/vintasoftware/django-role-permissions)|É um aplicativo de Django para permissões baseadas em função. Ele é construído sobre as funcionalidades Group e Permission do usuário do Django contrib.auth e não adiciona nenhum outro modelo ao seu projeto, ou seja, é totalmente independente.|Sim|Ele será utilizado no projeto para a criação de permissões de cada tipo de usuário do sistema e as permissões de acesso a determinadas páginas|
|[django-crispy-forms](http://django-crispy-forms.readthedocs.io/en/latest/)|É um aplicativo do Django que permite a construção, customização e reutilização de formulários facilmente podendo usar qualquer framework CSS, sem escrever código de template e sem ter que cuidar de outros tipos de detalhes.|Sim|Foi utilizado para facilitar a criação de formulários|

### 2.3 Banco de dados PostgreSQL

PostgreSQL é um poderoso sistema de banco de dados objeto-relacional de código aberto. Ele é executado em todos os principais sistemas operacionais, tem 15 anos de desenvolvimento ativo e uma arquitetura comprovada que lhe garantiu uma forte reputação de confiabilidade, integridade de dados e correção.

Para o projeto será utilizado o PostgreSQL como o banco de dados de desenvolvimento e produção da aplicação Dr. Down, pela simplicidade e segurança do mesmo.

### 2.4 Redis

Redis é um banco de dados não relacional, também conhecido como NOSQL que armazena dados no formato "chave-valor" em memória e é extremamente rápido.

O Redis é um servidor TCP, e seu funcionamento baseado em um modelo cliente-servidor, dessa forma, quando uma requisição é feita para o Redis, um comando é enviado ao servidor (Redis) pelo cliente, e este fica aguardando uma resposta do servidor através de uma conexão estabelecida via socket. Quando o servidor processa o comando, ele envia a resposta de volta ao cliente.

O Redis é uma boa opção para cenários nos quais é necessário alta performance para gravação e/ou leitura de dados baseado em chave-valor, sendo ele utilizado para servir como um servidor de cache para a aplicação, pois além de tudo, ele ainda permite que uma chave expire após um determinado período, dessa forma pode ser utilizado para gerenciar sessões de usuário.

O redis é usado na aplicação para fazer o cacheamento (_cache_) Django, com isso alguma _query_ que a aplicação faria diretamente ao banco o redis se comunicada e armazena o cache já com o resultado desta forma aumentando o desempenho e mantendo a aplicação _mint_ (com performance sempre igual desde o primeiro), mesmo com grandes quantidades de dados. O redis comunica o container do Django com o postgre e serve resultados de volta para o Django

### 2.5 Celery

O celery é um gerenciador de tarefas assíncronas. Com ele você pode executar uma fila de tarefas (que ele recebe por meio de mensagens), pode agendar tarefas direto no seu projeto sem precisar do cron e ele ainda tem integração fácil com a maioria dos frameworks python mais utilizados como Django, Flask e etc.

No caso do Django, sempre que um cliente faz uma requisição web (request), o servidor faz um processamento. Ele lê a requisição, trata os dados recebidos, salva ou recupera registros do banco de dados (através dos models), faz algum processamento do que será exibido para o usuário, renderiza isso em um template e manda uma resposta (response) para o cliente.

Dependendo da tarefa que você executa no servidor a resposta pode demorar muito e isso leva à problemas de **TimeOut**, a experiência do usuário fica comprometida. Existem diversas tarefas no projeto que podem demorar para ser executadas, como relatórios pesados, enviar diferentes emails para uma lista de usuários, e por ai vai...

O celery funciona da seguinte maneira: O cliente (Django) pode passar uma lista de tarefas para a fila do **Message Broker**, um programa responsável por manter a fila de mensagens que serão trocadas entre o seu programa e o Celery, geralmente é o RabbitMQ ou o Redis, no nosso caso será o Redis. O Message Broker distribui essas tarefas ente os **workers**, que vão executar as tarefas que devem ser assíncronas, e o resultado dessas tarefas pode ser escrito em um **Result Score** (Memóri cache, MongoDb ou até mesmo o Redis) que mais tarde pode ser lido pelo cliente novamente.

Ele é configurado por padrão pela ferramenta "cookiecutter", porém a decisão de utiliza-lo ou não no projeto ainda está sendo discutido, já que futuramente o projeto pode precisar dessa ferramenta para o gerenciamento de tarefas assíncronas. Caso não precise esse serviço será descartado.

### 2.6 Comunicação

1 - O **web client (navegador)** manda uma requisição para o **web server (Nginx)** com o protocolo HTTP.

2 - Os arquivos estáticos armazenados no sistema de arquivos, como CSS, JavaScript, Imagens e documentos PDF, são processados diretamente pelo **web server (Nginx)**.

3 - A parte dinâmica é delegada ao servidor de aplicativos WSGI (Web Server Gateway Interface) do Django, no caso o **gunicorn** que é um servidor WSGI para Unix feito em python puro e disponibilizada pelo framework Django, ele irá converter solicitações HTTP recebidas do servidor em chamadas python em colaboração com o framework Django que irá ter um arquivo chamado urls.py que diz ao nginx qual código deverá ser executado de acordo com o path e código HTTP recebido, através de proxy reverso será feito o redirecionamento inicial do Nginx com o servidor da aplicação, ou seja, o proxy reverso irá funcionar como uma ponte de ligação entre o nginx e o Django através do gunicorn.

4 - Dentro do **Django** a requisição recebida pelo **web server** é mapeado para uma view especifica através das urls, essa view pode ser tanto de aplicações do projeto Dr. Down como aplicações externas, elas pedem dados as modelos, as modelos do Dr. Down fazem uma requisição ao **redis** que pega os dados do banco de dados **postgresql** e retorna a view, a view seleciona o template e fornece os dados, com isso o template é preenchido e devolvido a view, que devolve o template como resposta ao web server.

5 - O web server (nginx) retorna a resposta para o web client (navegador)

## 3:  Requisitos e Restrições Arquiteturais

### 3.1 Dr. Down

Linguagem: Python 3.6.4

Framework: Django 2.0.3

Plataforma: Web - Navegadores Google Chrome, Safari e Firefox

Segurança: O sistema terá informações pessoais dos pacientes que só poderão ser vistas pelo mesmo ou pelo(s) seu(s) respectivo(s) médico(s). Outros dados pessoais só poderão ser vistos pelo próprio usuário.

Internacionalização (i18n):	A aplicação terá suporte aos idiomas: Inglês e Português do Brasil (sendo esta a linguagem padrão).

### 3.2 Docker e Compose

Docker versão: 1.13.1

Docker Compose versão: 1.8.0

## 4:	Visão Lógica

### 4.1	Visão Geral: Pacotes e Camadas

O framework Django organiza os projetos em apps, que são pastas que contém uma funcionalidade independente do restante da aplicação. Além disso, existem arquivos de configuração e arquivos estáticos globais. A figura a seguir mostra a organização de pastas de um app.

![Diagrama de Pacotes](http://uploaddeimagens.com.br/images/001/350/330/full/DP.png?1522284479)

## 5:	Visão de Implementação

### 5.1  Class-Based Views

Proporcionam um método alternativo para implementar views como objetos ao invés de funções. As Class-Based Views (CBV) são classes que implementam métodos e atributos que são comumente utilizados na programação das views. Dessa maneira, o programador pode utilizar métodos já implementados ou sobrescrevê-los e implementá-los da sua maneira. Para atender os mais variados casos de uso das views, as CBV oferecem diversos temas para implementação.

Podemos então agregar as funções básicas das views dentro de classes como métodos. E o recurso das Class Based Views está em algumas classes que já estão “pré-prontas” e que outras classes podem herdar. A partir daí as alterações que precisam ser feitas são mínimas!

### 5.2 Diagrama de Classes

![Diagrama de Classes](http://uploaddeimagens.com.br/images/001/352/613/original/DC2.jpeg?1522444895)

### 5.3 Modelo Entidade Relacionamento (MER)

### USER:

| Atributo | Tipo |Característica | Descrição |
|---|---|---|---|
| Name | CharField[100] | Obrigatório | Nome completo do usuário |
| Email | CharField[50] | Obrigatório, único | Email será usado como username do usuário |
| Telephone| CharField | Obrigatório | Telefone do usuário |
| Photo | Image | Opcional | Foto do usuário |
| Is_active | Boolean | Obrigatório | Verifica se o usuário está ativo no sistema |
| Is_superuser | Boolean | Obrigatório | Verifica se o usuário é um super administrador |
| Last_login | DateField | Automático | Último momento que o usuário logou |
| Created_at | DateField | Automático | Data de criação da conta |
| Updated_at | DateField | Automático | Data de modificação das informações da conta |
| Password | CharField[50] | Obrigatório | Senha do usuário |
| Is_staff | Boolean | Obrigatório | Verifica se o usuário é um funcionário |

### EMPLOYEE:

| Atributo | Tipo | Característica | Descrição |
|---|---|---|---|
| CPF | CharField | Obrigatório, único, validado | CPF do funcionário |
| Departament | CharField[30] | Obrigatório | Departamento do funcionário |

### PARENT:

| Atributo | Tipo | Característica | Descrição |
|---|---|---|---|
| CPF | CharField | Obrigatório, único, validado | CPF do parente |

### PATIENT:

| Atributo | Tipo | Característica | Descrição |
|---|---|---|---|
| Priority | IntergerField | Obrigatório | Grau de urgência para atendimento do paciente |
| SES | CharField[9] | Obrigatório, único, validado | Número SES do paciente |
| mother_name | CharField[80] | Obrigatório | Nome da mãe |
| father_name | CharField[80] | Obrigatório | Nome da pai |
| ethnicity | IntegerField | Obrigatório | Etnia |
| sus_number | CharField[15] | Obrigatório | número do SUS |
| civil_registry_of_birth | CharField | Obrigatório | Registro civil de nascimento |
| declaration_of_live_birth | CharField | Obrigatorio | Declaração de nascimento |


### Health Team:

| Atributo | Tipo | Característica| Descrição |
|---|---|---|---|
| CRM | CharField | Obrigatório, único, validado | Número CRM do médicos |
| Specialty | CharField[20] | Obrigatório | Especialidade |
| CPF | CharField | Obrigatório, único, validado | CPF do médicos |

### ADDRESS:

| Atributo | Tipo | Característica| Descrição |
|---|---|---|---|
| City | CharField[40] | Obrigatório | Cidade |
| CEP | CharFieldField | Obrigatório | CEP |
| Number |  CharField | Obrigatório | Numero da moradia|
| UF | CharField[2] | Obrigatório | Unidade da Federação |
| neighborhood | CharField[30] | Opcional | Bairro |

### POST:

| Atributo | Tipo | Característica | Descrição |
|---|---|---|---|
| Title |CharField[100] | Obrigatório | Título do post |
| Message | TextField | Obrigatório | Mensagem do post |
| Created_at | DateField | Automático | Data de criação do post |
| Updated_at | DateField | Automático | Data de modificação do post |

### MEDICAL QUESTIONARY:

| Atributo | Tipo | Característica | Descrição |
|---|---|---|---|
| Psychosocial_risk | IntergerField | Obrigatório | Risco psicossocial |
| Health_risk |IntergerField | Obrigatório | Risco de vida |
| Family_risk | IntergerField | Obrigatorio | Risco familiar |
| Total_risk | IntergerField | Opcional | Risco total |

### QUEUE:

| Atributo | Tipo | Característica | Descrição |
|---|---|---|---|
| Speciality | CharField[50] | Obrigatório | Especialidade |
| Time_left | DateField | Automático | Tempo faltando |
| Position | IntergerField | Automático | Posição |

### EVENTS:

| Atributo | Tipo | Característica| Descrição |
|---|---|---|---|
| Name | CharField[100] | Obrigatório |Nome do evento |
| Date | DateField | Obrigatório | Data do evento |
| Address | Address | Obrigatório | Endereço do evento |
| Description | TextField | Obrigatório | Descrição do evento |

### APPOINTMENTS:

| Atributo | Tipo | Característica | Descrição |
|---|---|---|---|
| Name | CharField[100] | Obrigatório | Nome do compromisso |
| Date | DateField | Obrigatório | Data do compromisso |
| Description | TextField | Opcional | Descrição do compromisso |

### Categoty:

| Atributo | Tipo | Característica | Descrição |
|---|---|---|---|
| name | CharField[100] | Obrigatório | Nome da categoria |
| Description | TextField | Obrigatório | Assunto da categoria |
| Slug | SlugField | Obrigatorio | Usado para inserir URLs renomeadas |

### Commentary:

| Atributo | Tipo | Característica | Descrição |
|---|---|---|---|
| Message | TextField | Obrigatório | Mensagem do comentário |
| Created_at | DateField | Automático | Data de criação do comentário |
| Updated_at | DateField | Automático | Data de modificação do comentário |



### RELACIONAMENTOS:

#### 1 - APPOINTMENTS tem USERS (Doctor):

Um médico pode ter uma ou várias consultas e uma consulta pertence a um único médico.

Cardinalidade: 1 X N

#### 2 - APPOINTMENTS tem USERS (pacientes):

Um paciente pode ter uma ou várias consultas e uma consulta pertence a um único paciente.

Cardinalidade: 1 X N

#### 3 - MEDICAL RECORDS tem USERS (pacientes):

Um prontuário pertence a um único paciente, mas uma paciente pode conter um ou vários prontuários.

Cardinalidade: 1 X N

#### 4 - USER (médico) tem USERS (pacientes):

Um médicos pode ter um ou vários pacientes, e  um paciente pode ter um ou vários médicos.

Cardinalidade: N X M

#### 5 - POST pertence a USER:

Um usuário pode ter um ou vários Posts, e um post pertence a um único usuário.

Cardinalidade:  1 X N

#### 6 - POST tem COMMENTARIES:

Um comentário pode conter um único post, e um post pode conter vários comentrios.

Cardinalidade: 1 X N

#### 7 - CLINIC possui ADDRESS:

Um endereço pode pertecer a apenas uma clinica, e uma clinica pode ter apenas um endereço.

Cardinalidade: 1 X 1

### 8 - EVENTS possui ADDRESS:

Um evento pode ter apenas um endereço, e um endereço pode ter apenas um evento.

Cardinalidade: 1 X 1


#### 9 - CATEGORIES tem POSTS:

Um post pode conter uma única categoria, e uma categoria pode conter vários posts.

Cardinalidade: 1 X N

## Referências

ARTEFATO: DOCUMENTO DE ARQUITETURA DE SOFTWARE. FUNPAR. Disponível em: <http://www.funpar.ufpr.br:8080/rup/process/artifact/ar_sadoc.htm>. Acesso em: 24 Mar. 2018.

ARQUITETURA BASEADA EM COMPONENTES. Disponível em: <https://marcobaccaro.wordpress.com/2010/10/05/arquitetura-baseada-em-componentes/>. Acessado em: 10 Abril. 2018.

CLASS-BASED VIEWS. DJANGO PROJECT. Disponível em: <https://docs.djangoproject.com/en/2.0/topics/class-based-views/>. Acesso em: 28 Mar. 2018.

DESMISTIFICANDO O CONCEITO DE DJANGO APPS. Disponível em: <http://henriquebastos.net/desmistificando-o-conceito-de-django-apps/>. Acesso em: 10 abril. 2018

PADRÕES ARQUITETURAIS MVC X ARQUITETURA DO DJANGO. GITHUB. Dispesclareceronível em: <https://github.com/fga-gpp-mds/A-Disciplina/wiki/Padr%C3%B5es-Arquiteturais---MVC-X-Arquitetura-do-Django>. Acesso em: 26 Mar. 2018.

POSTGRESQL. Disponível em: <https://www.postgresql.org/about/>. Acesso em: 03 abril. 2018

REDIS O QUE É E PARA QUE SERVE. Disponível em: <https://pt.linkedin.com/pulse/redis-o-que-%C3%A9-e-para-serve-romulo-cianci>. Acesso em: 03 Abril. 2018.

TAREFAS ASSINCRONAS COM DJANGO E CELERY. Disponível em: <https://fernandofreitasalves.com/tarefas-assincronas-com-django-e-celery/>. Acesso em: 03 Abril. 2018.

THE MODEL-VIEW-CONTROLLER DESIGN PATTERN. THE DJANGO BOOK. Disponível em: <https://djangobook.com/model-view-controller-design-pattern/>. Acesso em: 26 Mar. 2018.
