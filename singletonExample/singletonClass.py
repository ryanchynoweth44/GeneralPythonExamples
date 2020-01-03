

class MySingleton:
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if MySingleton.__instance == None:
            MySingleton()
        return MySingleton.__instance 

    def __init__(self, val1, val2):
        """ Virtually private constructor. """
        if MySingleton.__instance != None:
            raise Exception("This class is a MySingleton!")
        else:
            MySingleton.__instance = self
            MySingleton.val1 = val1
            MySingleton.val2 = val2