class User:
    def __init__(self, id, username, passsword, wallet):
        self.id = id
        self.username = username
        self.password = passsword
        self.wallet = wallet

    def __str__(self):
        return f"User: {self.username}, Password: {self.password}"
    
    def get_wallet(self):
        return self.wallet
    
    def get_password(self):
        return self.password
    
    def get_username(self):
        return self.username
    
    def get_id(self):
        return self.id