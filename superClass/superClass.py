



class SuperClass():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def superFunction(self, addition=100):
        return self.a+addition


    def overwriteFunction(self):
        return self.a + self.b + self.c

    def overloadFunction(self):
        return self.b