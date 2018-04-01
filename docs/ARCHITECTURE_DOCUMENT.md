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

## 1: Introdução

### 1.1	Finalidade

Este documento tem como finalidade apresentar uma visão geral da arquitetura que será usada no desenvolvimento do projeto Dr. Down e permitir um maior entendimento do sistema e de como ele irá se comportar. Com o maior detalhamento da arquitetura, espera-se deixar explícitas as decisões arquiteturais feitas pela equipe de desenvolvimento em conjunto com os gestores do projeto para o desenvolvimento do software.

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

### 1.4 Referências

ARTEFATO: DOCUMENTO DE ARQUITETURA DE SOFTWARE. FUNPAR. Disponível em: <http://www.funpar.ufpr.br:8080/rup/process/artifact/ar_sadoc.htm>. Acesso em: 24 Mar. 2018.

PADRÕES ARQUITETURAIS MVC X ARQUITETURA DO DJANGO. GITHUB. Dispesclareceronível em: <https://github.com/fga-gpp-mds/A-Disciplina/wiki/Padr%C3%B5es-Arquiteturais---MVC-X-Arquitetura-do-Django>. Acesso em: 26 Mar. 2018.

THE MODEL-VIEW-CONTROLLER DESIGN PATTERN. THE DJANGO BOOK. Disponível em: <https://djangobook.com/model-view-controller-design-pattern/>. Acesso em: 26 Mar. 2018.

CLASS-BASED VIEWS. DJANGO PROJECT. Disponível em: <https://docs.djangoproject.com/en/2.0/topics/class-based-views/>. Acesso em: 28 Mar. 2018.

## 2: Representação Arquitetural

O Dr.Down será uma aplicação web desenvolvida a partir do framework Django, o qual é escrito em Python. O padrão arquitetural utilizado pelo Django é a MVT (Model, View e Template), que é derivada da do padrão arquitetural MVC (Model, View e Controller). De acordo com o DjangoBook, a parte de controller, em Django, é tratada pelo próprio framework. Portanto a View do MVT desempenha um papel próximo, mas não igual ao controller.

### 2.1 Model

É uma representação do banco de dados. Além disso, também inclui características, relações e outros comportamentos que os dados podem assumir.
O Django inclui varias ferramentas para automatizar tanto quanto possível o processo e a manipulação do banco de dados, de forma que o desenvolvedor não precise se preocupar tanto com o banco de dados, o que ajuda no foco do desenvolvimento da aplicação de forma mais rápida.

### 2.2 View

Estabelece uma ponte entre a Models e o Templates. Recebe as requisições do usuário a partir do template, acessa o banco de dados e então retorna a informação solicitada pelo usuário, por meio de HTML, XML e/ou os erros encontrados.

### 2.3 Template

Agrega toda a parte visual que estará visível para os usuários. Inclui os códigos HTML, CSS, javascript, entre outras linguagens que são utilizadas na apresentação da View ao usuário.

### 2.4 Diagrama arquitetural

![Diagrama arquitetural](http://uploaddeimagens.com.br/images/001/354/150/original/MICROSERVI%C3%87OS-COR.png?1522592161)


## 3:  Requisitos e Restrições Arquiteturais

Linguagem: Python 3.6.4

Framework: Django  2.0.3

Plataforma: Web - Navegadores Google Chrome, Safari e Firefox

Segurança: O sistema terá informações pessoais dos pacientes que só poderão ser vistas pelo mesmo ou pelo(s) seu(s) respectivo(s) médico(s). Outros dados pessoais só poderão ser vistos pelo próprio usuário.

Internacionalização (i18n):	A aplicação terá suporte aos idiomas: Inglês e Português do Brasil (sendo esta a linguagem padrão).

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
| Telephone| IntergerField | Obrigatório | Telefone do usuário |
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
| CPF | IntergerField | Obrigatório, único, validado | CPF do funcionário |
| Departament | CharField[30] | Obrigatório | Departamento do funcionário |

### PARENT:

| Atributo | Tipo | Característica | Descrição |
|---|---|---|---|
| CPF | IntergerField | Obrigatório, único, validado | CPF do parente |

### PATIENT:

| Atributo | Tipo | Característica | Descrição |
|---|---|---|---|
| Urgency | IntergerField | Obrigatório | Grau de urgência para atendimento do paciente |
| SES | IntergerField | Obrigatório, único, validado | Número SES do paciente |

### DOCTOR:

| Atributo | Tipo | Característica| Descrição |
|---|---|---|---|
| CRM | IntergerField | Obrigatório, único, validado | Número CRM do médicos |
| Specialty | CharField[20] | Obrigatório | Especialidade |
| CPF | IntergerField | Obrigatório, único, validado | CPF do médicos |

### ADDRESS:

| Atributo | Tipo | Característica| Descrição |
|---|---|---|---|
| City | CharField[40] | Obrigatório | Cidade |
| CEP | IntergerField | Obrigatório | CEP |
| Number |  IntergerField | Obrigatório | Numero da moradia|
| UF | CharField[2] | Obrigatório | Unidade da Federação |
| neighborhood | CharField[30] | Opcional | Bairro |

### POST:

| Atributo | Tipo | Característica | Descrição |
|---|---|---|---|
| Title |CharField[100] | Obrigatório | Título do post |
| Description | TextField | Obrigatório | Descrição do post |
| Author | User | Obrigatório | Nome do autor do post |
| Created_at | DateField | Automático | Data de criação do post |
| Updated_at | DateField | Automático | Data de modificação do post |
| Updated_by | User | Obrigatório | Usuário que modificou o post |
|Slug | SlugField | Obrigatório | Usado para inserir URLs nomeadas |

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

### TOPIC:

| Atributo | Tipo | Característica | Descrição |
|---|---|---|---|
| Title | CharField[100] | Obrigatório | Título do tópico |
| Subject | TextField | Obrigatório | Assunto do tópico |
| Last_update | DateField | Automático | Último data atualizada |
| Slug | SlugField | Obrigatorio | Usado para inserir URLs renomeadas |

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

#### 6 - POST tem TOPICS:

Um post pode conter um único tópico, e um tópico pode conter vários posts.

Cardinalidade: 1 X N

#### 7 - CLINIC possui ADDRESS:

Um endereço pode pertecer a apenas uma clinica, e uma clinica pode ter apenas um endereço.

Cardinalidade: 1 X 1

### 8 - EVENTS possui ADDRESS:

Um evento pode ter apenas um endereço, e um endereço pode ter apenas um evento.

Cardinalidade: 1 X 1
