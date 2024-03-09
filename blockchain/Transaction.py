from datetime import datetime

class Transaction:
    def __init__(self, sender, recipient, amount, datetime=datetime.now):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.datetime = datetime

    # def __str__(self):
    #     return (f"\n\tsender= {self.sender}" 
    #             f"\n\trecipient= {self.recipient}"
    #             f"\n\tamount= {self.amount}" 
    #             f"\n\tdatetime= {self.datetime}")
        
    def __str__(self):
        return (f"{self.sender} --> {self.recipient}, amount = {self.amount} CEUs, datetime = {self.datetime}")

    def get_sender(self):
        return self.sender

    def get_recipient(self):
        return self.recipient

    def get_amount(self):
        return self.amount

    def get_datetime(self):
        return self.datetime
