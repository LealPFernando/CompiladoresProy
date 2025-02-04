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


print(cubo_semantico['int']['float']['+'])



# class semantic:
    
#     def __init__(self):
#         self.semanticv = []

#     def addsem(self, scope, name, value):
#         for data in self.semanticv:
#             if data[0] == scope:
#                 if data[1] == name:
#                     return False
#         self.semanticv.append([scope, name, value])
#         return True



# semantic = semantic()

# if semantic.addsem("global", "x", 5):
#     print(semantic.semanticv)

# else:
#     print("error")
    

# if semantic.addsem("global", "a", 5):
#     print(semantic.semanticv)

# else:
#     print("error")

