import json 
from libs.users import Users
from libs.favorite_drinks import FavoriteDrinks
from libs.drinks import Drinks

input_file_path = 'data/tr_member_fav_drink.json'
input_change_path = 'data/tr_member_fav_drink_changes.json'
output_path = 'data/tr_member_fav_drink_updated.json'

with open(input_file_path, 'r') as f:
    input_data = json.load(f)


with open(input_change_path, 'r') as f:
    change_data = json.load(f)


users = Users(input_data.get('user'))
drinks = Drinks(input_data.get('drink'))
favorite_drinks = FavoriteDrinks(input_data.get('favorite_tr_drinks'), users=users, drinks=drinks)

##
## Users
##
for i in change_data.get('user'): # for each item
    if i.get('action') == 'add' and i.get('name') is not None:
        users.add_user(i.get('name'))
    elif i.get('action') == 'delete' and i.get('name') is not None:
        users.delete_user(i.get('name'))
    else :
        print("Invalid action or name.")


##
### Drinks
###
for i in change_data.get('drink'):
    if i.get('type') is None or i.get('flavor') is None:
        print("Invalid drink")
        continue
    elif i.get('action') == 'add':
        drinks.add_drink(i.get('type'), i.get('flavor'))
    elif i.get('action') == 'delete':
        drinks.delete_drink(i.get('id'))
    else :
        print("Invalid action.")

##
## favorite_tr_drinks
##
for d in change_data.get('favorite_tr_drinks'):
    if d.get('action') == 'add':
        favorite_drinks.add_fav_drinks(d.get('fav_drink').get('user_id'), d.get('fav_drink').get('drinks'))

    elif d.get('action') == 'delete':
        for i in d.get('fav_drink').get('drinks'):
            favorite_drinks.remove_fav_drink(d.get('fav_drink').get('user_id'), i.get('drink_id'))

    else :
        print("Invalid action.")

### Isse with adding a list of drinks that do not exist.


with open(output_path, 'w') as f:
    change_data = json.dump({'user': users, 'drink': drinks, 'favorite_tr_drinks': favorite_drinks}, f)
