# Fechamento da Sprint 14

## 1. Resumo da Sprint

__Pontos Planejados__: 23 pontos

__Pontos concluídos__: 20 pontos

__Dívidas técnicas__: 3 pontos

__Histórias entregues:__

- [US120 - Agenda de eventos](https://github.com/fga-gpp-mds/2018.1-Dr-Down/issues/288)
- [US121 - Notificação por e-mail](https://github.com/fga-gpp-mds/2018.1-Dr-Down/issues/289)
- [US122 - Página de ajuda](https://github.com/fga-gpp-mds/2018.1-Dr-Down/issues/290)
- [TS123 - Correção do frontend](https://github.com/fga-gpp-mds/2018.1-Dr-Down/issues/291)
- [TS124 - Atualizar o EVM](https://github.com/fga-gpp-mds/2018.1-Dr-Down/issues/292)
- [TS126 - Corrigir imagem da representação da arquitetura](https://github.com/fga-gpp-mds/2018.1-Dr-Down/issues/294)
- [TS127 - Corrigir o pipeline](https://github.com/fga-gpp-mds/2018.1-Dr-Down/issues/295)
- [TS128 - Documentação da Sprint 13](https://github.com/fga-gpp-mds/2018.1-Dr-Down/issues/296)

__Histórias não entregues:__

- [TS125 - Corrigir o bug do deploy de produção](https://github.com/fga-gpp-mds/2018.1-Dr-Down/issues/293)

## 2. Retrospectiva da Sprint

| Pontos Positivos | Pontos Negativos | Sugestão de Melhoria |
| ----- | ----- | ---- |
| termino de história com antecedência | dificuldade em fazer a história com as restrições relacionadas ao DevOps | estudar mais para tentar solucionar o problema na homologação |
| bom planejamento de dupla | atraso em reuniões presenciais | recuperar dos problemas para retornar ao ritmo |
| está acabando | documentação de componente foi de pouca ajuda | - |
| foi uma semana tranquila com relação às histórias | problemas pessoais | - |
| ajuda entre os membros do grupo nas histórias | falta da daily presencial devido às circunstâncias | - |
| equipe manteve o foco e executou as estórias num tempo curto | bug no Postgres no ambiente de homologação | - |
| equipe testou as estórias no ambiente de homologação | dívida técnica depois de muito tempo com o time integrado e sem problemas com a ferramenta | - |
| a comunicação da equipe, mesmo que a distância, foi efetiva | alguns membros esqueceram de fechar a issue no mesmo dia que o PR foi fechado | - |
| a ferramenta de e-mail está funcionando perfeitamente (estória de notificação) | - | - |
| a ferramenta está com um frontend bem consolidado | - | - |
| burndown melhorou | - | - |
| equipe executou as história com uma maior celeridade | - | - |
| acabaram as estórias de usuário (features) do nosso escopo | - | - |

## 3. Quadro de Conhecimento

![Quadro de conhecimento da Sprint 14](https://uploaddeimagens.com.br/images/001/480/059/full/quadro_conhecimento_S14-15.png?1529874150)

## 5. Gráfico do Burndown

![Gráfico do burndown da Sprint 14](https://uploaddeimagens.com.br/images/001/478/487/full/burndown_S14.png?1529719817)

## 6. Velocity

![Gráfico do velocity da Sprint 14](https://uploaddeimagens.com.br/images/001/478/492/full/velocity_S14.png?1529720002)

## 7. Gráfico de Commits

![Gráfico de commits da Sprint 14](https://uploaddeimagens.com.br/images/001/478/485/full/commits_S14.png?1529719767)

## 8. EVM

![Gráfico da EVM da Sprint 14](https://uploaddeimagens.com.br/images/001/478/489/full/evm_S14.png?1529719846)

## 9. Análise do Scrum Master

Nesta sprint, diversos fatores externos e de difícil previsão atrapalharam o bom andamento das atividades, como o bug no Postgres no ambiente de homologação e os problemas pessoais. Mesmo assim, tudo foi entregue dentro do prazo estipulado e, no caso dos problemas pessoais, as pessoas envolvidas relataram que estes já estão sob controle, e que para a próxima sprint poderão se dedicar como vinham fazendo ao projeto.

O bug do Postgres foi informado aos desenvolvedores do Cookiecutter no git desse projeto, e estamos contando com a ajuda deles para conseguirmos resolver esta questão e estabilizar essa questão no ambiente de homologação. Enquanto isso, paralelamente estamos buscando maneiras de solucionar esse problema.

A dificuldade com as restrições relacionadas à questões do DevOps foi devido ao fato de que as alterações em certos arquivos não deveriam ser commitadas, já que possuiam informações que devem se manter sigilosas por serem relacionadas à configuração do servidor. Isso deu algum trabalho para os responsáveis pela história do email, mas no fim deu tudo certo.

Também tivemos, mais uma vez, que lidar com uma documentação de componente que usamos que não atendeu nossa demanda por informações. Mesmo assim, conseguimos usar aquele em nossa aplicação com sucesso.

Por fim, alguns de nossos combinados anteriores tiveram que ser relembrados, pois não estavam sendo seguidos como deveriam. Este foi o caso de fechar as issues após os PRs terem sido aceitos e ser verificado se tudo está funcionando corretamente no ambiente de homologação. Também foi o caso dos atrasos em reuniões presenciais. Conversamos sobre isso e os envolvidos se comprometeram a tomar mais cuidado com essas coisas para a próxima sprint.
