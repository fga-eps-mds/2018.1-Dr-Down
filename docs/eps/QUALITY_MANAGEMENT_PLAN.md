#Plano de gerênciamento de qualidade 

| Data | Versão | Descrição | Autor |
|:----:|:------:|:---------:|:-----:|
|03/04/2018|0.0.1|Primeira Versão do Plano de Qualidade|Mariana De Souza Mendes|

## Introdução

Este documento visa esclarecer entre os envolvidos no projeto _Dr. Down_ os critérios, ferramentas e o planejamento da qualidade do projeto.

"Qualidade de software é a conformidade com requisitos funcionais e de desempenho explicitamente declarados, padrões de desenvolvimento explicitamente documentados e características implícitas, que são esperadas em todo software desenvolvido profissionalmente" (PRESSMAN, 2002).

## Planejamento

Visando uma boa qualidade do projeto, alguns padrões de qualidade de corpos de conhecimentos e de normas foram definidos, tanto quanto as ferramentas que serão utilizadas para monitorar essa qualidade. 

### Métricas

Para a análise das métricas foram estabelecidos alguns critérios a serem seguidos. Quanto mais próximo do bom melhor.

|Métrica|Bom|Regular|Crítico|
|:-----:|---|-------|-------|
| Complexidade ciclomática | 0 a 20 | 21 a 60 | acima de 60 |
| Duplicação de código | 0% a 1.5% | 1,.6% a 2.9% | acima 3 %|
| Quebras no padrão de código/PEP 8 | 0 a 5 | 6 a 10 | acima de 11 |
| Cobertura de código	| acima de 95% | acima de 80% | abaixo de 75% |

### Monitoramento

O monitoramento da qualidade do projeto, além de garantir a entrega com qualidade desejada do produto, também garante um maior controle de um todo durante o seu desenvolvimento. Através do monitoramento, com o auxilio de ferramentas para isso, e medição de alguns aspectos podemos adequar os processos durante os tempo e assim conseguimos uma rastreabilidade melhor.

### Ferramentas

* [Code Climate](https://codeclimate.com/): O Code Climate permite que as organizações assumam o controle de sua qualidade de código, incorporando cobertura de teste totalmente configurável e dados de manutenção em todo o fluxo de trabalho de desenvolvimento.

* [ZenHub](https://www.zenhub.com/): ZenHub é uma ferramenta que auxilia no rastreio das issues do github e também criar gráficos como o "Velocity" e o "BurnDown".

* [Pytest](https://docs.pytest.org/en/latest/): O pytest é uma ferramenta de teste Python completa e madura que ajuda você a escrever programas melhores.



