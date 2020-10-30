import json 
from libs.users import Users
from libs.favorite_drinks import FavoriteDrinks
from libs.drinks import Drinks

input_file_path = 'data/tr_member_fav_drink.json'
input_change_path = 'data/tr_member_fav_drink_changes.json'

with open(input_file_path, 'r') as f:
    input_data = json.load(f)


users = Users(input_data.get('user'))
drinks = Drinks(input_data.get('drink'))

favorite_drinks = FavoriteDrinks(input_data.get('favorite_tr_drinks'), users=users, drinks=drinks)
favorite_drinks.users.list_users()
favorite_drinks.drinks.list_drinks()


users.add_user('Ryan Chynoweth')
favorite_drinks.users.list_users()
users.users



users.add_user('Ryan Chynoweth 2.0')
favorite_drinks.users.list_users()
users.users



drinks.add_drink('Ryan drink', flavor='Awesome')
drinks.drinks
favorite_drinks.drinks.list_drinks()

