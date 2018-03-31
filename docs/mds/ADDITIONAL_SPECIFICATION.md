# Especificação suplementar

## Histórico de Revisão
| Data | Versão | Descrição | Autores |
|  ---  |  ---  |  ---  |  ---  |
| 28/03/2018 | 0.0.1 | Abertura do documento | Geovana Ramos |
| 28/03/2018 | 0.1.0 | Adição dos tópicos de 1 a 9 | Geovana Ramos e Guilherme Guy |
| 29/03/2018 | 0.1.1 | Revisão dos tópicos 2 e 3 |  Gabriela Medeiros  |
| 29/03/2018 | 0.1.2 | Revisão do tópico 5 |  Guilherme Guy e Geovana Ramos |
| 29/03/2018 | 0.2.0 | Adição do tópico 9 |  Gabriela Medeiros |
| 30/03/2018 | 0.2.1 | Revisão ortográfica e do diagrama NFR |  Gabriela Medeiros e Geovana Ramos |


## 1. Introdução
### 1.1 Finalidade
Este documento tem como objetivo abordar aspectos técnicos, legais e demais requisitos sobre a aplicação Dr. Down, que não foram abordados nos demais documentos: Documento de Visão e Documento de Arquitetura.

### 1.2 Escopo
Os requisitos aqui elucidados fazem parte do processo de desenvolvimento da aplicação web Dr.Down, que auxiliará pacientes e funcionários do CRIS DOWN, centro que trata pacientes com Síndrome de Down.

Primeiramente estão definidos os requisitos não funcionais e em seguida estes requisitos estão dispostos em um diagrama NFR.  O NFR Framework é uma abordagem orientada a processos, onde os requisitos não-funcionais são explicitamente representados como metas a serem obtidas e como serão obtidas.


### 1.3 Definições, Acrônimos e Abreviações
| Abreviação  |  Definição  |
|   ---       |    ---      |
| SD          | Síndrome de Down |
|  CRIS DOWN  | Centro de Referência em Síndrome de Down |
|  NFR        | 	Non-Functional Requirement |

### 1.4 Referências
RESENDE, Angelica Aguiar. ANÁLISE DA VIABILIDADE TÉCNICA PARA DESENVOLVIMENTO DE APLICATIVO PARA O CENTRO DE REFERÊNCIA EM SÍNDROME DE DOWN (CRIS DOWN). 2017. 90 f. Trabalho de conclusão de curso (Graduação em Engenharia de Produção)- UNIVERSIDADE DE BRASÍLIA, Faculdade de Tecnologia Departamento de Engenharia de Produção, 2017.

ISO 27002: BOAS PRÁTICAS PARA GESTÃO DE SEGURANÇA DA INFORMAÇÃO . Disponível em: < https://ostec.blog/padronizacao-seguranca/iso-27002-boas-praticas-gsi >. Acesso em: 30/03/2018

10 HEURÍSTICAS DE NIELSEN. UMA FÓRMULA PARA EVITAR ERROS BÁSICOS DE USABILIDADE . Disponível em: < http://blog.caelum.com.br/10-heuristicas-de-nielsen-uma-formula-pra-evitar-erros-basicos-de-usabilidade/ >. Acesso em: 30/03/2018



## 2. Usabilidade
Um ponto essencial para a usabilidade do sistema proposto é que o mesmo ofereça um design e uma interação acessível aos portadores da SD.
Considerando a deficiência intelectual a que as pessoas com Síndrome de Down são acometidas, o sistema deverá presar por simplicidade e acesso intuitivo, tendo em vista sua importância para o ajustamento e uma utilização adequada pelos usuários da aplicação. Para alcançar tal meta, a aplicação deve conter um design limpo, de fácil vizualização e entendimento, com acesso rápido e intuitivo a informações e funcionalidades importantes, sempre utilizando-se uma linguagem de fácil entendimento e compreensão.

Inicialmente, os funcionários que atendem no CRIS DOWN passarão por uma fase de adaptação ao sistema, que pode incluir um treinamento inicial para instruí-los sobre o funcionamento das marcações de consulta e gerenciamento de pacientes. Devido ao requisito de facilidade de uso do sistema, este treinamento não irá durar mais que 2 horas, que são suficientes para inserir o Dr. Down como nova ferramenta de trabalho.

### 2.1 Metas de usabilidade
- Eficaz: O sistema deve fazer o que eu espero que faça, alcance seu objetivo.
- Eficiente: Velocidade de uso.
- Segurança: Proteção ao usuário contra condições perigosas (físicas) e situações indesejáveis (medo).
- Utilidade: Oferece o tipo certo de funcionalidade.
- Aprendizado: Fácil de aprender.
- Memorização: Fácil de lembrar como se usa.
- Prevenções de erros: Evitar inserção de dados errôneos ou inadequados.
- Diagnóstico de erro fácil para o usuário: Mensagens de erro claras e de fácil entendimento para o usuário.
- Visibilidade de estado do sistema: Deixar claro ao usuário o que está acontecendo em tempo real.


## 3. Confiabilidade
O sistema deverá ter alto nível de disponibilidade considerando a necessidade de acesso contínuo e frequente à aplicação. Tal requisito gerará um contexto em que falhas e bugs do sistema tenham a possibilidade de serem corrigidas rapidamente, pois esses erros podem gerar atrasos nos atendimentos e problemas administrativos no CRIS DOWN. Por isso, o sistema deve estar disponível em pelo menos 90% das 24 horas diárias.

## 4. Portabilidade
O sistema deverá funcionar nos navegadores de internet Google Chrome, Mozilla Firefox e Apple Safari e em dispositivos capazes de acessar a internet, que suportem os navegadores descritos e, também, que estejam equipados com sistema Windows, Linux, Mac, Android e iOS, ou seja,se adaptando visualmente à esses sistemas.

## 5. Desempenho
O sistema deverá processar as requisições de acesso do usuário de maneira eficiente e fluída, contribuindo para a qualidade dos atendimentos do CRIS DOWN. O número mínimo de acessos suportados simultaneamente deve ser de 2 mil usuários.

## 6. Interoperabilidade
O sistema possuirá conexão com banco de dados para armazenar informações de usuários cadastrados e também deverá salvar suas informações remotamente, fora do dispositivo do usuário.

## 7. Segurança
As informações de um usuário somente serão acessadas por ele mesmo ou outros usuários que possuam permissão pra isso. O sistema atenderá as políticas de privacidade do usuário, que garantem a proteção dos seus dados e a visualização restrita,  e buscará incluir boas práticas de segurança de informações como segurança das operações e comunicações, controle de acesso e conformidade com a legislação.

## 8. Restrições de Design

### 8.1 Interface
- Minimalista
- Intuitivo
- Informações objetivas
- Links de informações visíveis
### 8.2 Arquitetura
- Model-View-Template
### 8.3 Padrão de código
- Class Based Views
- PEP 8
- Doc strings
### 8.4 Ferramentas
#### 8.4.1 Desenvolvimento
- MakeFile
- Travis
- CodeClimate
- CookieCutter
- Docker
- GitHub
#### 8.4.2 Gerenciamento
- ZenHub
- Slack
- Google Drive


## 9. Interfaces do Usuário
As seguintes telas serão disponibilizadas no sistema:
- Tela inicial
- Login
- Cadastro
- Informações do usuário
- Fila de espera
- Agenda de consultas
- Informações sobre SD
- Linha de cuidado
- Fórum
- Mapas dos locais de atendimento
- Eventos
- Prontuário
- Questionário de risco médico

## 10. Diagrama NFR
O diagrama NFR ilustra os requisitos não funcionais e suas relações.

![Diagrama NFR](http://uploaddeimagens.com.br/images/001/352/152/original/nfr%281%29.png?1522413253)
