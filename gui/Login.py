import customtkinter as ctk
from gui.Menu import Menu
from PIL import Image, ImageTk
from databaseManager.BlockchainManager import BlockchainManager
from user.User import User
from user.Wallet import Wallet


class Login:
    def __init__(self, blockchainmanager):
        self.blockchainmanager = blockchainmanager

        # Creation of main window
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.geometry("400x600")
        self.root.title("CEU Wallet")
        image = Image.open("images/CEUlogo.png")
        photo = ImageTk.PhotoImage(image)
        self.root.iconphoto(True, photo)

        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=30, padx=50, fill="both", expand=True)

        # Creation of components
        label = ctk.CTkLabel(master=self.frame, text="CEU COIN", font=("Roboto", 24))
        label.pack(pady=12, padx=10)

        self.load_and_display_image("images/CEUcoin.png")

        self.username_txt = ctk.CTkEntry(master=self.frame, placeholder_text="username")
        self.username_txt.pack(pady=10, padx=10)

        self.password_txt = ctk.CTkEntry(master=self.frame, placeholder_text="password", show="*")
        self.password_txt.pack(pady=10, padx=10)

        login_btn = ctk.CTkButton(master=self.frame, text="Log in", command=self.login)
        login_btn.pack(pady=13, padx=10)

        message_lbl = ctk.CTkLabel(master=self.frame, text="Don't have an account?...", text_color="black").pack()

        signup_btn = ctk.CTkButton(master=self.frame, text="Sign up", command=self.open_sign_up_dialog)
        signup_btn.pack(padx=10)

        self.info_login = ctk.CTkLabel(master=self.frame, text="")
        self.info_login.pack(pady=10)

    def load_and_display_image(self, image_path):
        logo_img = Image.open(image_path)
        logo_img = ImageTk.PhotoImage(logo_img)
        logo_label = ctk.CTkLabel(master=self.frame, image=logo_img, text="")
        logo_label.image = logo_img  # Para evitar que el recolector de basura lo elimine
        logo_label.pack(pady=20)

    def login(self):
        print("Test")
        user = self.blockchainmanager.check_user(self.username_txt.get(), self.password_txt.get())
        print(user)
        if user is not None :
            self.root.destroy()
            menu = Menu(self.blockchainmanager, user)
            menu.run()
        else:
            self.info_login.configure(text="Username or password incorrect")

    def open_sign_up_dialog(self):
        dialog = Signup(self.root, self.handle_sign_up)
        dialog.show()

    def handle_sign_up(self, id, username, password, card_id):
        print("New user:", username)
        print("With password:", password)
        print("Card id:", card_id)
        wallet = Wallet(100, card_id)
        user = User(id, username, password, wallet)
        self.blockchainmanager.add_user(user)

    def run(self):
        self.root.mainloop()
        

class Signup:
    def __init__(self, parent, callback):
        self.parent = parent
        self.callback = callback

        self.dialog = ctk.CTkToplevel(parent)
        self.dialog.title("Register")
        self.dialog.geometry("300x200")

        self.id_entry = ctk.CTkEntry(self.dialog, placeholder_text="DNI")
        self.id_entry.pack(pady=10)

        self.username_entry = ctk.CTkEntry(self.dialog, placeholder_text="username")
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(self.dialog, placeholder_text="password", show="*")
        self.password_entry.pack(pady=10)

        send_button = ctk.CTkButton(self.dialog, text="Send", command=self.register)
        send_button.pack(pady=15)

    def show(self):
        self.dialog.grab_set()
        self.parent.wait_window(self.dialog)

    def register(self):
        id = self.id_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Llamar a la funcion que lee la tarjeta para cojer el serial number y guardarlo en card_id
        # La tarjeta tiene un pin o hay que configurarlo??
        card_id = "123456789"
        # Llamar a la función de devolución de llamada con los datos ingresados
        self.callback(id, username, password, card_id)

        # Cerrar el diálogo
        self.dialog.destroy()

if __name__ == "__main__":
    app = Login()
    app.run()

