## DSL para Teste de API REST

## Equipe
    - Erasmo Alves
    - Everton Ferreira
    - Gabriel Henrique

## Motivação

    Em testes de API REST é comum repetir sempre o mesmo padrão de escrever código para chamar endpoints, montar parâmetros, checar status de resposta e validar campos de JSON. Isso costuma ser verboso, pouco declarativo e espalha a lógica de teste em várias funções de uma linguagem de propósito geral(ex: Python com requests e pytest).
    Este projeto propõe uma linguagem de domínio específico(DSL) para descrever testes de caixa-preta de API REST de forma declarativa. Em vez de escrever código para cada teste, descreve-se cenários, casos de teste, requisições e expectativas em uma arquivo .apitest. Em seguida, um compilador gera automaticamente um arquivo Python de testes.
    A DSL é independente de ferramenta e foi construída com ANTLR4 + Python, seguindo a estrutura de um compilador: análise léxica, análise sintática, construção de árvore sintática, visitor orientado a sintaxe e gerador de código.

## Visão geral da linguagem
    A linguagem descreve testes de API REST com os seguintes conceitos principais:
    - base_url: URL base da API
    - scenario: um agrupamento lógico de casos de teste
    - case: um caso de teste específico dentro de um cenário
    - request: bloco que descreve como a requisição HTTP deve ser feita
    - expect: bloco que descreve as expectativas sobre a resposta(status e conteúdo JSON)

## Sintaxe da DSL(exemplo)

    base_url "https://api.exemplo.com"

    scenario "login básico"
    case "sucesso"
    request
    method GET
    path "/login"
    query { user: "joao", pass: "123" }
    expect
    status 200
    json_has "token"

    case "senha errada"
    request
    method GET
    path "/login"
    query { user: "joao", pass: "errado" }
    expect
    status 401
    json_eq "error" "invalid_credentials"

    Principais construções:

    base_url "...": define a URL base.

    scenario "nome": inicia um cenário.

    case "nome": define um caso de teste dentro do cenário atual.

    request seguido de:

    method GET|POST|PUT|DELETE

    path "/caminho"

    query { chave: valor, ... } com valores string ou inteiros.

    expect seguido de:

    status <código HTTP>

    json_has "campo" para exigir que um campo exista no JSON.
    
    json_eq "campo" "valorEsperado" para exigir que um campo tenha o valor esperado.

## Estrutura
    - ApiTest.g4: gramática ANTLR4 da DSL (regras léxicas e sintáticas).
    - ApiTestLexer.py, ApiTestParser.py, ApiTestVisitor.py, ApiTestListener.py: arquivos gerados automaticamente pelo ANTLR a partir da gramática.
    - ApiTestCustomVisitor.py: visitor customizado que percorre a árvore sintática e constrói um modelo em Python (ApiSpec, Scenario, Case).​
    - model.py: definição das classes de modelo (ApiSpec, Scenario, Case).
    - generator.py: recebe um ApiSpec e gera o arquivo test_api_generated.py com código Python de teste (modo simulado, sem chamadas HTTP reais).​
    - main.py: “compilador” da DSL, que lê um arquivo .apitest, executa o parser, o visitor e chama o gerador.
    - exemplo.apitest: exemplo de especificação de testes na DSL.
    - test_api_generated.py: arquivo de código de teste gerado a partir de exemplo.apitest.
    - requirements.txt: dependências Python do projeto.
    - .venv/ (opcional): ambiente virtual Python.​

## Como executar
1. Requisitos:
    - Python 3 instalado
    - Java + ANTLR4

2. Criar ambiente virtual e instalar dependências:
    No diretório do projeto:
    - python -m venv .venv
    No Windows(PowerShell):
    - . venv/Scripts/Activate.ps1
    Depois de ativar o ambiente:
    - pip install -r requirements.txt

3. Gerar/regerar o parser:
    Se necessário regerar os arquivos do ANTLR a partir de ApiTest.g4, execute o comando apropriado para sua instalação de ANTLR. Exemplo:
    - antlr4-Dlanguage=Python3=ApiTest.g4-visitor
    O comando irá gerar:
    - ApiTestLexer.py
    - ApiTestParser.py
    - ApiTestVisitor.py
    - ApiTestListener.py
    Esses arquivos estão na mesma pasta que main.py.

4. Compilar o arquivo da DSL para código de teste:
    O arquivo de entrada padrão é exemplo.apitest, que deve estar na mesma pasta de main.py. Para gerar o código de teste:
    - python main.py

5. Executar o arquivo de teste gerado:
    - python test_api_generated.py

    O arquivo gerado executa os casos de teste em modo demonstração: em vez de chamar uma API real, ele simula respostas e imprime na tela as informações de cada teste (nome do cenário, nome do caso, status esperado, campos esperados etc.).

