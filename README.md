## DSL para Teste de API REST

Visamos nesse projeto escrever uma DSL simples para descrever testes de caixa preta de APIREST e um gerador que converte essa DSL em código Python de teste, só vamos demonstrar aqui, não chamaremos HTTPs reais, para termos a possibilidade de rodar em qualquer máquina.

## Estrutura

- ApiTest.g4: gramática ANTLR4 da DSL
- ApiTestLexer.py, ApiTestParser.py, ApiVisitor.py, ApiTestListener.py: arquivos gerados pelo ANTLR.
- ApiTestCustomVisitor.py: visitor que percorre a árvore sintática e constrói o modelo em Python.
- model.py: classes ApiSpec, Scenario e Case.
- generator.py: gera o arquivo test_api_generated.py a partir do modelo.
- main.py: compilador da DSL, que lê um .apitest e chama o gerador.
- exemplo.apitest: exemplo de especificação de testes.
- test_api_generated.py: exemplo de código gerado.

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

## Como executar

1. Criar ambiente virtual e instalar dependências:

python -m venv .venv
WIndows PowerShell:
. venv/Scripts/Activate.ps1
pip install -r requirements.txt

2. Gerar/regerar o parser:

antlr4-Dlanguage=Python3 =ApiTest.g4-visitor

3. Compilar o arquivo da DSL para código de teste:

python main.py

4. Executar o arquivo de teste gerado:

python test_api_generated.py

