
class Users():

    __instance = None
    
    @staticmethod
    def getInstance():
        """ Static access method. """
        if Users.__instance == None:
            Users()
        return Users.__instance 

    def __init__(self, users):
        assert type(users) == list
        """ Virtually private constructor. """
        if Users.__instance != None:
            raise Exception("Class already exists.")
        else:
            Users.__instance = self
            Users.users = users

    def reload(self, users):
        """ Used to reload data for tests """
        self.users = users
    
    def get_user_id(self, name):
        """ Gets the user id for a given name. Names are unique. """
        assert type(name) == str
        return next((u.get('id') for u in self.users if u.get('name')==name), None)

    def get_user_name(self, id):
        """ Gets the name of a user for a given id. Ids are unique. """
        assert type(id) == str
        return next((u.get('name') for u in self.users if u.get('id')==id), None)

    def __generate_id(self):
        """ Incrementally generates user ids """
        ids = [int(u.get('id')) for u in self.users]
        return str(max(ids)+1)

    def add_user(self, name):
        """ Adds a user if it does not exist. Names must be unique. """
        names = [u.get('name') for u in self.users]
        if name not in names:
            self.users.append({"id": self.__generate_id(), "name": name})
        else :
            return 'User Already Exists.'

    def delete_user(self, id):
        """ Deletes a user if it exists for a given id. """
        user_list = []
        for u in self.list_users():
            if u.get('id') != id:
                user_list.append(u)
            else :
                continue
        self.users = user_list

    def delete_user_by_name(self, name):
        """ Deletes a user if it exists for a given name. """
        uid = self.get_user_id(name) # get the user id
        self.delete_user(uid)

    def list_users(self):
        """ Returns a list of users stored in the object. """
        return self.users
    
