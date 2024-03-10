class User:
    def __init__(self, username, passsword, wallet):
        self.username = username
        self.password = passsword
        self.wallet = wallet

    def __str__(self):
        return f"User: {self.username}, Password: {self.password}"
    
    def get_wallet(self):
        return self.wallet