from sly import Lexer
from sly import Parser

class Duck2020Lexer(Lexer):
    tokens = { PROGRAM, ID, VAR, INT, FLOAT, ASSIGN, GT, LT, NT, IF, ELSE, PLUS, MINUS, TIMES, DIVIDE, CTEINT, CTEFLOAT, \
    CTESTRING, PRINT, MAIN, CHAR, EQUAL, AND, OR, LINE, POINT, CIRCLE, ARC, PENUP, PENDOWN, COLOR, SIZE, CLEAR, DO, WHILE, \
    FOR, TO}

    literals = { ';', ':', '(', ')', '{', '}',',' }

    ignore = ' \t'

    PROGRAM = r'program'
    MAIN    = r'main'
    VAR     = r'var'
    INT     = r'int'
    FLOAT   = r'float'
    CHAR    = r'char'
    PRINT   = r'print'
    IF      = r'if'
    ELSE    = r'else'
    LINE    = r'line'
    POINT   = r'point'
    CIRCLE  = r'circle'
    ARC     = r'arc'
    PENUP   = r'penup'
    PENDOWN = r'pendown'
    COLOR   = r'color'
    SIZE    = r'size'
    CLEAR   = r'clear'
    DO      = r'do'
    WHILE   = r'while'
    FOR     = r'for'
    TO      = r'to'
    ID      = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ASSIGN  = r'='
    GT      = r'>'
    LT      = r'<'
    NT      = r'<>'
    EQUAL   = r'=='
    AND     = r'&'
    OR      = r'\|'
    PLUS    = r'\+'
    MINUS   = r'-'
    TIMES   = r'\*'
    DIVIDE  = r'/'
    CTEFLOAT  = r'\d+\.\d+'
    CTEINT  = r'\d+'
    CTESTRING = r'\".*?\"'




class Duck2020Parser(Parser):
    
    tokens = Duck2020Lexer.tokens

    @_('PROGRAM ID ";" vars bloque', 'PROGRAM ID ";" bloque')
    def programa(self, p):
        pass

    @_('VAR vars2')
    def vars(self, p):
        pass

    @_('ID vars3 ":" tipo ";" vars4')
    def vars2(self, p):
        pass

    @_('"," ID vars3', '"," ID', '')
    def vars3(self, p):
        pass

    @_('vars2', '')
    def vars4(self, p):
        pass

    @_('INT', 'FLOAT')
    def tipo(self, p):
        pass

    @_('"{" estatuto bloque2 "}"', '"{" "}"')
    def bloque(self, p):
        pass

    @_('estatuto bloque2','estatuto', '')
    def bloque2(self, p):
        pass

    @_('asignacion', 'condicion', 'escritura')
    def estatuto(self, p):
        pass

    @_('ID ASSIGN expresion ";"')
    def asignacion(self, p):
        pass

    @_('PRINT "(" escritura2 escritura3 ")" ";"')
    def escritura(self, p):
        pass

    @_('expresion', 'CTESTRING')
    def escritura2(self, p):
        pass

    @_('"," escritura2 escritura3', '"," escritura2', '')
    def escritura3(self, p):
        pass

    @_('IF "(" expresion ")" bloque ELSE bloque ";"', 'IF "(" expresion ")" bloque ";"')
    def condicion(self, p):
        pass

    @_('exp GT exp', 'exp LT exp', 'exp NT exp', 'exp')
    def expresion(self, p):
        pass

    @_('termino exp2')
    def exp(self, p):
        pass

    @_('PLUS exp', 'MINUS exp', '')
    def exp2(self, p):
        pass

    @_('factor termino2')
    def termino(self, p):
        pass

    @_('TIMES factor', 'DIVIDE factor', '')
    def termino2(self, p):
        pass

    @_('"(" expresion ")"','PLUS varcte', 'MINUS varcte', 'varcte', '')
    def factor(self, p):
        pass

    @_('ID', 'CTEINT', 'CTEFLOAT')
    def varcte(self, p):
        pass


# if __name__ == '__main__':
#     lexer = Duck2020Lexer()
#     parser = Duck2020Parser()
#     while True:
#         try:
#             text = input('duck2020 > ')
#         except EOFError:
#             break
#         if text:
#             lex = lexer.tokenize(text)
#             for token in lex:
#                 print(token)


if __name__ == '__main__':

    file = open("test.txt", 'r')
    masterline = ""

    for line in file:
        masterline = masterline + line.strip()

    lexer = Duck2020Lexer()
    parser = Duck2020Parser()
    result = parser.parse(lexer.tokenize(masterline))
    print(result)
    # while True:
    #     try:
    #         text = input('duck > ')
    #         result = parser.parse(lexer.tokenize(text))
    #         print(result)
    #         # for line in file:
    #         #     result = parser.parse(lexer.tokenize(line.strip()))
    #         #     print(result)

    #     except EOFError:
    #         break
    
    file.close()
