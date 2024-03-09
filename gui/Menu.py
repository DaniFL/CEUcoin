import customtkinter as ctk
from databaseManager.BlockchainManager import *

class Menu:
    def __init__(self, blockchainManager):
        self.blockchainManager = blockchainManager
        self.root = ctk.CTk()
        self.root.geometry("500x550")

        self.mainframe = ctk.CTkFrame(master=self.root, height=450)
        self.mainframe.grid(row=0, pady=15, padx=10, sticky="nsew")

        self.frameList = [BalanceFrame(self.root), BlockchainFrame(self.root, self.blockchainManager), ContactsFrame(self.root)]
        self.frameList[1].grid_forget()
        self.frameList[2].grid_forget()

        self.buttonframe = ctk.CTkFrame(master=self.root)
        self.buttonframe.grid(row=1, pady=5, padx=10, sticky="nsew")

        balance_btn = ctk.CTkButton(master=self.buttonframe, text="My Balance", command=self.showBalanceFrame)
        balance_btn.grid(row=0, column=0, padx=10, pady=10)

        blockchain_btn = ctk.CTkButton(master=self.buttonframe, text="Blockchain", command=self.showBlockchainFrame)
        blockchain_btn.grid(row=0, column=1, padx=10, pady=10)

        contacts_btn = ctk.CTkButton(master=self.buttonframe, text="My contacts", command=self.showContactsFrame)
        contacts_btn.grid(row=0, column=2, padx=10, pady=10)

    

    def showBalanceFrame(self):
        self.frameList[1].grid_forget()
        self.frameList[2].grid_forget()
        self.frameList[0].grid(row=0, pady=5, padx=10, sticky="nsew")

    def showBlockchainFrame(self):
        self.frameList[0].grid_forget()
        self.frameList[2].grid_forget()
        self.frameList[1].grid(row=0, pady=5, padx=10, sticky="nsew")

    def showContactsFrame(self):
        self.frameList[0].grid_forget()
        self.frameList[1].grid_forget()
        self.frameList[2].grid(row=0, pady=5, padx=10, sticky="nsew")

    def run(self):
        self.root.mainloop()


class BalanceFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        ctk.CTkLabel(master=self, text="BALANCE FRAME").pack(fill="both", expand=True)
        self.grid(row=0, pady=5, padx=10, sticky="nsew")

    def showBlockchain(self)


class BlockchainFrame(ctk.CTkFrame):
    def __init__(self, parent, blockchainManager):
        super().__init__(parent)
        ctk.CTkLabel(master=self, text="BLOCKCHAIN FRAME").pack(fill="both", expand=True)




class ContactsFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        ctk.CTkLabel(master=self, text="CONTACTS FRAME").pack(fill="both", expand=True)

if __name__ == "__main__":
    app = Menu()
    app.run()