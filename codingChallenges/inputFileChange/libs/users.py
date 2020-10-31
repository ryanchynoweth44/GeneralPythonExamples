
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
        assert type(name) == str
        return next((u.get('id') for u in self.users if u.get('name')==name), None)

    def get_user_name(self, id):
        assert type(id) == str
        return next((u.get('name') for u in self.users if u.get('id')==id), None)

    def __generate_id(self):
        ids = [int(u.get('id')) for u in self.users]
        return str(max(ids)+1)

    def add_user(self, name):
        names = [u.get('name') for u in self.users]
        if name not in names:
            self.users.append({"id": self.__generate_id(), "name": name})
        else :
            return 'User Already Exists.'

    def delete_user(self, id):
        user_list = []
        for u in self.list_users():
            if u.get('id') != id:
                user_list.append(u)
            else :
                continue
        self.users = user_list

    def list_users(self):
        return self.users
    
