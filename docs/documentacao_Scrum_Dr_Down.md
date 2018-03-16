# ÍNDICE

- [Introdução](#introducao)
- [Papéis na Equipe](#papeis-da-equipe)
  - [Product Owner](#product-owner)
  - [Arquiteto de Software](#arquiteto-de-software)
  - [DevOps](#devops)
  - [Scrum Master](#scrum-master)
  - [Time de Desenvolvimento](#time-de-desenvolvimento)
- [Ritos do Scrum](#ritos-do-scrum)
  - [Sprint](#sprint)
  - [Planejamento da Sprint](#planejamento-da-sprint)
  - [Daily Meeting](#daily-meeting)
  - [Review da Sprint](#review-da-sprint)
  - [Retrospectiva da Sprint](#retrospectiva-da-sprint)

----

## Introdução

Este documento tem como objetivo deixar transparente o processo Ágil utilizado pelo Time Scrum do projeto Dr. Down, descrevendo informações como papéis existentes e ritos do Scrum adotados.

----

## Papéis na Equipe

Esta sessão lista todos os papéis existentes dentro do Time Scrum do projeto Dr. Down, suas atribuições e as pessoas que os estão exercendo.

### Product Owner

- Atribuições:

  - definir claramente os ítens do Backlog do Produto
  - priorizar os ítens do Backlog do Produto
  - otimizar o valor do trabalho do Time de Desenvolvimento
  - mostrar ao Time de Desenvolvimento no que eles devem trabalhar a seguir
  - garantir que o Time de Desenvolvimento entenda os ítens do Backlog do Produto no nível necessário

- Responsável atual:
  - Mariana Mendes

### Arquiteto de Software

- Atribuição:

  - determinar qual a arquitetura de software deverá ser utilizada nas diversas partes do projeto, levando em conta as especificidades deste e os requisitos exigidos
  - certificar-se de que a arquitetura definida está clara e sendo obedecida pelos demais membros do Time Scrum

- Responsável atual:
  - Victor Arnaud

### DevOps

- Atribuição:

  - automatizar ao máximo e monitorar os processos envolvidos na construção e implementação do software produzido pelo projeto Dr. Down

- Responsável atual:
  - João Sconetto

### Scrum Master

- Atribuições:

  - ajudar todos do Time Scrum a entenderem a teoria, prática, regras e valores do Scrum
  - servir ao Product Owner, auxiliando de diversas formas, tais como:
    - gerir de maneira eficiente o Backlog do produto
    - fazer todos do Time Scrum entenderem ao máximo os ítens do Backlog do Produto
  - servir ao Time de Desenvolvimento, auxiliando de diversas formas, tais como:
    - remover impedimentos ao progresso do Time de Desenvolvimento
    - instrui-lo em auto-organização e a serem multifuncionais

- Responsável atual: 
  - Diego França

### Time de Desenvolvimento

- Atribuições:

  - entregar os ítens contidos no Backlog da Sprint ao final de cada Sprint
  - determinar como farão para entregar os ítens do Backlog da Sprint (auto-organização)

- Responsáveis atuais:
  - Daniel Maike
  - Elias Bernardo
  - Gabriela Medeiros
  - Geovana Ramos
  - Guilherme Guy
  - Joberth Rodrigues

----

## Ritos do Scrum

Abaixo ritos do Scrum que serão realizados pelo Time Scrum do projeto Dr. Down. Para cada rito está descrito seus objetivos, o tempo máximo de realização deles (entre colchetes [ ] ) e os dias e horários em que ocorrerão.

### Sprint

- objetivo:

  - atingir o objetivo para a Sprint definido no Planejamento da Sprint, assim como entregar todos os ítens do Backlog da Sprint

- time box:
  - sábado à sexta [1 semana]

### Planejamento da Sprint

- Reunião realizada com o Time Scrum no início de cada Sprint que tem como objetivo:

  - determinar o que poderá ser entregue na Sprint que se inicia (criação do Backlog da Sprint)

    - isso deve ser negociado entre o Product Owner e o Time de Desenvolvimento, respeitando a capacidade projetada e a performance passada deste

  - determinar como o Time de Desenvolvimento irá se organizar para que haja a entrega prevista para a Sprint

- time box:
  - sábado: 11:00 [2h]

### Daily Meeting

- Reunião diária do Time Scrum que tem como objetivo:

  - cada membro responder as 3 perguntas abaixo, sobre sua participação no andamento da Sprint:

    - O que foi feito pelo membro no dia anterior para ajudar o Time de Desenvolvimento na Sprint?
    - O que será feito pelo membro no dia atual para ajudar o Time de Desenvolvimento na Sprint?
    - Houve algum empedimento para o membro que impossibilitou ele ajudar o Time de Desenvolvimento na Sprint? (gerenciamento de riscos)

- time box:

  - Dailys presenciais:

    - terça e quinta, 9:45 [15 min]
    - sábado: depois do Planejamento da Sprint [15 min]

  - Dailys online:

    - segunda, quarta e sexta, começando às 8:00

### Review da Sprint

- objetivo:

  - revisar como foi a Sprint, com foco no Backlog do Produto e no da Sprint

    - o que foi feito e o que ficou como débito (Product Owner)
    - atualização do Backlog do Produto (Product Owner)
    - problemas relacionados ao Backlog da Sprint e se/como foram resolvidos (Time de Desenvolvimento)

- time box:

  - sábado, início da reunião [1h]

- **IMPORTANTE**: um item do Backlog da Sprint **só será aceito como feito** se:

  - estiver terminado
  - estiver coberto, no mínimo, por **teste unitário e/ou de integração**
    - exceto em caso de documentação ou outros tipos de histórias que não puderem ser testadas
  - tiver sido feito o **pull request** para a branch develop ou master e este ser **aceito**
  - for aceito pelo Product Owner

### Retrospectiva da Sprint

- objetivo:

  - levantar como foi a Sprint, do ponto de vista das pessoas, relacionamentos, processos e ferramentas (pontos positivos e negativos)
  - identificar potenciais melhorias
  - identificar melhorias para colocar em prática na próxima Sprint

- time box:

  - sábado, logo após o review [1h]
