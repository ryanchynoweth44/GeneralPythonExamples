from superClass.superClass import SuperClass


class SubClass(SuperClass):

    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.d = d 


    def overwriteFunction(self):
        return self.a + self.d


    def anotherfunction(self, addition=100):
        return self.superFunction(addition)


    def overloadFunction(self, addition=30):
        return self.b+addition