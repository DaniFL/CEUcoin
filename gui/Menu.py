from PIL import Image, ImageTk
import customtkinter as ctk
from databaseManager.BlockchainManager import BlockchainManager

class Menu:
    def __init__(self, blockchainmanager):
        self.blockchainmanager = blockchainmanager
        self.root = ctk.CTk()
        self.root.geometry("500x550")

        self.mainframe = ctk.CTkFrame(master=self.root, height=450)
        self.mainframe.grid(row=0, pady=15, padx=10, sticky="nsew")

        self.frameList = [BalanceFrame(self.root), BlockchainFrame(self.root, self.blockchainmanager), ContactsFrame(self.root)]
        self.frameList[0].grid(row=0, pady=5, padx=10, sticky="nsew")
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

        # Cargar y mostrar la imagen de la tarjeta
        image_path = "images/CEUcard.png"
        pil_image = Image.open(image_path)
        tk_image = ImageTk.PhotoImage(pil_image)

        # Mostrar la imagen en un CTkLabel
        image_label = ctk.CTkLabel(self, image=tk_image, text = "")
        image_label.image = tk_image  # Guardar referencia a la imagen
        image_label.pack(pady=10)

        # Crear y mostrar etiqueta con el saldo actual
        balance_label = ctk.CTkLabel(self, text="Current Balance = 50 CEUs")
        balance_label.pack(pady=10)

        # Crear y mostrar etiqueta con la dirección de la wallet
        address_label = ctk.CTkLabel(self, text="1234567890123456789A")
        address_label.pack(pady=10)

        # Crear y mostrar botón para enviar dinero
        send_money_button = ctk.CTkButton(self, text="Send Money", command=self.open_send_money_dialog)
        send_money_button.pack(pady=10)

    def open_send_money_dialog(self):
        dialog = SendMoneyDialog(self, self.handle_send_money)
        dialog.show()

    def handle_send_money(self, recipient, amount, pin):
        # Aquí debes implementar la lógica para enviar el dinero
        print("Recipient:", recipient)
        print("Amount:", amount)
        print("PIN:", pin)

class SendMoneyDialog:
    def __init__(self, parent, callback):
        self.parent = parent
        self.callback = callback

        self.dialog = ctk.CTkToplevel(parent)
        self.dialog.title("Send Money")

        self.recipient_entry = ctk.CTkEntry(self.dialog, placeholder_text="Recipient card ID")
        self.recipient_entry.pack(padx=10, pady=5)

        self.amount_entry = ctk.CTkEntry(self.dialog, placeholder_text="Amount")
        self.amount_entry.pack(padx=10, pady=5)

        self.pin_entry = ctk.CTkEntry(self.dialog, placeholder_text="PIN", show="*")
        self.pin_entry.pack(padx=10, pady=5)

        send_button = ctk.CTkButton(self.dialog, text="Send", command=self.send)
        send_button.pack(pady=10)

    def show(self):
        self.dialog.grab_set()
        self.parent.wait_window(self.dialog)

    def send(self):
        recipient = self.recipient_entry.get()
        amount = self.amount_entry.get()
        pin = self.pin_entry.get()

        # Llamar a la función de devolución de llamada con los datos ingresados
        self.callback(recipient, amount, pin)

        # Cerrar el diálogo
        self.dialog.destroy()



class BlockchainFrame(ctk.CTkFrame):
    def __init__(self, parent, blockchainmanager):
        super().__init__(parent)
        ctk.CTkLabel(master=self, text="BLOCKCHAIN FRAME").pack(fill="both")

        blockchain = blockchainmanager.get_blockchain()
        chain = blockchain.get_chain()

        self.text_box = ctk.CTkTextbox(self, font=("Arial", 12), wrap="none")
        self.text_box.pack(fill="both", expand=True)

        for block in chain:
            self.text_box.insert("1.0", str(block) + "\n")

        self.text_box.configure(state="disable")

        



class ContactsFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        ctk.CTkLabel(master=self, text="CONTACTS FRAME").pack(fill="both", expand=True)

if __name__ == "__main__":
    app = Menu()
    app.run()
