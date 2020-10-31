
class FavoriteDrinks():
    
    def __init__(self, favorite_drinks, users, drinks):
        self.favorite_drinks = favorite_drinks
        self.drinks = drinks
        self.users = users

    def reload(self, favorite_drinks):
        """ Used to reload data for tests """
        self.favorite_drinks = favorite_drinks

    def get_fav_drinks(self, user_id):
        assert type(user_id) == str
        return next((fd.get('drink_id') for fd in self.favorite_drinks if fd.get('user_id')==user_id), None)

    def __generate_id(self):
        ids = [int(fd.get('id')) for fd in self.favorite_drinks]
        return str(max(ids)+1)

    def add_fav_drinks(self, user_id, drinks):
        """ 
        Adds a list of drinks to the user's favorite_tr_drinks. 
        At least one drink needs to exist in the drinks object.   
        :param user_id: user id. String.
        :param drinks: list of dicts containing drink dictionaries i.e. [{"type": "Sparkling Ice", "flavor": "Watermelon"}]. 
        """ 
        assert type(user_id) == str
        assert type(drinks) == list

        fav_drinks = self.get_fav_drinks(user_id)
        user_check = self.users.get_user_name(user_id)
        drinks_check = [self.drinks.get_drinks_by_flavor_and_type(d.get('flavor'), d.get('type')) for d in drinks]

        if all(x is None for x in drinks_check):
            print("All drinks provided do not exist. We will not add favorite drinks since one of the drinks must already exist.")
        elif user_check is None: # user does not exist
            print("User Id {} does not exist.".format(user_id))
        else : # add drinks
            # user has existing fav drinks
            if fav_drinks is not None:
                for d in drinks:
                    # add the drink if it does not exist 
                    drink_id = self.drinks.add_drink(d.get('type'), d.get('flavor'))
                    fav_drinks.append(drink_id)
            # user has no existing fav drinks
            else :
                ids = []
                for d in drinks:
                    # add the drink if it does not exist 
                    ids.append(self.drinks.add_drink(d.get('type'), d.get('flavor')))

                fd_id = self.__generate_id()
                self.favorite_drinks.append({"id": fd_id, "user_id": user_id, "drink_id": ids})

    def add_fav_drink(self, user_id, drink_id):
        """ Adds an existing drink id to a user's fav_drinks. """
        assert type(user_id) == str
        assert type(drink_id) == str    

        existing_drink = False if self.drinks.get_drink_by_id(drink_id) is None else True
        existing_user = False if self.users.get_user_name(user_id) is None else True
        if not existing_drink:
            print("Drink does not exist.")
        elif not existing_user:
            print("User does not exist.")
        else :
            fav_drinks = self.get_fav_drinks(user_id)
            if fav_drinks is not None:
                if drink_id not in fav_drinks:
                    fav_drinks.append(drink_id)
            else : # user exists but has no fav drinks
                fd_id = self.__generate_id()
                self.favorite_drinks.append({"id": fd_id, "user_id": user_id, "drink_id": [drink_id]})


    def remove_fav_drink(self, user_id, drink_id):
        """ Removes a single drink id from a given user's favorite_tr_drinks """
        assert type(user_id) == str
        assert type(drink_id) == str
        drinks = self.get_fav_drinks(user_id)
        user_check = self.users.get_user_name(user_id)
        if drink_id in drinks:
            drinks.remove(drink_id)
        elif user_check is None:
            print("User Id {} does not exist.".format(user_id))
        else :
            print("User Id {} does not have a favorite drink id {}.".format(user_id, drink_id))


