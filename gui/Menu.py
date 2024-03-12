from PIL import Image, ImageTk
import customtkinter as ctk
from databaseManager.BlockchainManager import BlockchainManager
from user.User import *
from user.Wallet import *
from smartcard.System import readers
from smartcard.util import toHexString
from smartcard.util import HexListToBinString

class Menu:
    def __init__(self, blockchainmanager, user):
        self.blockchainmanager = blockchainmanager

        self.connection = self.connect_to_card()
        
        self.root = ctk.CTk()
        self.root.geometry("500x550")
        self.root.title("CEU Wallet")
        image = Image.open("images/CEUlogo.png")
        photo = ImageTk.PhotoImage(image)
        self.root.iconphoto(True, photo)

        self.mainframe = ctk.CTkFrame(master=self.root, height=450)
        self.mainframe.grid(row=0, pady=15, padx=10, sticky="nsew")

        self.frameList = [BalanceFrame(self.root, self.blockchainmanager, user), BlockchainFrame(self.root, self.blockchainmanager, user), SettingsFrame(self.root, user)]
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

    def connect_to_card(self):
        # Buscar lectores disponibles
        reader_list = readers()
        
        if not reader_list:
            print("No se encontraron lectores de tarjetas inteligentes.")
            return None

        # Seleccionar el primer lector
        reader = reader_list[0]

        print("Conectándose al lector:", reader)

        try:
            # Conectar al lector
            connection = reader.createConnection()
            connection.connect(protocol=1)

            print("Conectado a la tarjeta:")
            print("ATR:", toHexString(connection.getATR()))


            return connection

        except Exception as e:
            print("Error al conectar a la tarjeta:", str(e))
            return None

    def send_apdu(self, connection, apdu):
        data, sw1, sw2 = connection.transmit(apdu)
        response = toHexString(data)
        return response, sw1, sw2
        
    def get_uid(self, connection):
        # Enviar el primer APDU (select) APDU: 00 A4 04 00 08   data: A0 00 00 00 03 00 00 00
       apdu1 = [0x00, 0xA4, 0x04, 0x00, 0x08, 0xA0, 0x00, 0x00, 0x00, 0x03, 0x00, 0x00, 0x00]
       response, sw1, sw2 = self.send_apdu(connection, apdu1)
    
       # Enviar el segundo APDU APDU: 80 50 00 00 08   data: 92 F0 7E B4 1B 5B 18 1C 20
       apdu2 = [0x80, 0x50, 0x00, 0x00, 0x08, 0x92, 0xF0, 0x7E, 0xB4, 0x1B, 0x5B, 0x18, 0x1C, 0x20]
       response, sw1, sw2 = self.send_apdu(connection, apdu2)
    
       if sw1 == 0x61: 
           # Enviar comando GET RESPONSE
           apdu_get_response = [0x00, 0xC0, 0x00, 0x00, sw2]
           response, sw1, sw2 = self.send_apdu(connection, apdu_get_response)
           # De la respuesta quiero los bytes de 5 a 10
           return response[11:29]
       else:
           return None

    def showBalanceFrame(self):
        self.frameList[1].grid_forget()
        self.frameList[2].grid_forget()
        self.frameList[0].grid(row=0, pady=5, padx=10, sticky="nsew")
        self.frameList[0].update_data()

    def showBlockchainFrame(self):
        self.frameList[0].grid_forget()
        self.frameList[2].grid_forget()
        self.frameList[1].grid(row=0, pady=5, padx=10, sticky="nsew")
        self.frameList[1].update_data()

    def showSettingsFrame(self):
        self.frameList[0].grid_forget()
        self.frameList[1].grid_forget()
        self.frameList[2].grid(row=0, pady=5, padx=10, sticky="nsew")

    def run(self):
        self.root.mainloop()


class BalanceFrame(ctk.CTkFrame):
    def __init__(self, parent, blockchainmanager, user, connection):
        super().__init__(parent)
        
        self.blockchainmanager = blockchainmanager
        self.user = user
        self.connection = connection

        # Actualizar saldo
        self.pending_transactions()

        # Cargar y mostrar la imagen de la tarjeta
        image_path = "images/CEUcard.png"
        pil_image = Image.open(image_path)
        tk_image = ImageTk.PhotoImage(pil_image)

        # Mostrar la imagen en un CTkLabel
        image_label = ctk.CTkLabel(self, image=tk_image, text = "")
        image_label.image = tk_image  # Guardar referencia a la imagen
        image_label.pack(pady=10)

        # Crear y mostrar etiqueta con el saldo actual
        self.balance_label = ctk.CTkLabel(self, text=f"Current Balance: {self.get_card_balance()} CEUs", font=("size", 16))
        self.balance_label.pack(pady=10)

        # Crear y mostrar etiqueta con la dirección de la wallet
        address_label = ctk.CTkLabel(self, text=f"Card ID: {self.user.get_wallet().get_card_id()}")
        address_label.pack(pady=10)

        # Crear y mostrar botón para retirar/enviar/ingresar dinero
        withdraw_button = ctk.CTkButton(self, text="Withdraw", command=self.open_withdraw_dialog)
        withdraw_button.pack(pady=10, padx=10, side=ctk.LEFT)

        send_money_button = ctk.CTkButton(self, text="Send Money", command=self.open_send_money_dialog)
        send_money_button.pack(pady=10, padx=10, side=ctk.LEFT)

        deposit_button = ctk.CTkButton(self, text="Deposit", command=self.open_deposit_dialog)
        deposit_button.pack(pady=10, padx=10, side=ctk.LEFT)

    def send_apdu(self, connection, apdu):
        data, sw1, sw2 = connection.transmit(apdu)
        response = toHexString(data)
        return response, sw1, sw2

    def open_withdraw_dialog(self):
        dialog = WithdrawDialog(self, self.handle_withdraw_money)
        dialog.show()

    def handle_withdraw_money(self, amount, pin):
        # Logica de withdraw
        # print("Amount:", amount)
        # print("PIN:", pin)
        if self.verify_pin(self.connection, pin):
            if self.get_card_balance() >= amount:
                apdu_debit_money = [0x80, 0x40, 0x00, 0x00, 0x01, amount]
                response, sw1, sw2 = self.send_apdu(self.connection, apdu_debit_money)
                if sw1 == 0x90 and sw2 == 0x00 :
                    transaction = Transaction(self.get_wallet().get_card_id(), "System", amount)
                    blockchain = self.blockchainmanager.get_blockchain()
                    blockchain.add_block(transaction)
                    self.blockchainmanager.add_block(blockchain.get_latest_block())
                    print("Withdraw succesfull.")
                else:
                    print("Cannot withdaw money. Call supervisor!")
            else:
                print("Not enough money")

    def open_send_money_dialog(self):
        dialog = SendMoneyDialog(self, self.handle_send_money)
        dialog.show()

    def handle_send_money(self, recipient, amount, pin):
        # Aquí debes implementar la lógica para enviar el dinero
        # print("Recipient:", recipient)
        # print("Amount:", amount)
        # print("PIN:", pin)
        if self.verify_pin(self.connection, pin):
            if self.get_card_balance() >= amount:
                apdu_debit_money = [0x80, 0x40, 0x00, 0x00, 0x01, amount]
                response, sw1, sw2 = self.send_apdu(self.connection, apdu_debit_money)
                if sw1 == 0x90 and sw2 == 0x00 :
                    transaction = Transaction(self.get_wallet().get_card_id(), recipient, amount, state="PENDING")
                    blockchain = self.blockchainmanager.get_blockchain()
                    blockchain.add_block(transaction)
                    self.blockchainmanager.add_block(blockchain.get_latest_block())
                    print("Money send.")
                else:
                    print("Cannot send money. Call supervisor!")
            else:
                print("Not enough money")

    def open_deposit_dialog(self):
        dialog = DepositDialog(self, self.handle_deposit_money)
        dialog.show()
    
    def handle_deposit_money(self, amount, pin):
        # Logica de deposit
        # print("Amount:", amount)
        # print("PIN:", pin)
        if self.verify_pin(self.connection, pin):
            
            apdu_credit_money = [0x80, 0x30, 0x00, 0x00, 0x01, amount]
            response, sw1, sw2 = self.send_apdu(self.connection, apdu_credit_money)
            if sw1 == 0x90 and sw2 == 0x00 :
                transaction = Transaction("System", self.get_wallet().get_card_id(), amount)
                blockchain = self.blockchainmanager.get_blockchain()
                blockchain.add_block(transaction)
                self.blockchainmanager.add_block(blockchain.get_latest_block())
                print("Withdraw succesfull.")
            else:
                print("Cannot withdaw money. Call supervisor!")
            
    def get_card_balance(self):
        # Comando APDU para verificar el saldo
        apdu_check_balance = [0x80, 0x50, 0x00, 0x00, 0x02]
        response, sw1, sw2 = self.send_apdu(self.connection, apdu_check_balance)
        if sw1 == 0x90 and sw2 == 0x00:
            # Decodificar la respuesta para obtener el saldo
            balance = int(response.replace(" ", ""), 16)
            return balance
        else:
            return None
       
    def verify_pin(self, connection, pin):
        # Comando APDU para verificar el PIN
        pin_bytes = bytes.fromhex(pin.replace(" ", ""))
        apdu_verify_pin = [0x80, 0x20, 0x00, 0x05, len(pin_bytes)] + list(pin_bytes)
        response, sw1, sw2 = self.send_apdu(connection, apdu_verify_pin)
        if sw1 == 0x90 and sw2 == 0x00:
            return True
        else:
            return sw1, sw2

    def pending_transactions(self):
        transactions = self.blockchainmanager.get_pending_transactions_of_user(self.user)
        for transaction in transactions:
            apdu_credit_money = [0x80, 0x30, 0x00, 0x00, 0x01, transaction.get_amount()]
            response, sw1, sw2 = self.send_apdu(self.connection, apdu_credit_money)
            if sw1 == 0x90 and sw2 == 0x00 :
                self.blockchainmanager.update_transactions_of_user(self.user)
                print("Pending transactions receive!")
            else:
                print("Cannot receive transactions. Call supervisor!")

    def update_data(self):
        self.balance_label.configure(text=f"Current Balance: {self.get_card_balance()} CEUs")
        
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
    def __init__(self, parent, blockchainmanager, user):
        super().__init__(parent)
        ctk.CTkLabel(master=self, text="CEUcoin BLOCKCHAIN").pack(fill="both")

        self.blockchainmanager = blockchainmanager
        self.user = user

        blockchain = self.blockchainmanager.get_blockchain()
        chain = blockchain.get_chain()

        self.text_box_b = ctk.CTkTextbox(self, font=("Arial", 12), wrap="none")
        self.text_box_b.pack(fill="both", expand=True)

        for block in chain:
            self.text_box_b.insert("1.0", str(block) + "\n\n")

        self.text_box_b.configure(state="disable")

        ctk.CTkLabel(master=self, text="My Transactions").pack(fill="both")

        transactions = blockchainmanager.get_transactions_of_user(self.user)
        print(transactions)

        self.text_box_t = ctk.CTkTextbox(self, font=("Arial", 12), wrap="none")
        self.text_box_t.pack(fill="both", expand=True)

        for transaction in transactions:
            self.text_box_t.insert("1.0", str(transaction) + "\n\n")

        self.text_box_t.configure(state="disable")
        
    def update_data(self):
        # Actualizar la blockchain
        blockchain = self.blockchainmanager.get_blockchain()
        chain = blockchain.get_chain()
        self.text_box_b.configure(state="normal")
        self.text_box_b.delete("1.0", "end")
        for block in chain:
            self.text_box_b.insert("1.0", str(block) + "\n\n")
        self.text_box_b.configure(state="disable")

        # Actualizar las transacciones del usuario
        transactions = self.blockchainmanager.get_transactions_of_user(self.user)
        self.text_box_t.configure(state="normal")
        self.text_box_t.delete("1.0", "end")
        for transaction in transactions:
            self.text_box_t.insert("1.0", str(transaction) + "\n\n")
        self.text_box_t.configure(state="disable")


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
