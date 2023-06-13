import ply.lex as lex
import sys

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'do' : 'DO', 
    'int': 'INT',
    'read': 'READ',
    'write': 'WRITE',
    'def' : 'DEF',
    'main': 'MAIN',
    'int' : 'INT'
}

literals = ['=',
            '+', '-', '*', '/', '%',
            '(', ')', '[', ']', '{', '}',
            ',', ';','<','>','!',
            ]

tokens = ['NUM', 'STR', 'AND', 'OR', 'NOT', 'EQ', 'NEQ', 'GEQ', 'LEQ', 'ID'] + list(reserved.values())


def t_ID(t):
     r'[a-z_][a-zA-Z_0-9]*'
     t.type = reserved.get(t.value,'ID')    # Check for reserved words
     return t

t_STR = r'"[\s\S]*"'
t_AND = r'&&'
t_OR = r'\|\|'
t_EQ = r'=='
t_NEQ = r'!='
t_GEQ = r'>='
t_LEQ = r'<='

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t\n'

#t_ignore_COMMENT = r'\#.*'


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error handling rule
def t_error(t):
    print(f'Illegal character {t.value[0]}')
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

inputfile = open(sys.argv[1], 'r', encoding="UTF-8")
lexer.input(inputfile.read())
for tok in lexer:
    #print(tok)
    pass