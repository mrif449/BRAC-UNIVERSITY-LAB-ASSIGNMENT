%{
#include <stdio.h>
#include <stdlib.h>
#include "symbol_table.h"

extern FILE *yyin;
int yylex(void);
void yyerror(const char *);

SymbolTable symbol_table;

int error_count = 0; 
int line_count = 1; 

%}

%union {
    symbol_info *info;
}

%token IF ELSE FOR WHILE DO BREAK INT CHAR FLOAT DOUBLE VOID RETURN SWITCH CASE DEFAULT CONTINUE PRINTLN ADDOP MULOP INCOP DECOP RELOP ASSIGNOP LOGICOP NOT LPAREN RPAREN LCURL RCURL LTHIRD RTHIRD COMMA SEMICOLON CONST_INT CONST_FLOAT ID

%nonassoc LOWER_THAN_ELSE
%nonassoc ELSE

%%
program : statements
        ;

statements : statement
           | statements statement
           ;

statement : expression
          | return_statement
          ;

expression : IDENTIFIER
           | INTEGER
           | LBRACKET expression RBRACKET
           ;

return_statement : RETURN expression
                 ;

external_declaration:
      type_specifier declarator_list SEMICOLON
    | type_specifier function_definition

type_specifier:
      INT
    | FLOAT
    | VOID

declarator_list:
      declarator
    | declarator_list COMMA declarator

declarator:
      IDENTIFIER
    | IDENTIFIER LBRACKET INTEGER RBRACKET

function_definition:
      type_specifier IDENTIFIER LPAREN parameter_list RPAREN compound_statement

parameter_list:
    | parameter_list_nonempty

parameter_list_nonempty:
      parameter_declaration
    | parameter_list_nonempty COMMA parameter_declaration

parameter_declaration:
      type_specifier IDENTIFIER

compound_statement:
      LBRACE statement_list RBRACE

statement_list:
    | statement_list statement

statement:
      expression SEMICOLON
    | declaration
    | compound_statement
    | selection_statement
    | iteration_statement
    | return_statement

declaration:
      type_specifier declarator_list SEMICOLON

selection_statement:
        IF LPAREN expression RPAREN statement ELSE statement 

iteration_statement:
    WHILE LPAREN expression RPAREN statement
    | FOR LPAREN expression_opt SEMICOLON expression_opt SEMICOLON expression_opt RPAREN statement

expression_opt:
    | expression
    | argument_list COMMA expression

%%

void yyerror(const char *s) {
    fprintf(stderr, "Syntax error at line %d: %s\n", line_count, s);
}

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <input_file>\n", argv[0]);
        return 1;
    }

    FILE *f = fopen(argv[1], "r");
    if (!f) {
        perror("fopen");
        return 1;
    }

    yyin = f;
    yyparse();

    fclose(f);

    FILE *log_file = fopen("20101363_log.txt", "w");
    if (!log_file) {
        perror("fopen");
        return 1;
    }

    writeLog(log_file);

    fclose(log_file);

    FILE *error_file = fopen("20101363_error.txt", "w");
    if (!error_file) {
        perror("fopen");
        return 1;
    }

    writeErrors(error_file);

    fclose(error_file);

    printf("Total errors: %d\n", error_count);

    return 0;
}
