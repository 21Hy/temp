class Cliente:
    def __init__(self, username, password, nif):
        self.username = username
        self.password = password
        self.nif = nif

    def get_username(self):
        return self.username
    def get_password(self):
        return self.password
    def get_nif(self):
        return self.nif
    
    def set_username(self, username):
        self.username = username
    def set_password(self, password):
        self.password = password    
    def set_nif(self, nif):
        self.nif = nif
