from sly import Lexer
from sly import Parser

class Duck2020Lexer(Lexer):
    tokens = { PROGRAM, ID, VAR, INT, FLOAT, ASSIGN, GT, LT, NT, IF, ELSE, PLUS, MINUS, TIMES, DIVIDE, CTEINT, CTEFLOAT, \
    CTESTRING, CTECHAR, PRINT, MAIN, CHAR, EQUAL, AND, OR, LINE, POINT, CIRCLE, ARC, PENUP, PENDOWN, COLOR, SIZE, CLEAR, DO, WHILE, \
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
    CTECHAR = r'[a-zA-Z_]'
    CTESTRING = r'\".*?\"'




class Duck2020Parser(Parser):
    
    tokens = Duck2020Lexer.tokens

    

    #Parametro
    @_('tipos espresion')
    def Parametro(self, p):
        pass

    #Estatuto
    @_('lectura', 'escritura', 'asignacion', 'decision', 'repeticion', 'funcionesp')
    def estatuto(self, p):
        pass

    #Lectura
    @_('read "(" expresion lectura2 ")" ";"')
    def lectura(self, p):
        pass

    @_('","expresion lectura 2', '')
    def lectura2(self, p):
        pass

    #Escritura
    @_('write "(" expresion escritura2 ")" ";"', 'write( CTESTRING escritura2 ")" ";"')
    def escritura(self, p):
        pass

    @_('"," expresion escritura2', 'CTESTRING escritura2', '')
    def escritura2(self, p):
        pass

    #Asignacion
    @_('id ASSIGN expresion ";"')
    def asignacion(self, p):
        pass

    #Repeticion
    @_('rcondicional', 'rncondicional')
    def repeticion(self, p):
        pass

    #RCondicional
    @_('do "(" expresion ")" while "{" estatuto rcondicional2 "}"')
    def rcondicional(self, p):
        pass

    @_('estatuto rcondicional2', '')
    def rcondicional2(self, p):
        pass

    #RNCondicional
    @_('for id = exp to exp do "{" estatuto rncondicional2 "}"')
    def rncondicional(self, p):
        pass

    @_('estatuto rncondicional2', '')
    def rncondicional2(self, p):
        pass

    #Decision
    @_('if "(" expresion ")" "{" estatuto decision2 "}"', 'if "(" expresion ")" "{" estatuto decision2 "}" else "{" estatuto decision2 "}"')
    def decision(self, p):
        pass

    @_('estatuto decision2', '')
    def decision2(self, p):
        pass

    #FuncionesESP
    @_('line "(" exp "," exp ")"', 'point "(" exp "," exp ")"', 'circle "(" exp ")"', 'arc "(" exp "," exp "," exp ")"', 'penup "(" ")"', 'pendown "(" ")"', 'color "(" exp ")"', 'size "(" exp ")"', 'clear "(" ")"')
    def funcioneesp(self, p):
        pass

    #Expresion
    @_('exp', 'exp GT exp', 'exp LT exp', 'exp NT exp', 'exp EQUAL exp', 'exp AND exp', 'exp OR exp')
    def expresion(self, p):
        pass

    #EXP
    @_('termino exp2')
    def exp(self, p):
        pass

    @_('PLUS termino', 'MINUS termino', '')
    def exp2(self, p):
        pass

    #Termino
    @_('factor termino2')
    def termino(self, p):
        pass

    @_('TIMES factor', "DIVIDE factor", '')
    def termino2(self, p):
        pass

    #FACTOR
    @_('"(" expresion ")"', 'factor2 varcte')
    def factor(self, p):
        pass

    @_('PLUS', 'MINUS', '')
    def factor2(self, p):
        pass


    #VARCTE 
    #El problema de VARCTE es que no se pueden llamar funciones sin parametros se tendria que modificar la regla para que accepte
    #Tambien verificar que el token declarado de char sea el correcto, ya que no se puede verficar por el ID
    @_('CTEINT', 'CTEFLOAT', 'CTECHAR', 'ID varcte2')
    def varcte(self, p):
        pass

    @_('"(" ID varcte3 ")"', '')
    def varcte2(self, p):
        pass

    @_('"," ID varcte3', '')
    def varcte3(self, p):
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

    # file = open("test.txt", 'r')
    # masterline = ""

    # for line in file:
    #     masterline = masterline + line.strip()

    lexer = Duck2020Lexer()
    parser = Duck2020Parser()
    # result = parser.parse(lexer.tokenize(masterline))
    # print(result)
    while True:
        try:
            text = input('duck > ')
            result = parser.parse(lexer.tokenize(text))
            print(result)
            # for line in file:
            #     result = parser.parse(lexer.tokenize(line.strip()))
            #     print(result)

        except EOFError:
            break
    
    # file.close()


#-----------Main original
    # if __name__ == '__main__':

    # file = open("test.txt", 'r')
    # masterline = ""

    # for line in file:
    #     masterline = masterline + line.strip()

    # lexer = Duck2020Lexer()
    # parser = Duck2020Parser()
    # result = parser.parse(lexer.tokenize(masterline))
    # print(result)
    # # while True:
    # #     try:
    # #         text = input('duck > ')
    # #         result = parser.parse(lexer.tokenize(text))
    # #         print(result)
    # #         # for line in file:
    # #         #     result = parser.parse(lexer.tokenize(line.strip()))
    # #         #     print(result)

    # #     except EOFError:
    # #         break
    
    # file.close()
