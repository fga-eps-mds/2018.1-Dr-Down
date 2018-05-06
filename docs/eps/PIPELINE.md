# Pipeline CI/CD

| Data | Versão | Descrição | Autor |
|:----:|:------:|:---------:|:-----:|
|06/05/2018|0.0.1|Versão inicial do documento do pipeline|João Pedro Sconetto e Mariana Mendes|

## Processos de DevOps

### Padrão de _Commit_

#### Por questões de padronização recomendamos que sigam nosso estilo de _commit_:

* Os _commits_ devem ser todos em __inglês__;

* Ele deve conter um título curto e objetivo do que foi feito naquele _commit_;

* Após esse título, deve-se descrever, com um pouco mais de detalhes, todas as atividades executadas.

* Caso esteja trabalhando em com algum associado assine nos seus _commits_ os seus parceiros

__Exemplo:__

    Creating project community files (Título curto e objetivo)

    Adds project license (Descrição de uma das atividades)

    Adds project code of conduct file

    Adds project contributing file

    Adds project issue template file

    Adds projects pull request file

    Co-authored-by: John Doe <john@email.com> (Assinatura de parceria)

### Política de _Branchs_

Tendo como meta manter a integralidade e confiabilidade do código do projeto foi proposta a utilização de política de branches.
Essa Política de Branches deverá guiar os desenvolvedores na forma de organização de suas contribuições ao repositório.
__OBS__: A política de _branchs_ foi idealizada para trabalhar em conjunto com a ferramenta do _git flow_, sua documentação e mais informações podem ser acessadas [aqui](https://github.com/nvie/gitflow).

* __master__ - Branch principal do repositório onde será permitida somente a integração de software consolidado e testado. Essa branch será exclusiva para a entrega de Realeases, ou seja, um conjunto maior de funcionalidades que integram o software, aqui estará a versão _**stable**_ do software.

* __develop__ - Branch para integração de novas funcionalidades, onde será permitido a entrega das features desenvolvidas e que estão em um estágio avançado de completude. Será o branch base para o início do desenvolvimento das features e da correção de bugs. Aqui também serão _mergeadas_ as releases.

* __feature/<nome-da-feature>__ - Branch utilizada para o desenvolvimento de novas features do _backlog_. Caso a feature tenha sida proposta por uma _issue_ do repositório e aceita no _backlog_ o nome deverá conter o número da _issue_.
Ex: feature/1-<nome-da-nova-feature> (Considerando que a feature tenha sido solicitada na _issue_ #1)

* __bugfix/<nome-do-bug>__ - Branch utilizada para corrigir bugs de baixa/média urgência e que não estão presentes na branch __master__. Caso o bug tenha sido reportado por uma _issue_ do repositório o nome deverá conter o número da _issue_.
 Ex: bugfix/1-<descrição-do-bug> (Considerando que o bug tenha sido reportado na _issue_ #1)

* __hotfix/<nome-do-bug>__ - Branch utilizada para corrigir bugs de alta urgência e que estão presentes na branch __master__. Caso o bug tenha sido reportado por uma _issue_ do repositório o nome deverá conter o número da _issue_.
 Ex: bugfix/1-<descrição-do-bug> (Considerando que o bug tenha sido reportado na _issue_ #1)

* __release/<versão-da-release>__ - Branch onde será feito os ajustes finais/build antes da entrega de uma versão do produto de software. Constará no nome da branch a versão da release a ser entregue.

* __support/<tema-ou-natureza>__ - Branch onde serão executadas tarefas de suporte relacionadas ao software, como elaboração de documentações, correções de natureza de gerência de configuração e etc.
