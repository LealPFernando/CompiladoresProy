class semantic:
    
    def __init__(self):
        self.semanticv = []

    def addsem(self, scope, name, value):
        for data in self.semanticv:
            if data[0] == scope:
                if data[1] == name:
                    return False
        self.semanticv.append([scope, name, value])
        return True



semantic = semantic()

if semantic.addsem("global", "x", 5):
    print(semantic.semanticv)

else:
    print("error")
    

if semantic.addsem("global", "a", 5):
    print(semantic.semanticv)

else:
    print("error")