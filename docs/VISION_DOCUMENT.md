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
| 11/03/2018 | 0.2 | Tópicos 1 e 2 | Guilherme Guy e Joberth Rogers |
| 14/03/2018 | 0.3 | Tópicos 3 e 4 | Daniel Maike e Geovana Ramos |
| 14/03/2018 | 0.4 | Tópicos 5,6,7,8 e 9 | Elias Bernardo e Gabriela Medeiros |


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

## 3:  Descrições da Parte Interessada e do Usuário

### 3.1 Resumo da Parte Interessada

| Nome | Descrição | Responsabilidade |
|------|------------|-----------------|
| Equipe de Desenvolvimento | Estudantes da Universidade de Brasília da disciplina Métodos de Desenvolvimento de Software | Participar de forma ativa implementando o software descrito neste documento. |
|Equipe de Gestão de Projeto | Estudantes da Universidade de Brasília da disciplina de Engenharia de Produto de Software. | Gerenciar a equipe de desenvolvimento, apontando caminhos e soluções e possíveis riscos. |
| Clientes | Comunidade Médica, paciente e familiares do Centro de Referência em Síndrome de Down - Cris Down | Requisitar as informações para verificar status das consultas dos pacientes. |

### 3.2  Resumo do Usuário

| Nome | Descrição | Parte Interessada |
|------|-----------|-------------------|
| Médicos do Cris Down | Equipe médica que trabalha no Cris Down | Usuários |
| Profissionais de Saúde | Profissionais de saúde diversos que são associados ao Cris Down | Usuários |
| Familiares |Familiares (ou responsáveis) do paciente com síndrome de Down | Usuários |
Paciente com Síndrome de Down | Paciente com síndrome de Down atendido pelo Cris Down | Usuários |

### 3.3 Ambiente do Usuário

O acesso aos serviços da aplicação poderá ser feito por navegadores de internet, como o Mozilla Firefox, Google Chrome, Opera, Apple Safari e outros.

### 3.4 Perfis das Partes Interessadas

#### 3.4.1 - Equipe de desenvolvimento

|                        |                     |
|------------------------|---------------------|
| Representantes | Daniel Maike, Elias Bernardo, Gabriela Medeiros, Geovana Ramos, Guilherme Guy, Joberth Rogers |
| Descrição | Desenvolvedores |
| Tipo | Estudantes da Universidade de Brasília da disciplina de Métodos de Desenvolvimento de Software |
| Responsabilidade | Desenvolvimento e Implementação da aplicação
| Critério de sucesso | Entregar o software com todas as suas funcionalidades dentro do prazo |
| Envolvimento | Alto |
| Comentários ou problemas | Falta de experiência com projetos deste porte, dificuldades com o uso de novas ferramentas e linguagens de programação. |

#### 3.4.2 - Equipe de gestão de projeto

|                |                                                            |
|-----------------|-----------------------------------------------------------|
| Representantes | Diego França, João Sconetto, Mariana Mendes, Victor Arnaud |
| Descrição | Gestores de Projeto |
| Tipo | Estudantes da Universidade de Brasília da disciplina de Engenharia de Produto de Software. |
| Responsabilidade | Estabelecer metas e prazos, informar os melhores caminhos e possíveis riscos na aplicação. Gerenciar a equipe de desenvolvimento. |
| Critério de sucesso | Manter o foco sobre a equipe impondo metas, tentar estabelecer uma relação profissional dentro da equipe de desenvolvimento de forma que o software seja entregue no prazo, sem riscos e com qualidade. |
| Envolvimento | Alto |
| Comentários ou problemas | Dificuldade em aprender a gerenciar enquanto se coloca em prática. |

#### 3.4.3 - Usuários do Aplicativo

|               |                |
|---------------|----------------|
|Representantes | Pacientes, familiares e membros da equipe de saúde participante do Cris Down |
| Descrição| Usuários que irão usufruir da aplicação e de suas informações.
Tipo |
| Médicos | Funcionários do hospital
familiares | Pacientes |
|Responsabilidade | Usar a aplicação de forma a otimizar o tempo de busca das informações do paciente e seu status para funcionalidades do Cris Down.|
| Critério de sucesso | Diminuir o uso de métodos tradicionais usando papelada e recorrer informações do usuário de forma mais rápida e eficiente pelo aplicativo web.|
| Envolvimento | Alto |
| Comentários ou problemas | - |

### 3.5 Perfil dos Usuários

#### 3.5.1 - Médicos do Cris Down

|               |           |
|---------------|----------|
| Representante | Usuários |
| Descrição | Médico que trabalha no Cris Down atendendo casos de SD. |
| Tipo | Usuário Avançado |
| Responsabilidade | Conhecer a aplicação e todas as suas funcionalidades.  Além de utilizar a aplicação para facilitar seu trabalho. |
| Critérios de sucesso | Possuir acesso à dispositivos capazes de acessar os serviços que a aplicação fornece e que estejam em bom estado de funcionamento. |
| Envolvimento | Baixo |
| Comentários ou Problemas | - |

#### 3.5.2 - Profissionais de Saúde

|               |                     |
|---------------|---------------------|
| Representante | Usuários |
| Descrição |Profissionais de saúde relacionados ao Cris Down que possibilitam atendimento ao paciente em localizações mais próximas a sua residência. |
| Tipo | Usuário Avançado |
| Responsabilidade | Conhecer a aplicação e utilizá-la para auxiliar no tratamento de pacientes com SD. |
| Critérios de sucesso | Possuir acesso à dispositivos capazes de acessar os serviços que a aplicação fornece e que estejam em bom estado de funcionamento. |
| Envolvimento | Baixo |
| Comentários ou Problemas | - |

#### 3.5.3 - Familiares

|                  |                     |
|------------------|---------------------|
| Representante | Usuários|
| Descrição | Familiares do paciente com SD. |
| Tipo | Usuário Informal |
| Responsabilidade | Conhecer a aplicação e usá-la para auxiliar no acompanhamento de seu familiar com SD. Marcar consultas para seu familiar com SD. |
| Critérios de sucesso | Possuir acesso à dispositivos capazes de acessar os serviços que a aplicação fornece e que estejam em bom estado de funcionamento. |
| Envolvimento | Baixo |
| Comentários ou Problemas | - |

#### 3.5.4 - Paciente

|                  |               |
|------------------|---------------|
| Representante | Usuários |
| Descrição | Paciente com SD
Tipo | Usuário Informal |
| Responsabilidade | Conhecer a aplicação e usá-la para auxiliar em seu tratamento. |
| Critérios de sucesso | Possuir acesso à dispositivos capazes de acessar os serviços que a aplicação fornece e que estejam em bom estado de funcionamento. |
| Envolvimento | Baixo |
| Comentários ou Problemas | - |


### 3.6 Principais Necessidades da Parte Interessada ou do Usuário

| Necessidade | Prioridades | Interesses | Solução atual | Solução proposta |
|-------------|-------------|------------|---------------|------------------|
| Ajustar a ficha médica de acordo com as especificidades da SD | Alta | Permitir e facilitar aos médicos o diagnóstico de pacientes com SD | Prontuário padronizado para todos os pacientes | Prontuário específico para pacientes com SD |
| Maior comunicação entre as partes envolvidas | Alta | Facilitar a transmissão de informações entre pacientes, familiares e médicos | Informações transmitidas durante a consulta presencial | Um meio de comunicação virtual acessível entre os interessados |
| Definição de atributos para a fila de espera | Alta | Padronizar e tornar mais eficiência o sistema de posicionamento da fila de espera | Classificação subjetiva de acordo com o diagnóstico feito pelo médico | Tornar os critérios para a posição na fila de espera objetivos e padronizados |

### 3.7	Alternativas e Concorrência

Atualmente não há nenhum aplicativo que integre pacientes de SD, familiares e profissionais - o que é proposto neste projeto.  Há um aplicativo específico para o acompanhamento à saúde das crianças com Síndrome de Down (DownEx) e outros aplicativos que atendem pessoas com deficiência intelectual, que poderiam ser utilizados por pessoas com Síndrome de Down. Contudo, como tais aplicativos têm foco pedagógico e educacional, não são considerados concorrentes.


## 4:	Visão Geral do Produto

### 4.1	Perspectiva do Produto

O sistema Dr. Down funciona em múltiplas camadas com a finalidade de melhor atender os seus usuários. A função do sistema se resume em auxiliar a equipe do Cris Down no cadastro e gerenciamento de pacientes, isso inclui marcação de consultas, fila de espera, além da divulgação de informações importantes. Para auxiliar nessa tarefa, o sistema terá acesso aos dados da Secretaria de Estado de Saúde (SES) através de um número de identificação, o que possibilitará levantar dados de determinados pacientes.

### 4.2	Resumo das Capacidades

|                  |                 |
|------------------|-----------------|
|Benefícios para o Cliente |Recursos de |
| Consulta rápida do histórico do paciente |Pesquisa do banco de dados do Cris Down. |
| Comunicação entre pacientes, familiares e médicos |Fórum para dúvidas e mensagens diretas. |
| Verificação do paciente na fila de espera | Funcionalidade mostrando o tempo que falta até a sua consulta. |
| Jogos para o desenvolvimento dos pacientes | Ligação da página com links para jogos interativos |

### 4.3	Licenciamento e Instalação

A distribuição do software se dará sob a licença do MIT. Tal licença é aberta quanto a permissão para edição, visualização e utilização do software.

## 5:	Recursos do Produto

### 5.1 Acesso.

A autenticação do usuário deverá ocorrer por login.

### 5.2 Nível de acesso

As informações dependem do tipo de usuário. Os pacientes e familiares terão apenas informações básicas do prontuário. Caso seja um funcionário do hospital, possuirá, além das informações básicas do paciente, o número de SES e poderá inserir informações sobre o atendimento realizado por ele. O médico, por fim, terá acesso a todas as funcionalidades básicas, além de modificar/atualizar informações no sistema sobre o paciente.

### 5.3 Cadastro

O cadastramento ocorrerá no próprio aplicativo. Quando o perfil for de um  funcionário do hospital ou médico do Cris Down, dependerá do administrador para verificar as informações dos profissionais da rede.

### 5.4 Espaço

Dentro da aplicação o espaço deve fornecer salas de fóruns com dúvidas dos usuários e chats privados para comunicação entre médicos e pacientes/familiares.

### 5.5 Informações

No quesito informações, o aplicativo fornecerá um  FAQ com as perguntas mais frequentes feitas pelos usuários, agenda com as futuras consultas, além dos locais de atendimento para a comunidade do Cris Down.

### 5.6 Localização

Além de conter a localização do Cris Down, o aplicativo fornecerá a localização com os principais eventos perto da localização do usuário.

### 5.7 Fila de Espera

Haverá um questionário antes de cada triagem para definir a posição do paciente de acordo com o risco ambulatório de seu prontuário: Risco familiar, psicossocial ou risco de  saúde; O que irá definir a classificação do paciente dentro da fila. Além do citado acima irá conter o tempo estimado na fila e um contador de onde a pessoa está na mesma.

### 5.8 Relatórios gerenciais

O software irá gerar relatórios a respeito do aplicativo e da lista de espera dos atendimentos.

### 5.9 Marcação de consulta

Para incluir o paciente na fila de espera, o paciente ou familiar deve responder um questionário com seu risco ambulatório e definir a urgência da consulta.

## 6: Restrições

### 6.1 Restrições de sistema

O sistema se comunica com um banco de dados externo, sendo que nenhuma informação deve estar vinculada a qualquer outros aparelhos ou computadores.
O sistema não deve revelar quaisquer informações a terceiros exceto funcionários e médicos do Cris Down, além de manter confidencialidade médico e paciente.

### 6.2 Restrições externas

Dentre as restrições externas as que mais irão influenciar são a inexperiência com a linguagem, perda ou dano de equipamento, conflito entre a equipe de desenvolvimento.

### 6.3 Restrições de design

O sistema não pode  ter uma interface muito complexa, pelo motivo de estar lidando com os paciente no seu  conjunto, de forma que seja uma plataforma chamativa e onde todos os ícone esteja de fácil acesso.

## 7:	Faixas de Qualidade

Para maior eficiência, a aplicação será web, pois o gerenciamento de pacientes pelos funcionários do hospital seria dificultado caso tivesse que ser feito em aparelhos mobile. Porém, para atender os pacientes e familiares com qualidade, o Dr. Down deve se adaptar a tela de smartphones e tablets.

## 8:	Precedência e Prioridade

O gerenciamento e cadastro de usuários é a funcionalidade de maior importância, seguida pela marcação de consultas e local para contato entre funcionários de saúde e pacientes/familiares. Demais funcionalidades possuem mesma prioridade.

## 9:	Outros Requisitos do Produto

### 9.1	Requisitos do Sistema

O usuário deverá ter acesso a um navegador de internet para poder utilizar o Dr. Down.

### 9.2	Requisitos de Desempenho

O sistema deverá funcionar com fluidez independente da demanda. Se todos os funcionários estiverem usando o Dr.Down ao mesmo tempo, ele deverá responder sem travamentos e processar todos os comandos.
