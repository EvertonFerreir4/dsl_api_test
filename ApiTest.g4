grammar ApiTest;

// =========================
// REGRAS LÉXICAS (tokens)
// =========================

// PALAVRAS-CHAVE
BASE_URL  : 'base_url';
SCENARIO  : 'scenario';
CASE      : 'case';
REQUEST   : 'request';
EXPECT    : 'expect';
METHOD    : 'method';
PATH      : 'path';
QUERY     : 'query';
STATUS    : 'status';
JSON_HAS  : 'json_has';
JSON_EQ   : 'json_eq';

// MÉTODOS HTTP
HTTP_METHOD
  : 'GET' | 'POST' | 'PUT' | 'DELETE'
  ;

// SÍMBOLOS
COLON   : ':';
COMMA   : ',';
LBRACE  : '{';
RBRACE  : '}';

// IDENTIFICADOR simples (para chaves de query)
ID      : [a-zA-Z_][a-zA-Z_0-9]* ;

// NÚMEROS
INT     : [0-9]+ ;

// STRINGS entre aspas duplas
STRING
  : '"' (~["\r\n])* '"'
  ;

// QUEBRAS DE LINHA
NEWLINE : '\r'? '\n' ;

// ESPAÇOS E TABS ignorados
WS : [ \t]+ -> skip ;

// =========================
// REGRAS SINTÁTICAS (parser)
// =========================

// Arquivo de especificação: base_url opcional + 1 ou mais cenários
spec
  : baseDecl? scenarioDecl+ EOF
  ;

// base_url "https://api.exemplo.com"
baseDecl
  : BASE_URL STRING NEWLINE+
  ;

// scenario "nome do cenário"
scenarioDecl
  : SCENARIO STRING NEWLINE+ caseDecl+
  ;

// case "nome do caso"
caseDecl
  : CASE STRING NEWLINE+ requestBlock expectBlock
  ;

// Bloco de request
// request
// method GET
// path "/login"
// query { user: "joao", pass: "123" }
requestBlock
  : REQUEST NEWLINE+ requestItem+
  ;

requestItem
  : methodDecl
  | pathDecl
  | queryDecl
  ;

// method GET
methodDecl
  : METHOD HTTP_METHOD NEWLINE+
  ;

// path "/login"
pathDecl
  : PATH STRING NEWLINE+
  ;

// query { user: "joao", pass: "123" }
queryDecl
  : QUERY LBRACE queryPair (COMMA queryPair)* RBRACE NEWLINE+
  ;

queryPair
  : ID COLON value
  ;

// Bloco de expect
// expect
// status 200
// json_has "token"
// json_eq "campo" "valorEsperado"
expectBlock
  : EXPECT NEWLINE+ expectItem+
  ;

expectItem
  : statusDecl
  | jsonHasDecl
  | jsonEqDecl
  ;

// status 200
statusDecl
  : STATUS INT NEWLINE+
  ;

// json_has "token"
jsonHasDecl
  : JSON_HAS STRING NEWLINE+
  ;

// json_eq "campo" "valor"
jsonEqDecl
  : JSON_EQ STRING STRING NEWLINE+
  ;

// valor genérico (string ou número)
value
  : STRING
  | INT
  ;
