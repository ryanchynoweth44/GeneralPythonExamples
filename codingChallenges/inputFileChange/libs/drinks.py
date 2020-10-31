
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
        """ returns the drink object for a given id """
        assert type(id) == str
        return next((d for d in self.drinks if d.get('id')==id), None)

    def get_drinks_by_type(self, drink_type):
        """ gets all the drinks of a specific type. """
        assert type(drink_type) == str
        return [d for d in self.drinks if d.get('type')==drink_type]

    def get_drinks_by_flavor(self, flavor):
        """ gets all drinks of a specific flavor. """ 
        assert type(flavor) == str
        return [d for d in self.drinks if d.get('flavor')==flavor]

    def get_drinks_by_flavor_and_type(self, flavor, drink_type):
        """ returns the drink object for a given unique pair of flavor and type. """
        assert type(drink_type) == str
        assert type(flavor) == str
        return next((d for d in self.drinks if d.get('flavor')==flavor and d.get('type')==drink_type), None)

    def __generate_id(self):
        """ Incrementally generates a drink id"""
        ids = [int(d.get('id')) for d in self.drinks]
        return str(max(ids)+1)

    def add_drink(self, drink_type, flavor):
        """ Adds a drink if it does not exists. Returns drink id whether existing or created """
        existing = False if self.get_drinks_by_flavor_and_type(flavor, drink_type) is None else True        
        if not existing: # if it does not exist then add it and return the new id
            drink_id = self.__generate_id()
            print("Adding Drink Id: {}".format(drink_id))
            self.drinks.append({"id": drink_id, "type": drink_type, 'flavor': flavor})
            return drink_id
        else : # if it exists then just return the id
            drink_id = self.get_drinks_by_flavor_and_type(flavor, drink_type).get('id')
            print("Drink exists. Id {}.".format(drink_id))
            return drink_id

    
    def delete_drink(self, id):
        """ Deletes a drink if it exists given an id. """
        drink_list = []
        for d in self.list_drinks():
            if d.get('id') != id:
                drink_list.append(d)
            else :
                continue
        self.drinks = drink_list


    def delete_drink_by_type_flavor(self, drink_type, flavor):
        """ Deletes a drink by type and flavor if it exists. Type and flavor are unique combinations """
        d = self.get_drinks_by_flavor_and_type(flavor, drink_type)
        if d is not None:
            did = d.get('id')
            self.delete_drink(did)
        else :
            print("Drink does not exist. ")

    def list_drinks(self):
        """ Returns all drinks in object. """
        return self.drinks

