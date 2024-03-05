import tkinter as tk
from tkinter import messagebox
from blockchain.Blockchain import *
from user.Wallet import *
class App:
    def __init__(self, master):
        self.master = master
        self.master.title("CEUcoin App")

        # Crear la instancia de la blockchain y las billeteras
        self.blockchain = Blockchain()
        self.wallet1 = Wallet(100, "12")
        self.wallet2 = Wallet(0, "11")

        # Configurar la interfaz gráfica
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta para mostrar el estado de la cadena de bloques
        self.label_blockchain = tk.Label(self.master, text="CEUcoin Blockchain")
        self.label_blockchain.pack(pady=10)

        # Botón para realizar una transacción
        self.button_transaction = tk.Button(self.master, text="Realizar Transacción", command=self.perform_transaction)
        self.button_transaction.pack(pady=10)

        # Botón para mostrar el estado de la cadena de bloques
        self.button_show_blockchain = tk.Button(self.master, text="Mostrar Blockchain", command=self.show_blockchain)
        self.button_show_blockchain.pack(pady=10)

    def perform_transaction(self):
        try:
            # Realizar una transacción desde wallet1 a wallet2
            amount = 10
            transaction = self.wallet1.send(amount, self.wallet2)
            self.blockchain.add_block(transaction)

            # Mostrar mensaje de éxito
            messagebox.showinfo("Éxito", f"Transacción exitosa: {self.wallet1.get_card_id()} envió {amount} a {self.wallet2.get_card_id()}")
        except Exception as e:
            # Capturar excepciones y mostrar mensaje de error
            messagebox.showerror("Error", str(e))

    def show_blockchain(self):
        # Mostrar el estado actual de la cadena de bloques en la etiqueta
        blockchain_str = str(self.blockchain)
        self.label_blockchain.config(text=blockchain_str)

# Ejemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
