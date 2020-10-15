from collections import defaultdict

cubo_semantico = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: None))))

#ASSIGN
cubo_semantico['int']['int']['<'] = "int"
cubo_semantico['float']['float']['<'] = "float"
cubo_semantico['char']['char']['<'] = "char"

#GT
cubo_semantico['int']['int']['>'] = "int"
cubo_semantico['int']['float']['>'] = "int"
cubo_semantico['float']['int']['>'] = "int"
cubo_semantico['float']['float']['>'] = "int"
cubo_semantico['char']['char']['>'] = "int"

#LT
cubo_semantico['int']['int']['<'] = "int"
cubo_semantico['int']['float']['<'] = "int"
cubo_semantico['float']['int']['<'] = "int"
cubo_semantico['float']['float']['<'] = "int"
cubo_semantico['char']['char']['<'] = "int"

#NT
cubo_semantico['int']['int']['<>'] = "int"
cubo_semantico['int']['float']['<>'] = "int"
cubo_semantico['float']['int']['<>'] = "int"
cubo_semantico['float']['float']['<>'] = "int"
cubo_semantico['char']['char']['<>'] = "int"

#EQUAL
cubo_semantico['int']['int']['=='] = "int"
cubo_semantico['int']['float']['=='] = "int"
cubo_semantico['float']['int']['=='] = "int"
cubo_semantico['float']['float']['=='] = "int"
cubo_semantico['char']['char']['=='] = "int"

#AND
cubo_semantico['int']['int']['&'] = "int"

#OR
cubo_semantico['int']['int']['|'] = "int"

#PLUS
cubo_semantico['int']['int']['+'] = "int"
cubo_semantico['int']['float']['+'] = "float"
cubo_semantico['float']['int']['+'] = "float"
cubo_semantico['float']['float']['+'] = "float"

#MINUS
cubo_semantico['int']['int']['-'] = "int"
cubo_semantico['int']['float']['-'] = "float"
cubo_semantico['float']['int']['-'] = "float"
cubo_semantico['float']['float']['-'] = "float"

#TIMES
cubo_semantico['int']['int']['*'] = "int"
cubo_semantico['int']['float']['*'] = "float"
cubo_semantico['float']['int']['*'] = "float"
cubo_semantico['float']['float']['*'] = "float"

#DIVIDE
cubo_semantico['int']['int']['/'] = "int"
cubo_semantico['int']['float']['/'] = "float"
cubo_semantico['float']['int']['/'] = "float"
cubo_semantico['float']['float']['/'] = "float"


def cube_check(node, left, right):
    result = cubo_semantico[left][right][node]
    if result == None:
        return "error"
    else:
        return result