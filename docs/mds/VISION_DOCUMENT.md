# Documento de Visão
***
## Histórico de Revisão
***

|Data | Versão | Descrição | Autores |
|  ---  |  ---  |  ---  |  ---  |
| 10/03/2018 | 0.0.1 | Abertura do documento | Guilherme Guy |
| 11/03/2018 | 0.1.0 | Tópicos 1 e 2 | Guilherme Guy e Joberth Rogers |
| 14/03/2018 | 0.2.0 | Tópicos 3 e 4 | Daniel Maike e Geovana Ramos |
| 14/03/2018 | 0.3.0 | Tópicos 5,6,7,8 e 9 | Elias Bernardo e Gabriela Medeiros |
| 18/03/2018 | 0.3.1 | Correção de informações Histórico de Revisão | Guilherme Guy |
| 18/03/2018 | 0.3.2 | Revisão geral | Joberth Rogers, Elias Bernardo, Guilherme Guy |
| 18/03/2018 | 1.0.0 | Termino do documento | Joberth Rogers, Elias Bernardo, Guilherme Guy |
| 19/03/2018 | 1.0.1 | Revisões gerais | Joberth Rogers, Daniel Maike, Guilherme Guy |
| 21/03/2018 | 1.0.2 | Revisão | Daniel Maike, Guilherme Guy |
| 26/03/2018 | 1.1.0 | Adição de recurso do produto ao tópico 5 | Daniel Maike, Guilherme Guy, Joberth Rogers |
| 27/03/2018 | 1.1.1 | Revisão do tópico 5 | Daniel Maike, Guilherme Guy, Joberth Rogers |

***
## 1: Introdução
***

### 1.1	Propósito

O propósito deste documento é definir e especificar, de maneira ampla, as características pertinentes à aplicação solicitada pelo Centro de Referência em Síndrome de Down, mais conhecido como Cris Down. Sendo assim, possui como objetivo definir o escopo, os recursos e o público alvo, que serão englobados pelo sistema, além das razões que levam às necessidades do mesmo. Visa explicar detalhes sobre a aplicação a ser desenvolvida: suas características, funcionalidades, como os usuários se relacionam nesse meio e possíveis restrições no desenvolvimento.

### 1.2	Escopo

No mês de Abril do ano de 2013, foi inaugurado na Asa Norte, em Brasília - DF, um local especializado no acompanhamento e cuidado de pessoas com Síndrome de Down, condição também conhecida como trissomia 21. A demanda por atendimento especializado cresce rotineiramente, resultando no aumento da quantidade de pacientes e em uma fila de espera crescente. Consequentemente há a necessidade de um sistema de classificação de prioridades que, atualmente, prioriza os pacientes a partir de uma análise subjetiva por parte da equipe de saúde, sendo esse um dos tópicos a serem abordados para a melhoria da gestão e administração do Cris Down.
O projeto a ser desenvolvido tem como objetivo oferecer uma ferramenta de gestão dos pacientes, assim como algumas utilidades complementares. O software oferecerá funcionalidades tanto para os profissionais de saúde e demais funcionários do Cris Down quanto para os pacientes e seus responsáveis, tratando de áreas como marcação e visualização de consultas, esclarecimentos sobre a Síndrome de Down, localização da instituição e classificação de prioridade do paciente, entre outros.

### 1.3	Definições, acrônimos e abreviações

| Abreviação | Definição |
| --------         | ------         |
| SD | Síndrome de Down |
| CRIS DOWN |Centro de Referência em Síndrome de Down |
|UnB|Universidade de Brasília|
|SES|Secretaría de Estado de Saúde|

### 1.4 Referências

DOCUMENTO DE VISÃO PARA UM PROJETO DE REQUISITOS. IBM Knowledge Center. Disponível em: < https://www.ibm.com/support/knowledgecenter/pt-br/SSYMRC_4.0.6/com.ibm.rational.rrm.help.doc/topics/r_vision_doc.html >. Acesso em: 10/03/2018

RESENDE, Angelica Aguiar. ANÁLISE DA VIABILIDADE TÉCNICA PARA DESENVOLVIMENTO DE APLICATIVO PARA O CENTRO DE REFERÊNCIA EM SÍNDROME DE DOWN (CRIS DOWN). 2017. 90 f. Trabalho de conclusão de curso (Graduação em Engenharia de Produção)- UNIVERSIDADE DE BRASÍLIA, Faculdade de Tecnologia Departamento de Engenharia de Produção, 2017.

(em inglês). Instituto de Tecnologia de Massachusetts, licença https://mit-license.org/. Consultado em 13 de Março de 2018.

### 1.5 Visão Geral

Este documento está organizado de maneira a se compreender primeiramente as funções e os objetivos do projeto, seguidos pelos perfis de usuário e equipe do projeto. Por fim, são descritas as características técnicas da aplicação. Está organizado em: posicionamento, descrição da parte interessada e do usuário, visão geral e recursos do produto, restrições, faixas de qualidade, procedência e prioridade, requisitos e documentação do produto e apêndice.

***
## 2: Posicionamento
***

### 2.1 Oportunidade de Negócios

O Dr. Down busca facilitar e agilizar a interação entre profissionais de saúde e pacientes do Cris Down. Dessa forma, haverá a economia de recursos, tempo e trabalho, tornando os atendimentos no Centro mais eficientes e as funcionalidades mais acessíveis.

### 2.2 Instrução do Problema

|  |  |
|---|---|
|**Problema**|Há um constante aumento na demanda pelos serviços oferecidos pelo Cris Down e não há recursos para um atendimento eficaz aos pacientes.|
|**Funções afetadas**|O gerenciamento dos pacientes na fila de espera, pois os métodos de avaliação de prioridade de pacientes, por serem totalmente manuais, acabam por diminuir a eficiência na gestão da fila.|
|**Efeito**| A sobrecarga dos funcionários resultando em uma pior comunicação entre as partes interessadas, e na demora para o paciente ser atendido.|
|**Solução**|A criação de uma aplicação eletrônica que visa auxiliar na “Linha de cuidado” do paciente, possibilitando o cadastro dele no sistema, assim como o acompanhamento deste por seus responsáveis e pela equipe de saúde.|

### 2.3 Instrução de Posição do Produto


|  |  |
|--------|--------|
|**Público alvo** |Equipe de saúde, comunidade do Hospital, pacientes e seus responsáveis|
|**Carências**| Necessidade de uma plataforma que disponibiliza informações relevantes sobre o paciente, como seu histórico e prontuário.|
|**Solução**| Dr. Down|
|**Descrição da solução**|Ferramenta que disponibiliza todas as informações do prontuário do paciente e informações sobre a Síndrome de Down, assim como uma interface de troca de conhecimentos entre a equipe de saúde e o paciente (fórum).|
|**Diferenciais**|O Dr. Down se destaca de outras ferramentas que apresentam somente uma ou duas dessas funções por reunir todas essas funcionalidades em uma só aplicação.|

***
## 3:  Descrições da Parte Interessada e do Usuário
***

### 3.1 Resumo da Parte Interessada

| Nome | Descrição | Responsabilidade |
|------|------------|-----------------|
| Equipe | Composta por graduandos em Engenharia de Software pela Universidade de Brasília, no Campus Gama, discentes das disciplinas de Engenharia de Produto de Software e Métodos de Desenvolvimento de Software. | Desenvolver e gerir o software. |
| Clientes | Equipe de saúde, funcionários, pacientes e seus responsáveis do Centro de Referência em Síndrome de Down - Cris Down | Manipular as informações disponibilizadas no sistema para aprimorar o atendimento dos pacientes com SD |

### 3.2  Resumo do Usuário

| Nome | Descrição | Parte Interessada |
|------|-----------|-------------------|
| Equipe de saúde do Cris Down | Equipe multidisciplinar de profissionais da área de saúde que trabalha no Cris Down | Usuário |
| Funcionários | Funcionários do Cris Down que trabalham nas áreas de administração e secretaria | Usuário |
| Responsáveis |Responsáveis do(s) paciente(s) com SD | Usuário |
| Paciente com Síndrome de Down | Paciente com Síndrome de Down atendido pelo Cris Down | Usuário |

### 3.3 Ambiente do Usuário

O acesso aos serviços da aplicação poderá ser feito por navegadores de internet, como o Mozilla Firefox, Google Chrome, Apple Safari.

### 3.4 Perfis das Partes Interessadas

#### 3.4.1 - Usuários do Aplicativo

|               |                |
|---------------|----------------|
|**Representantes** | Pacientes e seus responsáveis, funcionários e membros da equipe de saúde participantes do Cris Down |
| **Descrição**| Usuários que irão usufruir da aplicação e de suas informações.
|**Responsabilidade** | Usar a aplicação de forma a otimizar o tempo de busca das informações necessárias e seu status para cada função.|
| **Critério de sucesso** | Diminuir o uso de métodos tradicionais e fornecer informações do usuário de forma mais rápida e eficiente pelo aplicativo web.|
| **Envolvimento** | Alto |
| **Comentários ou problemas** | - |

### 3.5 Perfil dos Usuários

#### 3.5.1 - Equipe de Saúde do Cris Down

|               |           |
|---------------|----------|
| **Representante** | Usuários |
| **Descrição** | Equipe médica que trabalha no Cris Down atendendo casos de SD. |
| **Tipo** | Usuário Avançado |
| **Responsabilidade** | Conhecer a aplicação e todas as suas funcionalidades, adicionar informações obtidas em consultas nos dados do paciente, além de utilizá-las para facilitar seu trabalho.|
| **Critérios de sucesso** | Ser capaz de utilizar o sistema para melhorar o atendimento de seus pacientes e aprimorar o gerenciamento do Cris Down. |
| **Envolvimento** | Baixo |
| **Comentários ou Problemas** | - |

#### 3.5.2 - Funcionários

|               |                     |
|---------------|---------------------|
| **Representante** | Usuários |
| **Descrição** | Funcionários que gerenciam e administram o Cris Down |
| **Tipo** | Usuário Avançado |
| **Responsabilidade** | Conhecer a aplicação e utilizá-la para auxiliar no tratamento de pacientes com SD. Tem a responsabilidade de marcar consultas, especializar os usuários cadastrados no sistema e gerenciar o fórum.  |
| **Critérios de sucesso** | Se adaptar e utilizar o sistema para colaborar no tratamento dos pacientes com SD do Cris Down |
| **Envolvimento** | Alto |
| **Comentários ou Problemas** | - |

#### 3.5.3 - Responsáveis

|                  |                     |
|------------------|---------------------|
| **Representante** | Usuários|
| **Descrição** | Responsável do paciente com SD. |
| **Tipo** | Usuário Informal |
| **Responsabilidade** | Conhecer a aplicação e usá-la para auxiliar no acompanhamento de seu familiar com SD, marcar consultas para seu familiar com SD e manter-se informado com os dados de seu/seus dependentes. |
| **Critérios de sucesso** | Se comunicar com o Cris Down e acompanhar o prontuário de seu familiar portador de SD de forma facilitada. |
| **Envolvimento** | Baixo |
| **Comentários ou Problemas** | - |

#### 3.5.4 - Paciente

|                  |               |
|------------------|---------------|
| **Representante** | Usuários |
| **Descrição** | Paciente com SD|
| **Tipo** | Usuário Informal |
| **Responsabilidade** | Conhecer a aplicação, usá-la para auxiliar em seu tratamento. |
| **Critérios de sucesso** | Passar menos tempo em fila de espera e ter uma forma mais fácil de gerir seu calendário de consulta. |
| **Envolvimento** | Baixo |
| **Comentários ou Problemas** | - |


### 3.6 Principais Necessidades da Parte Interessada ou do Usuário

| Necessidade | Prioridades | Interesses | Solução atual | Solução proposta |
|-------------|-------------|------------|---------------|------------------|
| Ajustar a ficha médica de acordo com as especificidades da SD | Alta | Permitir e facilitar à equipe de saúde o diagnóstico de pacientes com SD | Prontuário padronizado para todos os pacientes | Prontuário específico para pacientes com SD |
| Maior comunicação entre as partes envolvidas | Alta | Facilitar a transmissão de informações entre pacientes, seus responsáveis e equipe de saúde | Informações transmitidas durante a consulta presencial | Um meio de comunicação virtual acessível entre os interessados |
| Definição de atributos para a fila de espera | Alta | Padronizar e tornar mais eficiente o sistema de posicionamento da fila de espera | Classificação subjetiva de acordo com o diagnóstico feito pela equipe de saúde | Tornar os critérios para a posição na fila de espera objetivos e padronizados |

### 3.7	Alternativas e Concorrência

Atualmente não há nenhum aplicativo que integre pacientes de SD, seus responsáveis e profissionais - o que é proposto neste projeto.  Há um aplicativo específico para o acompanhamento à saúde das crianças com Síndrome de Down (DownEx) e outros aplicativos que atendem pessoas com deficiência intelectual, que poderiam ser utilizados por pessoas com Síndrome de Down. Contudo, como tais aplicativos têm foco pedagógico e educacional, não são considerados concorrentes.

***
## 4:	Visão Geral do Produto
***

### 4.1	Perspectiva do Produto

 O sistema Dr. Down funciona em múltiplas camadas com a finalidade de atender as necessidades de seus usuários.  A função do sistema pode ser resumida em auxiliar a equipe do Cris Down no cadastro e gerenciamento de pacientes, o que inclui: marcação de consultas, fila de espera, além da divulgação de informações importantes. Para possibilitar a execução dos propósitos do sistema, ele deverá possuir acesso aos dados do paciente que é identificado pelo número de identificação da Secretaria de Estado de Saúde (SES), o que possibilitará levantar dados dos pacientes, para auxiliar na consulta e no acompanhamento.

### 4.2	Resumo das Capacidades

|Benefícios para o Cliente |Recursos de |
|------------------|-----------------|
| Consulta rápida do histórico do paciente |Pesquisa no banco de dados do Cris Down. |
| Comunicação entre pacientes, seus responsáveis e equipe de saúde |Fórum para dúvidas e mensagens diretas. |
| Verificação do paciente na fila de espera | Funcionalidade mostrando o tempo que falta até a sua consulta. |

### 4.3	Licenciamento e Instalação

A distribuição do software se dará sob a licença do MIT. Tal licença é aberta quanto a permissão para edição, visualização e utilização do software.

***
## 5:	Recursos do Produto
***

### 5.1 Acesso.

A autenticação do usuário deverá ocorrer por login.

### 5.2 Nível de acesso

As informações dependem do tipo de usuário. Os pacientes e seus responsáveis terão acesso às informações básicas do prontuário e de dados relacionados à marcação de consulta, porém não poderão editá-los. Caso seja um funcionário do hospital, possuirá, além do acesso à informações básicas do paciente, permissão para editá-las, dentre outras funcionalidades relacionadas à administração do site. A equipe de saúde, por fim, terá acesso a todas as funcionalidades básicas, além de modificar/atualizar informações sobre o paciente no sistema.

### 5.3 Cadastro

O cadastro ocorrerá no próprio aplicativo. Quando o usuário cadastrado fizer parte da equipe de saúde ou dos funcionário do Cris Down, a concretização do usuário no site dependerá da confirmação das informações prestadas, que será feita por meio de um administrador do sistema.

### 5.4 Fórum

Dentro da aplicação, o espaço deve fornecer salas de fóruns para o esclarecimento de dúvidas, reclamações e sugestões dos usuários.

### 5.5 Informações

No quesito informações, o aplicativo fornecerá um FAQ com as perguntas mais frequentes feitas pelos usuários, locais de vacinação, calendário de vacina, texto informativo sobre a SD, além de uma página de ajuda sobre a usabilidade do site.

### 5.6 Localização

Além de conter a localização do Cris Down, o aplicativo fornecerá a localização dos principais eventos organizados ou recomendados pelo mesmo.

### 5.7 Marcação de consulta

Funcionários do Cris Down poderão marcar consultas, aceitar pedidos de consultas feitos pelos pacientes e seus responsáveis e definir a prioridade do paciente para a fila de espera de acordo com o seu risco ambulatorial.

### 5.8 Linha de Cuidado

O software listará diversos procedimentos e orientações que são recomendados à pessoas com Síndrome de Down de acordo com sua idade. Caso não haja confirmação de que o paciente tenha seguido o que foi listado até a data sugerida no aplicativo, o software notificará o paciente e/ou parente responsável, para que uma ação seja tomada para resolver a pendência.

## 6: Restrições
***

### 6.1 Restrições de sistema

O sistema se comunica com um banco de dados externo.
O sistema não deve revelar quaisquer informações a terceiros, exceto funcionários e equipe de saúde do Cris Down, além de manter confidencialidade entre a equipe de saúde e o paciente.

### 6.2 Restrições externas

Dentre as restrições externas as que mais irão influenciar são a inexperiência com a linguagem, perda ou dano de equipamento, e conflitos entre a equipe de desenvolvimento.

### 6.3 Restrições de design

O sistema deve ter uma interface que seja de fácil uso para pessoas com e sem SD. Dessa forma, será necessária uma plataforma chamativa, com ícones e botões intuitivos e de fácil acesso.

***
## 7:	Faixas de Qualidade
***

Para maior eficiência, a aplicação será web, pois o gerenciamento de pacientes pelos funcionários do hospital seria dificultado no caso de uma aplicação exclusiva para aparelhos mobile. Porém, para facilitar o acesso de pacientes e seus responsáveis, o Dr. Down também deve se adaptar à tela de smartphones e tablets.

***
## 8:	Precedência e Prioridade
***

O gerenciamento e o cadastro dos usuários é a funcionalidade de maior importância, seguida pela marcação de consultas e a disponibilização do local para contato entre funcionários da equipe de saúde do Cris Down e pacientes/responsáveis. As demais funcionalidades são tão importantes quanto, porém, em sua maioria, dependem da implementação do cadastro e login para serem acessadas.

***
## 9:	Outros Requisitos do Produto
***

### 9.1	Requisitos do Sistema

O usuário deverá ter acesso a um navegador de internet para poder utilizar o Dr. Down.

### 9.2	Requisitos de Desempenho

O sistema será dimensionado para suprir a necessidade de uma aplicação acessível à grande maioria dos aparelhos que têm disponibilidade de acesso. Sendo assim, o desempenho do aparelho será um fator de mínima importância para o acesso, porém de alta relevância para a obtenção de um melhor desempenho da aplicação.
