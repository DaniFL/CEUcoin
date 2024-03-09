class User:
    def __init__(self, username, passsword):
        self.username = username
        self.password = passsword
        # Faltaria que poner el wallet tambien

    def __str__(self):
        return f"User: {self.username}, Password: {self.password}"