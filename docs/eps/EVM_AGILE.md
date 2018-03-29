# EVM Agile - Dr. Down

## Histórico de Revisões
| Data | Versão | Descrição | Autores |
| --- | --- | --- | --- |
| 28/03/2018 | 0.0.1 | Criação do documento | João Pedro Sconetto |

## EVM Agile

O __EVM__ (_Earned Value Management_ ou Gerenciamento de Valor agregado) se trata de uma técnica da gestão tradicional de projetos que é usada para medir a saúde de um projeto. Essa técnica foi adaptada para projetos agéis a fim de auxiliar a equipe de gestão a verificar métricas e avaliar entregas em projetos que seguem esta metodologia, e que enfretam alguns problemas como:
- Escopo aberto;
- Falta de visibilidade em entregas e custos;
- e etc.

### Dados Fixos
| Identificador | Descrição | Valor |
| --- | --- | --- |
| BAC | Orçamento disponível para a primeira _release_ | R$ 34.039,38 |
| L | Tamanho da sprint em dias | 7 |
| PS | Total de sprints planejadas | 6 |
| SD	| Data de início | 05/03/2018 |
| PRP | Pontos planejados para a primeira _release_ | 172 |

### Legenda:
| Identificador | Descrição |
| --- | --- | 
| PRP | O PRP foi modificado para ser a soma de todos os pontos reavaliados das histórias. |
| RPC | De forma análoga, o RPC é avaliado como o somatório dos pontos concluídos até a sprint atual. |
| PPC | Esse valor é o somatório da razão entre a duração da sprint atual sobre o número de sprints da _release_ até a sprint atual. |
| APC | Esse valor é obtido pela razão entre o RPC da sprint e o PRP. |
| PP | Pontos que foram planejados para cada sprint. |
| PA | Funcionalidades novas que foram adicionadas ao projeto/sprint. |
| PDT | Pontos relacionados a dívidas técnicas deixadas pelas sprints anteriores. |
| PC | Quantos pontos foram efetivamente completados na sprint. |
| PV | O valor planejado é obtido através da multiplicação do PPC pelo orçamento do projeto. |
| AC | É conseguido através da multiplicação do PPC pelo orçamento também, visto que no projeto ágil o valor real é sempre igual ao planejado. |
| EV | É resultado da multiplicação da PC pelo orçamento do projeto, divido pelo PRP. |
| TEV | É o somatório do TEV até aquela sprint. |
| CV | É a subtração do TEV pelo AC. |
| SV | É a subtração do TEV pelo PV. |
| CPI | É a divisão de TEV por AC. |
| SPI | É a divisão de TEV por PV. |

### Planilha EVM
Link para a planilha EVM no [Google Docs](https://docs.google.com/spreadsheets/d/1ZHlVvq_5Sjnyp-sH-7Zfn_KFYzFxoZwtOBWQ92yfd3M/edit?usp=sharing).

## Referências
HiFlex Consultoria. Gerenciamento de valor agregado (EVM)  em projetos agéis. Vitor Massari. Acesso em: <http://www.hiflex.com.br/v1/gerenciamento-de-valor-agregado-evm-em-projetos-ageis/>
codetiburon. Earned Value Management (EVM) for Agile Software Projects. Olga Yatskevich. Acesso em: <https://codetiburon.com/earned-value-management-evm-agile-software-projects/>
