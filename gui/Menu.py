from PIL import Image, ImageTk
import customtkinter as ctk
from databaseManager.BlockchainManager import BlockchainManager
from user.User import *
from user.Wallet import *

class Menu:
    def __init__(self, blockchainmanager, user):
        self.blockchainmanager = blockchainmanager
        
        self.root = ctk.CTk()
        self.root.geometry("500x550")
        self.root.title("CEU Wallet")
        image = Image.open("images/CEUlogo.png")
        photo = ImageTk.PhotoImage(image)
        self.root.iconphoto(True, photo)

        self.mainframe = ctk.CTkFrame(master=self.root, height=450)
        self.mainframe.grid(row=0, pady=15, padx=10, sticky="nsew")

        self.frameList = [BalanceFrame(self.root, self.blockchainmanager, user), BlockchainFrame(self.root, self.blockchainmanager), SettingsFrame(self.root, user)]
        self.frameList[0].grid(row=0, pady=5, padx=10, sticky="nsew")
        self.frameList[1].grid_forget()
        self.frameList[2].grid_forget()

        self.buttonframe = ctk.CTkFrame(master=self.root)
        self.buttonframe.grid(row=1, pady=5, padx=10, sticky="nsew")

        balance_btn = ctk.CTkButton(master=self.buttonframe, text="My Balance", command=self.showBalanceFrame)
        balance_btn.grid(row=0, column=0, padx=10, pady=10)

        blockchain_btn = ctk.CTkButton(master=self.buttonframe, text="Blockchain", command=self.showBlockchainFrame)
        blockchain_btn.grid(row=0, column=1, padx=10, pady=10)

        contacts_btn = ctk.CTkButton(master=self.buttonframe, text="Settings", command=self.showSettingsFrame)
        contacts_btn.grid(row=0, column=2, padx=10, pady=10)

    

    def showBalanceFrame(self):
        self.frameList[1].grid_forget()
        self.frameList[2].grid_forget()
        self.frameList[0].grid(row=0, pady=5, padx=10, sticky="nsew")

    def showBlockchainFrame(self):
        self.frameList[0].grid_forget()
        self.frameList[2].grid_forget()
        self.frameList[1].grid(row=0, pady=5, padx=10, sticky="nsew")

    def showSettingsFrame(self):
        self.frameList[0].grid_forget()
        self.frameList[1].grid_forget()
        self.frameList[2].grid(row=0, pady=5, padx=10, sticky="nsew")

    def run(self):
        self.root.mainloop()


class BalanceFrame(ctk.CTkFrame):
    def __init__(self, parent, blockchainmanager, user):
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
        balance_label = ctk.CTkLabel(self, text=f"Current Balance: {user.get_wallet().get_balance()} CEUs", font=("size", 16))
        balance_label.pack(pady=10)

        # Crear y mostrar etiqueta con la dirección de la wallet
        address_label = ctk.CTkLabel(self, text=f"Card ID: {user.get_wallet().get_card_id()}")
        address_label.pack(pady=10)

        # Crear y mostrar botón para retirar/enviar/ingresar dinero
        withdraw_button = ctk.CTkButton(self, text="Withdraw", command=self.open_withdraw_dialog)
        withdraw_button.pack(pady=10, padx=10, side=ctk.LEFT)

        send_money_button = ctk.CTkButton(self, text="Send Money", command=self.open_send_money_dialog)
        send_money_button.pack(pady=10, padx=10, side=ctk.LEFT)

        deposit_button = ctk.CTkButton(self, text="Deposit", command=self.open_deposit_dialog)
        deposit_button.pack(pady=10, padx=10, side=ctk.LEFT)

    def open_withdraw_dialog(self):
        dialog = WithdrawDialog(self, self.handle_withdraw_money)
        dialog.show()

    def handle_withdraw_money(self, amount, pin):
        # Logica de withdraw
        print("Amount:", amount)
        print("PIN:", pin)

    def open_send_money_dialog(self):
        dialog = SendMoneyDialog(self, self.handle_send_money)
        dialog.show()

    def handle_send_money(self, recipient, amount, pin):
        # Aquí debes implementar la lógica para enviar el dinero
        print("Recipient:", recipient)
        print("Amount:", amount)
        print("PIN:", pin)

    def open_deposit_dialog(self):
        dialog = DepositDialog(self, self.handle_deposit_money)
        dialog.show()
    
    def handle_deposit_money(self, amount, pin):
        # Logica de deposit
        print("Amount:", amount)
        print("PIN:", pin)

class SendMoneyDialog:
    def __init__(self, parent, callback):
        self.parent = parent
        self.callback = callback

        self.dialog = ctk.CTkToplevel(parent)
        self.dialog.title("Send Money")
        self.dialog.geometry("300x200")

        self.recipient_entry = ctk.CTkEntry(self.dialog, placeholder_text="Recipient card ID")
        self.recipient_entry.pack(pady=10)

        self.amount_entry = ctk.CTkEntry(self.dialog, placeholder_text="Amount")
        self.amount_entry.pack(pady=10)

        self.pin_entry = ctk.CTkEntry(self.dialog, placeholder_text="PIN", show="*")
        self.pin_entry.pack(pady=10)

        send_button = ctk.CTkButton(self.dialog, text="Send", command=self.send)
        send_button.pack(pady=15)

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
class WithdrawDialog:
    def __init__(self, parent, callback):
        self.parent = parent
        self.callback = callback

        self.dialog = ctk.CTkToplevel(parent)
        self.dialog.title("Withdraw money")
        self.dialog.geometry("300x200")

        ctk.CTkLabel(self.dialog, text="Withdraw from this account:").pack(pady=12)

        self.amount_entry = ctk.CTkEntry(self.dialog, placeholder_text="Amount")
        self.amount_entry.pack(pady=10)

        self.pin_entry = ctk.CTkEntry(self.dialog, placeholder_text="PIN", show="*")
        self.pin_entry.pack(pady=10)

        withdraw_button = ctk.CTkButton(self.dialog, text="Confirm", command=self.withdraw)
        withdraw_button.pack(pady=15)

    def show(self):
        self.dialog.grab_set()
        self.parent.wait_window(self.dialog)

    def withdraw(self):
        amount = self.amount_entry.get()
        pin = self.pin_entry.get()

        # Llamar a la función de devolución de llamada con los datos ingresados
        self.callback(amount, pin)

        # Cerrar el diálogo
        self.dialog.destroy()
class DepositDialog:
    def __init__(self, parent, callback):
        self.parent = parent
        self.callback = callback

        self.dialog = ctk.CTkToplevel(parent)
        self.dialog.title("Deposit Money")
        self.dialog.geometry("300x200")

        ctk.CTkLabel(self.dialog, text="Deposit into this account:").pack(pady=12)

        self.amount_entry = ctk.CTkEntry(self.dialog, placeholder_text="Amount")
        self.amount_entry.pack(pady=10)

        self.pin_entry = ctk.CTkEntry(self.dialog, placeholder_text="PIN", show="*")
        self.pin_entry.pack(pady=10)

        deposit_button = ctk.CTkButton(self.dialog, text="Confirm", command=self.deposit)
        deposit_button.pack(pady=15)

    def show(self):
        self.dialog.grab_set()
        self.parent.wait_window(self.dialog)

    def deposit(self):
        amount = self.amount_entry.get()
        pin = self.pin_entry.get()

        # Llamar a la función de devolución de llamada con los datos ingresados
        self.callback(amount, pin)

        # Cerrar el diálogo
        self.dialog.destroy()

class BlockchainFrame(ctk.CTkFrame):
    def __init__(self, parent, blockchainmanager):
        super().__init__(parent)
        ctk.CTkLabel(master=self, text="CEUcoin BLOCKCHAIN").pack(fill="both")

        # blockchain = blockchainmanager.get_blockchain()
        # chain = blockchain.get_chain()

        # self.text_box = ctk.CTkTextbox(self, font=("Arial", 12), wrap="none")
        # self.text_box.pack(fill="both", expand=True)

        # for block in chain:
        #     self.text_box.insert("1.0", str(block) + "\n")

        # self.text_box.configure(state="disable")

        try:
            blockchain = blockchainmanager.get_blockchain()
            chain = blockchain.get_chain() if blockchain else []

            self.text_box = ctk.CTkTextbox(self, font=("Arial", 12), wrap="none")
            self.text_box.pack(fill="both", expand=True)

            for block in chain:
                self.text_box.insert("1.0", str(block) + "\n")

            self.text_box.configure(state="disabled")
        except Exception as e:
            print(f"Error al cargar la cadena de bloques: {e}")
            # Manejar adecuadamente el error o mostrar un mensaje en la UI
        


class SettingsFrame(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)

        label_font = ("Helvetica", 15, "bold")

        ctk.CTkLabel(self, text="My account:", font=label_font).pack(pady=10)
        ctk.CTkLabel(self, text="DNI: " + user.get_id()).pack(pady=5)
        ctk.CTkLabel(self, text="Username: " + user.get_username()).pack(pady=5)

        # Espacio en la pantalla
        ctk.CTkLabel(self, text="").pack(pady=20)

        # Opciones para el modo
        modes = ["dark", "light"]

        # Combobox para el modo
        mode_lbl = ctk.CTkLabel(self, text="Appearance Mode:", font=label_font)
        mode_lbl.pack(padx=10, pady=10)
        self.mode = ctk.CTkComboBox(self, values=modes)
        self.mode.pack(padx=10, pady=5)

        # Botón para aplicar cambios
        apply_btn = ctk.CTkButton(self, text="Apply", command=self.apply_settings)
        apply_btn.pack(padx=10, pady=30)

    def apply_settings(self):
        # Obtener el modo y el tema seleccionados
        selected_mode = self.mode.get()
        
        # Cambiar el modo de la aplicacion
        if selected_mode == "dark":
            ctk.set_appearance_mode("dark")
        elif selected_mode == "light":
            ctk.set_appearance_mode("light")


if __name__ == "__main__":
    app = Menu()
    app.run()
