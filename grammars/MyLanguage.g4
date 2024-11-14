// Define grammar name
grammar MyLanguage;

// Lexer Rules
IF      : 'if';
ELSE    : 'else';
WHILE   : 'while';
PRINT   : 'print';
ASSIGN  : '=';
SEMI    : ';';
LPAREN  : '(';
RPAREN  : ')';
LBRACE  : '{';
RBRACE  : '}';
PLUS    : '+';
MINUS   : '-';
MULT    : '*';
DIV     : '/';

ID      : [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER  : [0-9]+;
WS      : [ \t\r\n]+ -> skip;

// Parser Rules
program         : (statement)* ;

statement
    : variableDeclaration
    | assignment
    | printStatement
    | ifStatement
    | whileStatement
    ;

variableDeclaration
    : 'int' ID SEMI
    ;

assignment
    : ID ASSIGN expression SEMI
    ;

printStatement
    : PRINT LPAREN expression RPAREN SEMI
    ;

ifStatement
    : IF LPAREN expression RPAREN block (ELSE block)?
    ;

whileStatement
    : WHILE LPAREN expression RPAREN block
    ;

block
    : LBRACE statement* RBRACE
    ;

expression
    : expression PLUS expression
    | expression MINUS expression
    | expression MULT expression
    | expression DIV expression
    | NUMBER
    | ID
    | LPAREN expression RPAREN
    ;
