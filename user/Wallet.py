from blockchain import Transaction

class Wallet:
    def __init__(self, balance, card_id):
        self.card_id = card_id
        self.balance = balance
        self.public_key = None
        self.private_key = None

    def send(self, amount, recipient):
        transaction = None
        if self.balance > amount:
            self.balance -= amount
            recipient.receive(amount)
            # Agregar una transacción al blockchain cada vez que se deposita.
            # Comprobar si es mejor hacerlo una vez que la transacción se añade al blockchain,
            # entonces debitar y acreditar el dinero en las cuentas. De lo contrario, devolver
            # una excepción "no se realizó la transacción".
            transaction = Transaction(self.card_id, recipient.get_card_id(), amount)
        return transaction

    def receive(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance

    def get_card_id(self):
        return self.card_id


class Transaction:
    def __init__(self, sender_card_id, recipient_card_id, amount):
        self.sender_card_id = sender_card_id
        self.recipient_card_id = recipient_card_id
        self.amount = amount
