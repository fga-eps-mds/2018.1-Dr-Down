# Especificação suplementar

## Histórico de Revisão
| Data | Versão | Descrição | Autores |
|  ---  |  ---  |  ---  |  ---  |
| 28/03/2018 | 0.0.1 | Abertura do documento | Geovana Ramos |
| 28/03/2018 | 0.1.0 | Adição dos tópicos de 1 a 9 | Geovana Ramos e Guilherme Guy |
| 29/03/2018 | 0.1.1 | Revisão dos tópicos 2 e 3 |  Gabriela Medeiros  |
| 29/03/2018 | 0.1.2 | Revisão do tópico 5 |  Guilherme Guy e Geovana Ramos |
| 29/03/2018 | 0.2.0 | Adição do tópico 9 |  Gabriela Medeiros |


## 1. Introdução
### 1.1 Finalidade
Este documento abordará todos os aspectos técnicos, legais e demais requisitos sobre a aplicação Dr. Down, os quais não foram abordados nos demais documentos: documento de visão e documento de arquitetura.

### 1.2 Escopo
 Primeiramente estão definidos os requisitos não funcionais e em seguida estes requisitos estão dispostos em um diagrama NFR.


### 1.3 Definições, Acrônimos e Abreviações
| Abreviação  |  Definição  |
|   ---       |    ---      |
| SD          | Síndrome de Down |
|  CRIS DOWN  | Centro de Referência em Síndrome de Down |
|  NFR        | 	Non-Functional Requirement |

### 1.4 Referências
RESENDE, Angelica Aguiar. ANÁLISE DA VIABILIDADE TÉCNICA PARA DESENVOLVIMENTO DE APLICATIVO PARA O CENTRO DE REFERÊNCIA EM SÍNDROME DE DOWN (CRIS DOWN). 2017. 90 f. Trabalho de conclusão de curso (Graduação em Engenharia de Produção)- UNIVERSIDADE DE BRASÍLIA, Faculdade de Tecnologia Departamento de Engenharia de Produção, 2017.

## 2. Usabilidade
Um ponto essencial para a usabilidade do sistema proposto é que o mesmo ofereça um design e uma interação acessível aos portadores da SD.
Considerando a deficiência intelectual a que esses pacientes são acometidos, o sistema deverá presar por simplicidade e acesso intuitivo, tendo em vista sua importância para o ajustamento e uma utilização adequada dos usuários à aplicação. Para alcançar tal proposta, a aplicação deve conter um design limpo, de fácil vizualização e entendimento, com acesso rápido e intuitivo a informações e funcionalidades importantes, sempre utilizando-se de um linguagem de fácil entendimento e compreensão.

## 3. Confiabilidade
O sistema deverá ter alto nível de disponibilidade considerando a necessidade de acesso contínuo e frequente à aplicação. Tal requisito gerará um contexto em que falhas e bugs do sistema tenham a possibilidade de serem corrigidas rapidamente, pois esses erros podem gerar atrasos nos atendimentos e problemas administrativos no CRIS DOWN.

## 4. Portabilidade
O sistema deverá funcionar nos navegadores de internet Google Chrome e Apple Safari em dispositivos capazes de acessar a internet, que suportem os navegadores descritos e, também, que estejam equipados com sistema Windows, Linux, Mac, Android e iOS, ou seja, o sistema deve se adaptar visualmente ao ambiente desses sistemas.

## 5. Desempenho
O sistema deverá processar as requisições de acesso do usuário de maneira a aprimorar a sua experiência de uso e contribuindo para a eficiência dos atendimentos do CRIS DOWN.

## 6. Interoperabilidade
O sistema possuirá conexão com banco de dados externo para coletar dados de pacientes cadastrados e também deverá salvar suas informações de maneira não vinculada ao dispositivo utilizado pelo usuário.

## 7. Segurança
As informações de um usuário somente serão acessadas por ele mesmo ou outros usuários que possuam nível de acesso elevado. O sistema atenderá a todas as políticas de privacidade do usuário e buscará incluir boas práticas de segurança de informações.

## 8. Restrições de Design

### 8.1 Interface
- Simplista
- Intuitivo
- Informações objetivas
- Links de informações visíveis
### 8.2 Arquitetura
- Uso de class-based-views
### 8.3 Padrão de código
- PEP 8
- Doc strings
### 8.4 Ferramentas
- CodeClimate
- CookieCutter
- Docker


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
- Prontuário
- Questionário de risco médico

## 10. Diagrama NFR
O diagrama NFR ilustra os requisitos não funcionais e suas relações.

![Diagrama NFR](http://uploaddeimagens.com.br/images/001/351/080/full/nfr.png?1522336206)
