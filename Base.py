from sly import Lexer
from sly import Parser

class Duck2020Lexer(Lexer):
    tokens = { PROGRAM, ID, VAR, INT, FLOAT, ASSIGN, GT, LT, NT, IF, ELSE, PLUS, MINUS, TIMES, DIVIDE, CTEINT, CTEFLOAT, \
    CTESTRING, CTECHAR, PRINT, MAIN, CHAR, EQUAL, AND, OR, LINE, POINT, CIRCLE, ARC, PENUP, PENDOWN, COLOR, SIZE, CLEAR, DO, WHILE, \
    FOR, TO, VOID, MODULE, RETURN, READ, WRITE}

    literals = { ';', ':', '(', ')', '{', '}',',' }

    ignore = ' \t'

    PROGRAM = r'program'
    MAIN    = r'main'
    VAR     = r'var'
    INT     = r'int'
    FLOAT   = r'float'
    CHAR    = r'char'
    PRINT   = r'print'
    VOID    = r'void'
    MODULE  = r'module'
    RETURN  = r'return'
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
    READ    = r'read'
    WRITE   = r'write'
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


class semantic:
    
    def __init__(self)
        self.semanticv = []
        self.scope = "global"

    def addSemantic(self, scope, name, value):
        for data in self.semanticv:
            if data[0] == scope:
                if data[1] == name:
                    return False
        self.semanticv.append([scope, name, value])
        return True


class Duck2020Parser(Parser):
    
    tokens = Duck2020Lexer.tokens
    
    #[Scope, name, value]

    #Programa
    @_('PROGRAM ID programa_accion ";" vars programa2 mainfuncion', 'PROGRAM ID programa_accion ";" programa2 mainfuncion')
    def programa(self, p):
        print("Probando Id del programa", p.ID)
        pass

    @_('')
    def programa_accion(self, p):
        print("buenas",p[-2])
        semantica.addSemantic(p[-2], p[-1], p[-1])
        print("Semantic", semantica.semanticv)

    @_('funcion programa2', '')
    def programa2(self, p):
        pass

    #vars ---------------unreachable
    @_('VAR vars2')
    def vars(self, p):
        pass

    @_('tipos vars3', '')
    def vars2(self, p):
        pass

    @_('":" ID vars4 ";" vars2', 'ID vars4 ";" vars2')
    def vars3(self, p):
        pass

    @_('"," ID vars4', '')
    def vars4(self, p):
        pass

    #Tipos  --------------Probable marca no reachable
    @_('INT', 'FLOAT', 'CHAR')
    def tipos(self, p):
        pass

    #Main --------------Faltan los diagramas
    @_('MAIN "{" estatuto mainfuncion2 "}"')
    def mainfuncion(self, p):
        pass

    @_('estatuto mainfuncion2', '')
    def mainfuncion2(self, p):
        pass

    #Fucion
    @_('funcionvoid', 'funciontipo')
    def funcion(self, p):
        pass

    #FuncionVoid
    @_('VOID MODULE ID "(" funcionvoid2 ")" vars "{" estatuto funcionvoid4 "}"', 'VOID MODULE ID "(" funcionvoid2 ")" "{" estatuto funcionvoid4 "}"')
    def funcionvoid(self, p):
        pass

    @_('parametro funcionvoid3', '')
    def funcionvoid2(self, p):
        pass

    @_('"," parametro funcionvoid3', '')
    def funcionvoid3(self, p):
        pass

    @_('estatuto funciontipo4', '')
    def funcionvoid4(self, p):
        pass

    #FuncionTipo
    @_('tipos MODULE ID "(" funciontipo2 ")" vars "{" estatuto funciontipo4 RETURN expresion "}"', 'tipos MODULE ID "(" funcionvoid2 ")" "{" estatuto funciontipo4 "}"')
    def funciontipo(self, p):
        pass

    @_('parametro funciontipo3', '')
    def funciontipo2(self, p):
        pass

    @_('"," parametro funciontipo3', '')
    def funciontipo3(self, p):
        pass

    @_('estatuto funciontipo4', '')
    def funciontipo4(self, p):
        pass

    #Parametro
    @_('tipos expresion')
    def parametro(self, p):
        pass

    #Estatuto
    @_('lectura', 'escritura', 'asignacion', 'decision', 'repeticion', 'funcionesp')
    def estatuto(self, p):
        pass

    #Lectura
    @_('READ "(" expresion lectura2 ")" ";"')
    def lectura(self, p):
        pass

    @_('"," expresion lectura2', '')
    def lectura2(self, p):
        pass

    #Escritura
    @_('WRITE "(" expresion escritura2 ")" ";"', 'WRITE "(" CTESTRING escritura2 ")" ";"')
    def escritura(self, p):
        pass

    @_('"," expresion escritura2', 'CTESTRING escritura2', '')
    def escritura2(self, p):
        pass

    #Asignacion
    @_('ID ASSIGN expresion ";"')
    def asignacion(self, p):
        pass

    #Repeticion
    @_('rcondicional', 'rncondicional')
    def repeticion(self, p):
        pass

    #RCondicional
    @_('DO "(" expresion ")" WHILE "{" estatuto rcondicional2 "}"')
    def rcondicional(self, p):
        pass

    @_('estatuto rcondicional2', '')
    def rcondicional2(self, p):
        pass

    #RNCondicional
    @_('FOR ID ASSIGN exp TO exp DO "{" estatuto rncondicional2 "}"')
    def rncondicional(self, p):
        pass

    @_('estatuto rncondicional2', '')
    def rncondicional2(self, p):
        pass

    #Decision
    @_('IF "(" expresion ")" "{" estatuto decision2 "}"', 'IF "(" expresion ")" "{" estatuto decision2 "}" ELSE "{" estatuto decision2 "}"')
    def decision(self, p):
        pass

    @_('estatuto decision2', '')
    def decision2(self, p):
        pass

    #FuncionesESP
    @_('LINE "(" exp "," exp ")"', 'POINT "(" exp "," exp ")"', 'CIRCLE "(" exp ")"', 'ARC "(" exp "," exp "," exp ")"', 'PENUP "(" ")"', 'PENDOWN "(" ")"', 'COLOR "(" exp ")"', 'SIZE "(" exp ")"', 'CLEAR "(" ")"')
    def funcionesp(self, p):
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
    semantica = semantic()
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
