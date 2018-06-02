# Pipeline CI/CD

## Histórico de Revisões
|Data|Versão|Descrição|Autor|
| --- | --- | --- | --- |
|06/05/2018|0.0.1|Versão inicial do documento do pipeline|João Pedro Sconetto e Mariana Mendes|

## Processos de DevOps
O presente documento visa esclarecer e registrar todos os processos, a cultura implementada e os padrões que foram utilizados no projeto __Dr. Down__ no viés das práticas de DevOps, a fim de unificar o desenvolvimento e as operações inerentes do projeto supracitado.

O documento se divide em duas partes:

* Integração Contínua (CI - _Continuous Integration_)

* Deploy Contínuo (CD - _Continuous Deploy_)

No qual a primeira parte irá mostrar as técnicas e itens aplicados ao projeto no propósito de, como o nome da técnica diz, integrar continuamente o trabalho desenvolvido pela equipe. A segunda parte irá mostrar as técnicas e itens aplicados ao projeto com o objetivo de fazer a implantação contínua do projeto na infraestrutura utilizada pela equipe, de forma automatizada.

### Integração Contínua:

#### Padrão de _Commit_

##### Por questões de padronização documentamos o seguinte estilo de _commit_:

* Os _commits_ devem ser todos em __inglês__;

* Ele deve conter um título curto e objetivo do que foi feito naquele _commit_;

* Após esse título, deve-se descrever, com um pouco mais de detalhes, todas as atividades executadas.

* Caso esteja trabalhando com algum associado assine nos seus _commits_ os seus parceiros

__Exemplo:__

    Creating project community files (Título curto e objetivo)

    Adds project license (Descrição de uma das atividades)

    Adds project code of conduct file

    Adds project contributing file

    Adds project issue template file

    Adds projects pull request file

    Co-authored-by: John Doe <john@email.com> (Assinatura de parceria)

#### Política de _Branchs_

Tendo como meta manter a integralidade e confiabilidade do código do projeto, foi proposta a utilização de política de branches.
Essa Política de Branches deverá guiar os desenvolvedores na forma de organização de suas contribuições ao projeto.

__OBS__: A política de _branchs_ foi idealizada para trabalhar em conjunto com a ferramenta do _git flow_, sua documentação e mais informações podem ser acessadas [aqui](https://github.com/nvie/gitflow).

* __master__ - Branch principal do repositório, onde será permitida somente a integração de software consolidado e testado. Essa branch será exclusiva para a entrega de Releases, ou seja, um conjunto maior de funcionalidades que integram o software. Aqui estará a versão _**stable**_ do software.

* __develop__ - Branch para integração de novas funcionalidades, onde será permitido a entrega das features desenvolvidas e que estão em um estágio avançado de completude. Será a branch base para o início do desenvolvimento das features e da correção de bugs. Aqui também serão _mergeadas_ as releases.  

* __feature/<nome-da-feature>__ - Branch utilizada para o desenvolvimento de novas features do _backlog_. Caso a feature tenha sida proposta por uma _issue_ do repositório e aceita no _backlog_ o nome deverá conter o número da _issue_.
Ex: feature/1-<nome-da-nova-feature> (Considerando que a feature tenha sido solicitada na _issue_ #1)

* __bugfix/<nome-do-bug>__ - Branch utilizada para corrigir bugs de baixa/média urgência e que não estão presentes na branch __master__. Caso o bug tenha sido reportado por uma _issue_ do repositório o nome deverá conter o número da _issue_.
 Ex: bugfix/1-<descrição-do-bug> (Considerando que o bug tenha sido reportado na _issue_ #1)

* __hotfix/<nome-do-bug>__ - Branch utilizada para corrigir bugs de alta urgência e que estão presentes na branch __master__. Caso o bug tenha sido reportado por uma _issue_ do repositório o nome deverá conter o número da _issue_.
 Ex: bugfix/1-<descrição-do-bug> (Considerando que o bug tenha sido reportado na _issue_ #1)

* __release/<versão-da-release>__ - Branch onde será feito os ajustes finais/build antes da entrega de uma versão do produto de software. Constará no nome da branch a versão da release a ser entregue.

* __support/<tema-ou-natureza>__ - Branch onde serão executadas tarefas de suporte relacionadas ao software, como elaboração de documentações, correções de natureza de gerência de configuração e etc.

#### Testes e Estilo de Código

Com o objetivo de garantir a qualidade de código, assim como a sua manutenibilidade, a equipe definiu técnicas e padrões a serem seguidos, quanto ao estilo de código foi definido uma folha de estilo que é considerada a padrão por programadores Python, se trata da [PEP8](https://www.python.org/dev/peps/pep-0008/). Com isto é possível verificar, com o auxílio da ferramenta Code Climate o quão manutenível é o código que está sendo feito.

Em complemento ao estilo do código a equipe acordou em manter todo o código testado, pois com a união das duas técnicas é possível assegurar uma maior qualidade de código. Para isso foram usados técnicas padrões de teste do Python/Django, com o auxílio do [Coverage.py](https://coverage.readthedocs.io/en/coverage-4.5.1/) e do [pytest](https://docs.pytest.org/en/latest/), estes que, também, servem de _input_ para o Code Climate analisar a manutenibilidade do software.

Ficou acordado entre os membros da equipe que a cobertura de teste deveria ser igual ou superior a 90% em todos os momentos do projeto.

#### _Pull Requests_

Ao término da execução da codificação é necessário a abertura de um _Pull Request_ no repositório oficial do software para que possa ser apreciado o código solução. Com isso as ferramentas de CI/CD automático irão executar a fase de _build_ e teste para verificar se etapa de teste e estilo de código foram implementadas corretamente. Caso não tenha dívidas nessa fase, cabe a dois membros da equipe de EPS (com foco no P.O. na análise) analisar o produto para verificar se atende os critérios de aceitação e se está de acordo com o que foi definido para ser entregue. Com todas as técnicas e fases entregues em conformidade, cabe aos membros aprovarem o _pull request_ para que o mesmo possa ser _mergeado_ em branchs de entregue de _feature_.

#### _Build_ e Testes

Com o auxílio de ferramentas de automatização essa fase é executada, via [Travis-CI](https://travis-ci.org/), a fim de garantir a fase de Teste e Estilo de Código. Com isso a ferramenta vai verificar o código, executar todos os testes para procurar erros na lógica do software e após tentar construir (_build_) os _containers_ da aplicação. Caso qualquer passo dessa fase tenha algum problema a ferramenta irá informar (via e-mail e via repositório) que algo está errado e é preciso correções antes de avançar no pipeline.

### Deploy Contínuo:

Com a execução de todos os passos da integração contínua a ferramenta de automatização irá executar os passos de deploy, caso não tenho encontrado nenhum erro, que seguem com o deploy/entrega da aplicação no ambiente de homologação e produção. Os passos executados são:

* Publica a última versão integrada na _branch_ no docker hub da aplicação;

* Acessa as máquinas de deploy (Hosts no Digital Ocean);

* Baixa a última versão do docker hub no host;

* Executa atualizações necessárias com as novas funcionalidades (migrações, modificações no banco, traduções e etc);

* Caso tenha algum problema a máquina envia um log para a ferramenta de logs (sentry.io). Caso contrário, o sistema mantém o funcionamento contínuamente.

### Pipeline v0.0.1

![pipeline](https://i.imgur.com/v3m6lQr.png)

#### Legenda

Primeiro Estágio:
* No primeiro estágio estão as culturas de política de _branches_, padrão de _commits_, estilo de código e testes, onde durante o desenvolvimento a equipe segue as culturas propostas até a publicação do código com as novas adições.

Segundo Estágio:
* Aqui o código publicado com as adições, chamada de versão, é alcançada pela ferramenta de CI, executado os testes (todos os implementados e os novos adicionados) e é feito a build, caso haja erro nesse estágio retorna-se ao primeiro fazendo as adições necessárias.

Terceiro Estágio:
* Aqui a nova versão está em um estágio estável do seu ciclo de vida, se todas as adições esperadas para esta versão estiverem prontas a equipe espera uma abertura de um novo _pull request_ solicitando a junção dessa versão com a versão atual do software. Nesta fase é feito a verificação manual da concordância das adições, tanto com os estágios anteriores quanto com as especificações de produto levantado pelo _Product Owner_, caso positivo o pipeline avança, do contrário retorna a estágios anteriores.

Quarto Estágio:
* Aqui com a nova versão aprovada e consolidada ela é direcionada para o ambiente o qual deve integrar (homologação ou produção) e a ferramenta de CI/CD faz o deploy e entrega automática dessas novas adições.


__OBS__: Os principais artefatos que estão inclusos no, e participam do, pipeline são: ```.travis.yml```, ```codeclimate.yml```, ```mkdocs-build.sh```, ```production-deploy.sh``` e ```staging-deploy.sh```, todos estão disponíveis no repositório da aplicação no [GitHub](https://github.com/fga-gpp-mds/2018.1-Dr-Down).

### Processo do Pipeline v0.0.1

A fim de tornar mais claro como ocorre o processo do CI/CD, assim como mostrar em detalhes como é feito o pipeline de integração, deploy e entrega contínua da ferramenta Dr. Down, foi desenhado, com auxílio da ferramenta [Bizagi](https://www.bizagi.com/pt), o processo com cada tarefa e como é executado cada estágio que foi descrito acima:

![processo](https://i.imgur.com/5mOnkbz.png)
