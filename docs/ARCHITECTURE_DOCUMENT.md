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

## 1: Introdução

### 1.1	Finalidade

Este documento tem como finalidade apresentar uma visão geral da arquitetura que será usada no desenvolvimento do projeto Dr. Down e permitir um maior entendimento do sistema e de como ele irá se comportar. Com o maior detalhamento da arquitetura, espera-se deixar explícitas as decisões arquiteturais feitas pela equipe de desenvolvimento em conjunto com os gestores do projeto para o desenvolvimento do software.

### 1.2	Escopo

Dr. Down será uma ferramenta desenvolvida para gerenciar, auxiliar e facilitar a administração do fluxo de pacientes do CRIS DOWN, além de possibilitar a comunicação entre médicos, pacientes e familiares. O documento apresentará toda a parte arquitetural para a confecção do software Dr. Down, a fim de tornar claras as características arquiteturais do projeto.

### 1.3	Definições, acrônimos e abreviações

| Abreviação | Definição |
| --------         | ------         |
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

O Dr.Down será uma aplicação web desenvolvida a partir do framework Django, o qual é escrito em Python. A arquitetura utilizada pelo Django é a MVT (Model, View e Template), que é derivada da arquitetura MVC (Model, View e Controller). De acordo com o DjangoBook, a parte de controller, em Django, é tratada pelo próprio framework. Portanto a View do MVT desempenha um papel próximo, mas não igual ao controller.
 A arquitetura MVT faz uso do design responsivo, onde o site se adapta ao browser do usuário, acessando os dados do sistema Dr.Down a partir do navegador do usuário. Quando os usuários acessam o site, eles entram em contato com a view, que faz uma requisição ao sistema, e executa as ações definidas.

### 2.1 Model

É uma representação do banco de dados. Além disso, também inclui características, relações e outros comportamentos que os dados podem assumir.
Para adicionar os valores no banco, é necessário apenas definí-los de acordo com suas variáveis correspondentes e o Django, comunica-se com o banco de forma inteligente.

### 2.2 View

Estabelece uma ponte entre a Models e o Templates. Recebe as requisições do usuário a partir do template, acessa o banco de dados e então retorna a informação solicitada pelo usuário, como: HTML, XML e os erros encontrados.

### 2.3 Template

Agrega toda a parte visual que estará visível para os usuários. Inclui os códigos HTML, CSS, javascript, entre outras linguagens que são utilizadas na apresentação da View ao usuário.

## 3:  Organização Arquitetural

### 3.1  Class-Based Views

Proporcionam um método alternativo para implementar views como objetos ao invés de funções. As Class-Based Views (CBV) são classes que implementam métodos e atributos que são comumente utilizados na programação das views. Dessa maneira, o programador pode utilizar métodos já implementados ou sobrescrevê-los e implementá-los da sua maneira. Para atender os mais variados casos de uso das views, as CBV oferecem diversos temas para implementação.

## 4:  Requisitos e Restrições Arquiteturais

Linguagem: Python 3.6.4

Framework: Django  2.0.3

Plataforma: Web - Navegadores Google Chrome, Safari e Firefox

Segurança: O sistema terá informações pessoais dos pacientes que só poderão ser vistas pelo mesmo ou pelo(s) seu(s) respectivo(s) médico(s). Outros dados pessoais só poderão ser vistos pelo  usuário a quem esses dados se referem.

Internacionalização (i18n):	A aplicação terá suporte aos idiomas: Inglês e Português do Brasil (sendo esta a linguagem padrão).

## 5:	Visão Lógica

### 5.1	Visão Geral: Pacotes e Camadas

O framework Django organiza os projetos em apps, que são pastas que contém uma funcionalidade independente do restante da aplicação. Além disso, existem arquivos de configuração e arquivos estáticos globais. A figura a seguir mostra a organização de pastas de um app.

## 6:	Visão de Implementação

### 6.1 Diagrama de Pacotes

![Diagrama de Pacotes](http://uploaddeimagens.com.br/images/001/350/330/full/DP.png?1522284479)

### 6.2 Diagrama de Classes

![Diagrama de Classes](http://uploaddeimagens.com.br/images/001/350/293/full/DC.png?1522283843)

### 6.3 Modelo Entidade Relacionamento (MER)

### USER:

| Atributo | Tipo |para Característica | Descrição |
|  ---  |  ---  |  ---  |  ---  |
| name | string[100] | obrigatório | Nome completo do usuário |
| email | string[50] | obrigatório, único | Email será usado como username do usuário |
| telephone| string[14] | obrigatório | Telefone do usuário |
| photo | image | opcional | Foto do usuário |
| is_active | boolean | obrigatório | Verifica se o usuário está ativo no sistema |
| is_superuse | boolean | obrigatório | Verifica se o usuário é um super administrador |
| last_login | date | automático | Último momento que o usuário logou |
| created_at | date | automático | Data de criação da conta |
| updated_at | date | automático | Data de modificação das informações da conta |
| password | string[50] | obrigatório | Senha do usuário |
| is_staff | boolean | obrigatório | Verifica se o usuário é um funcionário |

### EMPLOYEE:

| Atributo | Tipo | Característica | Descrição |
|  ---  |  ---  |  ---  |  ---  |
| cpf | string[25] | obrigatório, único, validado | CPF do funcionário |
| departament | string[30] | obrigatório | Departamento do funcionário |

### PARENT:

| Atributo | Tipo | Característica | Descrição |
|  ---  |  ---  |  ---  |  ---  |
| cpf | string[25] | obrigatório, único, validado | CPF do parente |

### PATIENT:

| Atributo | Tipo | Característica | Descrição |
|  ---  |  ---  |  ---  |  ---  |
| urgency | integer | obrigatório | Grau de urgência para atendimento do paciente |
| ses | integer | obrigatório, único, validado | Número SES do paciente |

### DOCTOR:

| Atributo | Tipo | Característica| Descrição |
|----|------|-------|--------|
| CRM | Integer | Obrigatório, único | Número CRM do doutor |
| specialty | String[20] | Obrigatório | Especialidade |
| CPF | String[25] | Obrigatório, único, validado | CPF do doutor |

### POST:

| Atributo | Tipo | Característica | Descrição |
|--|--|--|--|
| title |string[100] | obrigatório | Título do post |
| description | text | obrigatório | Descrição do post |
| author | user | obrigatório | Nome do autor do post |
| created_at | date | automático | Data de criação do post |
| _at | date | automático | Data de modificação do post |
| updated_by | user | obrigatório | Usuário que modificou o post |
|slug | SlugField | obrigatório | Usado para inserir URLs nomeadas |

### MEDICAL QUESTIONARY:

| Atributo | Tipo | Característica | Descrição |
|--|---|--|--|
| psychosocial_risk | integer | obrigatório | Risco psicossocial
| health_risk |integer | obrigatório | Risco de vida |
| family_risk | integer | obrigatorio | Risco familiar |
| total_risk | integer | opcional | Risco total |

### QUEUE:

| Atributo | Tipo | Característica | Descrição |
|--|----|----|--|
| speciality | string[50] | obrigatório | Especialidade |
| time_left | dateTimeField | automático | Tempo faltando |
| position | integer | automático | Posição |

### EVENTS:

| Atributo | Tipo | Característica| Descrição |
|---|----|---|---|
| name | string[100] | obrigatório |Nome do evento |
| date | dateTime | obrigatório | Data do evento |
| address | string[60] | obrigatório | Endereço do evento |
| description | text | obrigatório | Descrição do evento |

### APPOINTMENTS:

| Atributo | Tipo | Característica | Descrição |
|  ---  |  ---  |  ---  |  ---  |
| name | string[100] | obrigatório | Nome do compromisso |
| date | date/time | obrigatório | Data do compromisso |
| description | text | opcional | Descrição do compromisso |

### TOPIC:

| Atributo | Tipo | Característica | Descrição |
|  ---  |  ---  |  ---  |  ---  |
| title | string[100] | obrigatório | Título do tópico |
| subject | text | obrigatório | Assunto do tópico |
| last_update | date/time | automático | Último data atualizada |
| slug | SlugField | string | Usado para inserir URLs renomeadas |

### RELACIONAMENTOS:

#### 1 - APPOINTMENTS tem USERS (Doctor)

Um doutor pode ter uma ou várias consultas, mas toda consulta tem um médico.
Cardinalidade: 1 X N

#### 2 - APPOINTMENTS tem USERS (pacientes)

Um paciente pode ter várias consultas, mas toda consulta tem um paciente.
Cardinalidade: 1 X N


#### 3 - MEDICAL RECORDS tem USERS (pacientes):

Um prontuário pertence a um paciente e um paciente tem um prontuário.
Cardinalidade: 1 X 1

#### 4 - USER (Doutor) tem USERS (pacientes):

Um doutor tem um ou vários pacientes, e um paciente pode ter um ou vários doutores.
Cardinalidade: N X M

#### 5 - POST pertence a USER

Um usuário pode ter um ou vários Posts, mas um post pertence a um único usuário.
Cardinalidade:  1 X N

#### 6 - POST tem TOPICS

Um post pode ter vários tópicos e um tópico pode ter vários posts.
Cardinalidade: M X N
