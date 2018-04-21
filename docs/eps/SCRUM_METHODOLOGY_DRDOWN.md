# Introdução

Este documento tem como objetivo deixar transparente o processo Ágil utilizado pelo Time Scrum do projeto Dr. Down, descrevendo informações como papéis existentes e ritos do Scrum adotados.

# Papéis na Equipe

Esta sessão lista todos os papéis existentes dentro do Time Scrum do projeto Dr. Down, suas atribuições e as pessoas que os estão exercendo.

## Product Owner

- Atribuições:

  - Responsável pelo gerenciamento do Backlog do Produto e por garantir o valor do trabalho realizado pelo Time;
 - Manter o Backlog do Produto e garante que ele está visível para todos;
 - Informar a todos quais itens têm a maior prioridade, de forma que todos sabem em que se irá trabalhar;
 - Definir e priorizar os itens do Backlog do Produto;
 - Vender o produto;
 - Intermediário(ligação) entre o cliente e a equipe;
 - Valor de negócio;
 - Visão de negócio;
 - Negociar com o time e com o cliente;
 - Canvas.


## Arquiteto de Software

- Atribuição:

  - determinar qual a arquitetura de software deverá ser utilizada nas diversas partes do projeto, levando em conta as especificidades deste e os requisitos exigidos
  - certificar-se de que a arquitetura definida está clara e sendo obedecida pelos demais membros do Time Scrum

## DevOps

- Atribuição:

  - garantir a integração continua
  - garantir o deploy continuo
  - facilitar o processo de desenvolvimento
  - organizar os diversos pipeline do produto de software 

## Scrum Master

- Atribuições:

  - ajudar todos do Time Scrum a entenderem a teoria, prática, regras e valores do Scrum
  - servir ao Product Owner, auxiliando de diversas formas, tais como:
    - gerir de maneira eficiente o Backlog do produto
    - fazer todos do Time Scrum entenderem ao máximo os ítens do Backlog do Produto
  - servir a equipe, auxiliando de diversas formas, tais como:
    - remover impedimentos ao progresso de todos da equipe.
    - instrui-lo em auto-organização e a serem multifuncionais
  - documentar cada Sprint
  - determinar e analisar as métricas e indicadores utilizados para acompanhar o progresso de toda a equipe

## Desenvolvedores

- Atribuições:

  - entregar os ítens contidos no Backlog da Sprint ao final de cada Sprint
  - determinar como farão para entregar os ítens do Backlog da Sprint (auto-organização)

# Ritos do Scrum

Abaixo ritos do Scrum que serão realizados pelo Time Scrum do projeto Dr. Down. Para cada rito está descrito seus objetivos, o tempo máximo de realização deles (entre colchetes [ ] ) e os dias e horários em que ocorrerão.

## Sprint

- objetivo:

  - atingir o objetivo para a Sprint definido no Planejamento da Sprint, assim como entregar todos os ítens do Backlog da Sprint

- time box:
  - sábado à sexta [1 semana]

## Planejamento da Sprint

- Reunião realizada com o Time Scrum no início de cada Sprint que tem como objetivo:

  - determinar o que poderá ser entregue na Sprint que se inicia (criação do Backlog da Sprint)

    - isso deve ser negociado entre o Product Owner e restante da equipe, respeitando a capacidade projetada e a performance passada deste

  - estimar o esforço necessário para entregar as histórias do backlog, através da pontuação delas usando o _planning poker_:
    - antes do início da pontuação de cada história, o Product Owner deve explicá-la e tirar as dúvidas da equipe, para que todos possam ter uma melhor base para a pontuação
    - cada participante vota, dando os pontos que acham que aquela história vale, tendo como base quantas horas eles imaginam que serão necessárias para completá-la. O voto de todas as pessoas só é revelado quando todos tiverem decidido quantos pontos darão para a história
      - a pontuação dada para cada história deve estar dentro da sequência de Fibonacci, sendo a menor pontuação válida 1
      - este passo é repetido até que haja consenso de todos os presentes sobre quantos pontos a história em questão vale
    - a equipe passa a pontuar a próxima história, até que todas estejam pontuadas

  - determinar como a equipe irá se organizar para que haja a entrega prevista para a Sprint

- time box:
  - sábado: 11:00 [2h]

## Daily Meeting

- Reunião diária do Time Scrum que tem como objetivo:

  - cada membro responder as 3 perguntas abaixo, sobre sua participação no andamento da Sprint:

    - O que foi feito pelo membro no dia anterior para ajudar a desenvolver na Sprint?
    - O que será feito pelo membro no dia atual para ajudar no desenvolvimento na Sprint?
    - Houve algum empedimento para o membro que impossibilitou ele ajudar o restante da equipe na Sprint? (gerenciamento de riscos)

- time box:

  - Dailys presenciais:

    - terça e quinta, 9:45 [15 min]
    - sábado: depois do Planejamento da Sprint [15 min]

  - Dailys online:

    - segunda, quarta e sexta, começando às 8:00

## Review da Sprint

- objetivo:

  - revisar como foi a Sprint, com foco no Backlog do Produto e no da Sprint

    - o que foi feito e o que ficou como débito (Product Owner)
    - atualização do Backlog do Produto (Product Owner)
    - problemas relacionados ao Backlog da Sprint e se/como foram resolvidos (toda a equipe)

- time box:

  - sábado, início da reunião [1h]

- **IMPORTANTE**: um item do Backlog da Sprint **só será aceito como feito** se:

  - estiver terminado
  - estiver coberto, no mínimo, por **teste unitário e/ou de integração**
    - exceto em caso de documentação ou outros tipos de histórias que não puderem ser testadas
  - tiver sido feito o **pull request** para a branch develop ou master e este ser **aceito** pelos revisores
  - a funcionalidade entregue ser aceita pelo Product Owner, de acordo com os critérios de aceitação especificados na história

## Retrospectiva da Sprint

- objetivo:

  - levantar como foi a Sprint, do ponto de vista das pessoas, relacionamentos, processos e ferramentas (pontos positivos e negativos)
  - identificar potenciais melhorias
  - identificar melhorias para colocar em prática na próxima Sprint

- time box:

  - sábado, logo após o review [1h]
