Testes
======

Nesta seção iremos demonstrar alguns processos de teste da aplicação Dr. Down, além de mostrar como você pode escrever os seus próprios testes.
A aplicação Dr. Down vem com duas suítes de teste python instaladas e configuradas, sendo uma o py.test e a outra o coverage.
Antes de explicar por menor as suítes de teste vamos ver como são feitos os testes em python/Django.

Testes python/Django
--------------------

O Django provê ao desenvolvedor diversas formas de testar sua aplicação, diversas ferramentas *third-party* também estão disponíveis para auxiliar na tarefa dos testes.
Testar uma aplicação web é uma tarefa complexa, porque uma aplicação web é feita por diversas camadas lógicas – vai do nível de uma requisição HTTP, a uma validação e processamento de um formulário, até a renderização de um template. Com a execução de teste em Django e dispondo de diversas utilidades, você pode simular requisições, inserir informações testes, inspecionar saídas de sua aplicação e geralmente verificar se seu código está fazendo o que ele deveria fazer.
Por padrão os testes Django devem estar na pasta ``tests/`` do seu app, com isso as ferramentas reconhecem como teste do seu código e são executadas.
Algumas documentações de referência são:

.. _`Escrevendo e Executando Testes`: https://docs.djangoproject.com/pt-br/2.0/topics/testing/overview/

.. _`Testes Unitários`: https://docs.djangoproject.com/pt-br/2.0/internals/contributing/writing-code/unit-tests/

`Escrevendo e Executando Testes`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Testes Unitários`_
^^^^^^^^^^^^^^^^^^^

Testando Dr. Down
-----------------

py.test:
^^^^^^^^

Para apenas rodar a suíte de testes com o py.test basta executar o seguinte comando::

    $ docker-compose -f local.yml run --rm django py.test

.. _py.test: https://docs.pytest.org/en/latest/contents.html

**Observação**: No próprio terminal será mostrado o *output* dos testes rodados. Outras configurações, *flags* e modos de uso do py.test podem ser verificadas na documentação do py.test_.


coverage:
^^^^^^^^^

O Coverage é uma ferramenta auxiliar que permite gerar relatórios e verifcar a cobertura de código a partir dos testes executados. Tanto que para isso ele usa o auxílio do py.test, no entanto, há forma de executar apenas o coverage, ou até usar de outros *frameworks* de teste, mas nesse projeto utilizamos ele em conjunto com o py.test, sua execução se dá da seguinte forma::

    $ docker-compose -f local.yml run --rm django coverage run -m py.test
    $ docker-compose -f local.yml run --rm django coverage html
    $ firefox htmlcov/index.html

Com estes comandos o coverage irá executar o testes com auxílio do py.test, vai utilizar os dados dele como input para gerar a cobertura de testes e mostrar ao usuário.

.. _coverage: https://coverage.readthedocs.io/en/coverage-4.5.1/

**Observação**: Será gerada uma pasta ``htmlcov/`` que conterá o ``index.html``, este arquivo contem o relatório extraído dos testes rodados, no exemplo acima foi utilizado o navegador *Mozilla Firefox* para a abertura do arquivo HTML gerado. Outras configurações, *flags* e modos de uso do coverage podem ser verificadas na documentação do coverage_.

.. _github: https://github.com/fga-gpp-mds/2018.1-Dr-Down

Dúvidas ou problemas, acesse nosso github_ e fique a vontade para abrir uma *issue* para que possamos esclarecer!
