import ply.lex as lex
import ply.yacc as yacc
import sys

'''
Tokenization = process of converting a sequence of 
characters into a sequence of tokens
A program that performs lexical-analysis/Tokenization may be termed a lexer, tokenizer
'''

tokens = [
    
    'INT',
    'DOUBLE',
    'CHAR',
    'STRING',
    'BOOL',

    'DISPLAY',#Display
    'ASSIGN',#=
    'COMMA',#,
    
    #expressions
    'PLUS',#+
    'MINUS',#-
    'DIVIDE',#/
    'MULTIPLY',#*
    'POW',#^
    'PERCENTAGE',#%
    'PLUSPLUS',#++
    'MINUSMINUS',#--

    #logical operators
    'LESSTHAN', #<
    'GREATERTHAN', #>
    'LESSEQUAL', #<=
    'GREATEREQUAL', #>=
    'NOTEQUAL',#!=
    'EQUALS',#==
    'NOT',#NOT
    'AND',#AND
    'OR',#OR

    #NESTED PARATHESIS
    'RSQBRAC',#]
    'LSQBRAC',#[
    'RCURLY', # }
    'LROUND', # (
    'RROUND', # )
    'LCURLY', # {
    'DOT', #.
    
    
    #type
    'TYPE', #int double string char bool
    'SEMICOLON', #end of line
    'IDENTIFIER', #variable function name
    'NEWLINE',
]
t_SEMICOLON = r'\;'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIVIDE = r'\/'
t_MULTIPLY = r'\*'
t_POW = r'\^'
t_PERCENTAGE = r'\%'
t_PLUSPLUS = r'\++'
t_MINUSMINUS = r'\--'


t_ASSIGN = r'='
t_LESSTHAN = r'\<'
t_GREATERTHAN = r'\>'
t_LESSEQUAL = r'\<\='
t_GREATEREQUAL = r'\>\='
t_NOTEQUAL = r'\!\='
t_EQUALS = r'\=\='
t_DOT = r'\.'

t_COMMA = r'\,'
t_NOT = r'not'
t_AND = r'and'
t_OR = r'or'
t_ignore = r' '#ignoring spaces

t_RSQBRAC = r'\]'
t_LSQBRAC = r'\['
t_RCURLY = r'\}'
t_LROUND = r'\{'
t_RROUND = r'\)'
t_LCURLY = r'\('

# token is a string with an assigned and thus identified meaning

def t_NEWLINE(token):#handle new lines
    r'\n'
    #\n escapes endline
    token.lexer.lineno += 1
    pass

def t_TYPE(token):
    r'int|double|string|char|bool'
    return token

def t_BOOL(token):
    r'True|False'
    return token

def t_INT(token):
    r'\d+'
    #\d means matching digits from 0-9 and + means that could be 1 to many
    token.value = int(token.value)
    return token

def t_DOUBLE(token):
    r'\d+\.\d+' #any character followed by a dot and zero or many characters
    token.value = float(token.value)
    return token

def t_STRING(token):
    r'\"[a-zA-Z0-9_]+\"'
    return token 

def t_CHAR(token):
    r'\'[a-zA-Z0-9_] \''
    return token

def t_DISPLAY(token):
    r'display'
    return token

def t_IDENTIFIER(token):#variable function names
    r'[a-zA-Z][A-Za-z_]*' 
    #[]contains a set of characters to match, [a-z]matches any alphabet from a-z
    #[a-zA-Z] matches characters from a-z and A-Z
    #a* a could be 0 or more time
    #a+ a could be 1 or more time
    return token

def t_error(t):
    print("illegal characters")
    t.lexer.skip(1)

# #LEXER TESTING
# lexer = lex.lex()

# lexer.input("{}[]()")

# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)