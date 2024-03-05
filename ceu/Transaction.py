from datetime import datetime

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.datetime = datetime.now()

    def __str__(self):
        return f"ceuCoin.Transaction{{sender='{self.sender}', recipient='{self.recipient}', amount={self.amount}, datetime={self.datetime}}}"

    def get_sender(self):
        return self.sender

    def get_recipient(self):
        return self.recipient

    def get_amount(self):
        return self.amount

    def get_datetime(self):
        return self.datetime
