# Documento de Visão


Índice
=================

   * [Documento de Visão](#documento-de-visão)
      * [Histórico de Revisão](#histórico-de-revisão)
      * [1: Introdução](#1-introdução)
         * [1.1	Propósito](#11propósito)
         * [1.2	Escopo](#12escopo)
         * [1.3	Definições, acrônimos e abreviações](#13definições-acrônimos-e-abreviações)
         * [1.4 Referências](#14-referências)
         * [1.5 Visão Geral](#15-visão-geral)
      * [2: Posicionamento](#2-posicionamento)
         * [2.1 Oportunidade de Negócios](#21-oportunidade-de-negócios)
         * [2.2 Instrução do Problema](#22-instrução-do-problema)
         * [2.3 Instrução de Posição do Produto](#23-instrução-de-posição-do-produto)


## Histórico de Revisão

|Data | Versão | Descrição | Autores |
|  ---  |  ---  |  ---  |  ---  |
| 10/03/2018 | 0.1 | Abertura do documento | Guilherme Guy |
| 11/03/2018 | 0.2 | Tópicos 1 e 2 | Daniel Maike, Geovana Ramos |

## 1: Introdução
 
### 1.1	Propósito 
O propósito deste documento é definir e especificar, de maneira ampla, as características pertinentes à aplicação solicitada pelo Centro de Referência em Síndrome de Down, mais conhecido como Cris Down. Este documento possui como pontos principais: definir o escopo, os recursos e todo o público alvo que será englobados pelo sistema e as razões que levam às necessidades do mesmo. Visa explicar detalhes sobre a aplicação a ser desenvolvida, suas características, funcionalidades, como os usuários se relacionam nesse meio e possíveis restrições no desenvolvimento.
 
### 1.2	Escopo
No mês de Abril do ano de 2013, foi inaugurado na Asa Norte, em Brasília -DF, um local especializado no acompanhamento e cuidado de pessoas com Síndrome de Down, condição também conhecida como trissomia 21. Apesar do excelente trabalho realizado pelos profissionais do local, a demanda por atendimento especializado cresce rotineiramente, resultando na sobrecarga de pacientes e em uma fila de espera crescente. Tal consequência gera a necessidade de um sistema de classificação de prioridades, que, atualmente, priorizam os pacientes a partir de uma análise subjetiva por parte do médico, sendo esse um dos tópicos a serem abordados para a melhoria da gestão e administração do centro já citado. 
O projeto a ser desenvolvido tem como objetivo oferecer uma ferramenta de gestão desses pacientes, assim como algumas utilidades complementares. O software oferecerá funcionalidades tanto para os profissionais de saúde do Cris Down, como para os pacientes e familiares, tratando de áreas como gestão de pacientes, agenda de consultas, orientações sobre a Síndrome de Down, localização do Cris Down, classificação de risco, informações, chat e sugestões de jogos voltados para os pacientes.

### 1.3	Definições, acrônimos e abreviações
| Abreviação | Definição |
| --------         | ------         |
| SD | Síndrome de Down |
| CRIS DOWN |Centro de Referência em Síndrome de Down |
| MDS | Métodos de Desenvolvimento de Software |
| EPS| Engenharia de Produto de Software |
|UnB|Universidade de Brasília|
|SES|Secretaría de Estado de Saúde|

### 1.4 Referências
DOCUMENTO DE VISÃO PARA UM PROJETO DE REQUISITOS. IBM Knowledge Center. Disponível em: <https://www.ibm.com/support/knowledgecenter/pt-br/SSYMRC_4.0.6/com.ibm.rational.rrm.help.doc/topics/r_vision_doc.html >. Acesso em: 10/03/2018
 
RESENDE, Angelica Aguiar. ANÁLISE DA VIABILIDADE TÉCNICA PARA DESENVOLVIMENTO DE APLICATIVO PARA O CENTRO DE REFERÊNCIA EM SÍNDROME DE DOWN (CRIS DOWN). 2017. 90 f. Trabalho de conclusão de curso (Graduação em Engenharia de Produção)- UNIVERSIDADE DE BRASÍLIA, Faculdade de Tecnologia Departamento de Engenharia de Produção, 2017.

(em inglês). Instituto de Tecnologia de Massachusetts, licença https://mit-license.org/. Consultado em 13 de Março de 2018.

### 1.5 Visão Geral
Este documento se organiza de maneira que se entenda primeiramente as funções e objetivos do projeto, seguidos pelos perfis de usuário e equipe de desenvolvimento. Por fim, se descreve as características técnicas da aplicação. Está organizado em: posicionamento, descrição da parte interessada e do usuário, visão geral e recursos do produto, restrições, faixas de qualidade, procedência e prioridade, requisitos e documentação do produto e apêndice.

## 2: Posicionamento

### 2.1 Oportunidade de Negócios
O Dr. Down possui o intuito de facilitar e agilizar a interação entre profissionais de saúde e pacientes do hospital. Dessa maneira, haverá a economia de recursos, de tempo e trabalho, tornando mais eficaz os atendimentos no hospital.

### 2.2 Instrução do Problema
| | |
|---|---|
|O problema é que|há um constante aumento da demanda pelos serviços oferecidos pelo Cris Down e não há recursos para um atendimento eficaz aos pacientes|
|o que afeta|o gerenciamento dos pacientes na fila de espera, pois o métodos de avaliação de prioridade de pacientes deixam de ser eficazes e as atividades administrativas do Cris Down|
|isso causa| a sobrecarga dos funcionários resultando na má comunicação entre as partes interessadas, atendimento demorado e de baixa qualidade |
|e uma possível solução é|a criação de uma aplicação eletrônica que visa auxiliar na “Linha de cuidado” do paciente, possibilitando seu cadastro no sistema e também seu acompanhamento por seus responsáveis ou equipes de saúde|

### 2.3 Instrução de Posição do Produto
| | |
|---|---|
|**Para** |Médicos, comunidade do Hospital, familiares e pacientes|
|**que**| necessitam de uma plataforma que disponibiliza o status do paciente com seu prontuário e sua posição na fila de espera das consultas|
|**o**| Dr. Down|
|**é uma**|ferramenta que disponibiliza todas as informações do prontuário do paciente e sua posição na fila de espera nas consultas de forma rápida e fácil, assim como uma interface de comunicação entre médico e paciente, além de informações sobre a Síndrome de Down|
|**diferente**|de outras ferramentas que apresentam somente uma ou duas dessas funções, o Dr. Down reúne todas essas funcionalidades em uma só aplicação|
