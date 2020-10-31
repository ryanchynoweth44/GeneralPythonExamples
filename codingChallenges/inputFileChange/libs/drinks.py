
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

    def reload(self, drinks):
        """ Used to reload data for tests """
        self.drinks = drinks
    
    def get_drink_by_id(self, id):
        assert type(id) == str
        return next((d for d in self.drinks if d.get('id')==id), None)

    def get_drinks_by_type(self, drink_type):
        assert type(drink_type) == str
        return [d for d in self.drinks if d.get('type')==drink_type]

    def get_drinks_by_flavor(self, flavor):
        assert type(flavor) == str
        return [d for d in self.drinks if d.get('flavor')==flavor]

    def get_drinks_by_flavor_and_type(self, flavor, drink_type):
        assert type(drink_type) == str
        assert type(flavor) == str
        return next((d for d in self.drinks if d.get('flavor')==flavor and d.get('type')==drink_type), None)

    def __generate_id(self):
        ids = [int(d.get('id')) for d in self.drinks]
        return str(max(ids)+1)

    def add_drink(self, drink_type, flavor):
        """ Adds a drink if it does not exists. Returns drink id whether existing or not """
        existing = False if self.get_drinks_by_flavor_and_type(flavor, drink_type) is None else True        
        if not existing:
            drink_id = self.__generate_id()
            print("Adding Drink Id: {}".format(drink_id))
            self.drinks.append({"id": drink_id, "type": drink_type, 'flavor': flavor})
            return drink_id
        else :
            drink_id = self.get_drinks_by_flavor_and_type(flavor, drink_type).get('id')
            print("Drink exists. Id {}.".format(drink_id))
            return drink_id

    
    def delete_drink(self, id):
        drink_list = []
        for d in self.list_drinks():
            if d.get('id') != id:
                drink_list.append(d)
            else :
                continue
        self.drinks = drink_list
    
    def list_drinks(self):
        return self.drinks

