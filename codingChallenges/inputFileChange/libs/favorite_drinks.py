
class FavoriteDrinks():
    
    def __init__(self, favorite_drinks, users, drinks):
        self.favorite_drinks = favorite_drinks
        self.drinks = drinks
        self.users = users

    def get_fav_drinks(self, user_id):
        assert type(user_id) == str
        return next((fd.get('drink_id') for fd in self.favorite_drinks if fd.get('user_id')==user_id), None)


    # def add_fav_drink(self, user_id, drink_id)