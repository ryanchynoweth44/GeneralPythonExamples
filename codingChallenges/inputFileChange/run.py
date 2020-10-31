import sys
import json 
from libs.users import Users
from libs.favorite_drinks import FavoriteDrinks
from libs.drinks import Drinks

# get command line arguments
args = sys.argv
assert len(args) == 4 or args == ['run.py'] # ensures file path ags

# set default values
input_file_path = 'data/tr_member_fav_drink.json'
input_change_path = 'data/tr_member_fav_drink_changes.json'
output_path = 'data/tr_member_fav_drink_updated.json'

# overwrite if values provided
if len(args) == 4:
    input_file_path = args[1]
    input_change_path = args[2]
    output_path = args[3]


# load the input data as dicts
with open(input_file_path, 'r') as f:
    input_data = json.load(f)

with open(input_change_path, 'r') as f:
    change_data = json.load(f)

# create the objects
users = Users(input_data.get('user'))
drinks = Drinks(input_data.get('drink'))
# users and drinks are singletons so any changes in those classes will be broadcasted to the favorite drinks class
# this ensures data integrity. 
favorite_drinks = FavoriteDrinks(input_data.get('favorite_tr_drinks'), users=users, drinks=drinks)

##
## Users
##
users.list_users()
# for each provide change for users execute the action
for i in change_data.get('user'): # for each item
    if i.get('action') == 'add' and i.get('name') is not None:
        users.add_user(i.get('name'))
    elif i.get('action') == 'delete' and i.get('name') is not None:
        users.delete_user_by_name(i.get('name'))
    else :
        print("Invalid action or name.")

users.list_users()

##
### Drinks
###
drinks.list_drinks()
# for each provided change for drinks execute the action
for i in change_data.get('drink'):
    if i.get('type') is None or i.get('flavor') is None:
        print("Invalid drink")
        continue
    elif i.get('action') == 'add':
        drinks.add_drink(i.get('type'), i.get('flavor'))
    elif i.get('action') == 'delete':
        drinks.delete_drink_by_type_flavor(i.get('type'), i.get('flavor'))
    else :
        print("Invalid action.")

drinks.list_drinks()

##
## favorite_tr_drinks
##
favorite_drinks.favorite_drinks
# for each provided change for the favorite_tr_drinks execute the change
for d in change_data.get('favorite_tr_drinks'):
    if d.get('action') == 'add':
        favorite_drinks.add_fav_drinks(d.get('fav_drink').get('user_id'), d.get('fav_drink').get('drinks'))

    elif d.get('action') == 'delete':
        for i in d.get('fav_drink').get('drinks'):
            favorite_drinks.delete_fav_drink(d.get('fav_drink').get('user_id'), i.get('drink_id'))

    else :
        print("Invalid action.")

favorite_drinks.favorite_drinks

# format output json file
output_data = {'user': users.users, 'drink': drinks.drinks, 'favorite_tr_drinks': favorite_drinks.favorite_drinks}

# dump the contents
with open(output_path, 'w') as f:
    json.dump(output_data, f)

