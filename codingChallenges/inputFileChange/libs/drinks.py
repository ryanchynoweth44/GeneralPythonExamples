
class Drinks():

    __instance = None
    
    @staticmethod
    def getInstance():
        """ Static access method. """
        if Drinks.__instance == None:
            Drinks()
        return Drinks.__instance 

    def __init__(self, drinks):
        """ Virtually private constructor. """
        if Drinks.__instance != None:
            raise Exception("Class already exists.")
        else:
            Drinks.__instance = self
            Drinks.drinks = drinks
    
    def get_drink_by_id(self, id):
        assert type(id) == str
        return next((d for d in self.drinks if d.get('id')==id), None)

    def get_drinks_by_type(self, drink_type):
        assert type(drink_type) == str
        return [d for d in self.drinks if d.get('type')==drink_type]

    def get_drinks_by_flavor(self, flavor):
        assert type(drink_type) == str
        return [d for d in self.drinks if d.get('flavor')==flavor]

    def __generate_id(self):
        ids = [int(d.get('id')) for d in self.drinks]
        return str(max(ids)+1)

    def add_drink(self, drink_type, flavor):
        drink_types = self.get_drinks_by_type(drink_type)
        existing = False
        for d in drink_types:
            if d.get('flavor') == flavor:
                existing = True
        
        if not existing:
            self.drinks.append({"id": self.__generate_id(), "type": drink_type, 'flavor': flavor})
        else :
            return 'Drink Already Exists.'

    
    def list_drinks(self):
        return self.drinks