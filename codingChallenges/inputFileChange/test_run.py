import json 
from libs.users import Users
from libs.favorite_drinks import FavoriteDrinks
from libs.drinks import Drinks

input_file_path = 'data/tr_member_fav_drink.json'
input_change_path = 'data/tr_member_fav_drink_changes.json'

with open(input_file_path, 'r') as f:
    input_data = json.load(f)

users = Users(input_data.get('user')[:])
drinks = Drinks(input_data.get('drink')[:])
favorite_drinks = FavoriteDrinks(input_data.get('favorite_tr_drinks')[:], users=users, drinks=drinks)


def reload():
    with open(input_file_path, 'r') as f:
        input_data = json.load(f)

    users.reload(input_data.get('user')[:])
    drinks.reload(input_data.get('drink')[:])
    favorite_drinks.reload(input_data.get('favorite_tr_drinks')[:])


def test_add_users(): 
    reload()
    # existing user
    prev_cnt = len(users.list_users())
    users.add_user("Tom Hanks")
    assert prev_cnt == len(users.list_users())
    # new user
    prev_cnt = len(users.list_users())
    users.add_user("Tom Hanks 2.0")
    assert len(users.list_users()) == (prev_cnt+1)

def test_get_user(): 
    reload()    
    assert users.get_user_id("Tom Hanks") is not None
    assert users.get_user_id("Ryan Chynoweth") is None
    assert users.get_user_name("1") is not None
    assert users.get_user_name("10000") is None

def test_delete_user(): 
    reload()    
    # existing user
    prev_cnt = len(users.list_users())
    users.delete_user("1")
    assert (prev_cnt-1) == len(users.list_users())
    # non-existent user
    prev_cnt = len(users.list_users())
    users.delete_user("20000")
    assert len(users.list_users()) == prev_cnt


def test_add_drink():
    reload()    
    # existing drink
    prev_cnt = len(drinks.list_drinks())
    drinks.add_drink(drink_type="Sparkling Ice", flavor="Lemon Lime")
    assert len(drinks.list_drinks()) == prev_cnt
    # new drink
    prev_cnt = len(drinks.list_drinks())
    drinks.add_drink(drink_type="Sparkling Ice", flavor="Watermelon")
    assert len(drinks.list_drinks()) == (prev_cnt+1)


def test_get_drink(): 
    reload()    
    assert drinks.get_drink_by_id("1") is not None
    assert drinks.get_drink_by_id("20000") is None

    assert drinks.get_drinks_by_flavor("Lemon Lime") is not None
    assert drinks.get_drinks_by_flavor("Kiwi") == []

    assert drinks.get_drinks_by_type("Talking Rain Essentials") is not None
    assert drinks.get_drinks_by_type("Ryan's Drink") == []


def test_delete_drink(): 
    reload()    
    # existing 
    prev_cnt = len(drinks.list_drinks())
    drinks.delete_drink("1")
    assert (prev_cnt-1) == len(drinks.list_drinks())
    # non-existent drink
    prev_cnt = len(drinks.list_drinks())
    drinks.delete_drink("111111")
    assert len(drinks.list_drinks()) == prev_cnt


def test_get_fav_drinks(): 
    reload()
    assert len(favorite_drinks.get_fav_drinks("2")) == 2



def test_remove_fav_drink():
    reload()
    # actual fav
    prev_cnt = len(favorite_drinks.get_fav_drinks('2'))
    favorite_drinks.remove_fav_drink(user_id='2', drink_id='8')
    assert len(favorite_drinks.get_fav_drinks('2')) == (prev_cnt-1)
    # non-existent fav drink
    prev_cnt = len(favorite_drinks.get_fav_drinks('2'))
    favorite_drinks.remove_fav_drink(user_id='2', drink_id='88')
    assert len(favorite_drinks.get_fav_drinks('2')) == prev_cnt


def test_add_fav_drink():
    # existing drink
    reload()
    prev_cnt = len(favorite_drinks.get_fav_drinks('3'))
    favorite_drinks.add_fav_drink('3', '1')
    assert len(favorite_drinks.get_fav_drinks('3')) == (prev_cnt+1)
    # existing fav drink
    reload()
    prev_cnt = len(favorite_drinks.get_fav_drinks('3'))
    favorite_drinks.add_fav_drink('3', '6')
    assert len(favorite_drinks.get_fav_drinks('3')) == prev_cnt
    # one existing and one non
    reload()
    prev_cnt = len(favorite_drinks.get_fav_drinks('3'))
    favorite_drinks.add_fav_drinks('3', drinks=[{"type": "Sparkling Ice", "flavor": "Watermelon"}, {"type": "Sparkling Ice", "flavor": "Grape Raspberry"}])
    assert len(favorite_drinks.get_fav_drinks('3')) == (prev_cnt+2)
    # no existing
    reload()
    prev_cnt = len(favorite_drinks.get_fav_drinks('3'))
    favorite_drinks.add_fav_drinks('3', drinks=[{"type": "Sparkling Ice", "flavor": "TESTDRINK"}, {"type": "Sparkling Ice", "flavor": "TESTDRINK2"}])
    assert len(favorite_drinks.get_fav_drinks('3')) == prev_cnt
    # non-existent drink
    reload()
    prev_cnt = len(favorite_drinks.get_fav_drinks('3'))
    favorite_drinks.add_fav_drink('3', '7000')
    assert len(favorite_drinks.get_fav_drinks('3')) == prev_cnt


