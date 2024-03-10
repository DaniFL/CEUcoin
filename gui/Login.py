import customtkinter as ctk
from gui.Menu import Menu
from PIL import Image, ImageTk
from databaseManager.BlockchainManager import *


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
        self.username_txt.pack(pady=12, padx=10)

        self.password_txt = ctk.CTkEntry(master=self.frame, placeholder_text="password", show="*")
        self.password_txt.pack(pady=12, padx=10)

        login_btn = ctk.CTkButton(master=self.frame, text="Log in", command=lambda: self.login(self.blockchainmanager))
        login_btn.pack(pady=12, padx=10)

        signup_btn = ctk.CTkButton(master=self.frame, text="Sign up", command=self.change_theme)
        signup_btn.pack(pady=12, padx=10)

        self.info_login = ctk.CTkLabel(master=self.frame, text="")
        self.info_login.pack(pady=10)

    def load_and_display_image(self, image_path):
        logo_img = Image.open(image_path)
        logo_img = ImageTk.PhotoImage(logo_img)
        logo_label = ctk.CTkLabel(master=self.frame, image=logo_img, text="")
        logo_label.image = logo_img  # Para evitar que el recolector de basura lo elimine
        logo_label.pack(pady=20)

    def login(self, blockchainmanager):
        print("Test")
        user = blockchainmanager.check_user(self.username_txt.get(), self.password_txt.get())
        print(user)
        if user is not None :
            self.root.destroy()
            menu = Menu(blockchainmanager, user)
            menu.run()
        else:
            self.info_login.configure(text="Username or password incorrect")
            

    def change_theme(self):
        ctk.set_appearance_mode("light")

    def run(self):
        self.root.mainloop()
        

if __name__ == "__main__":
    app = Login()
    app.run()

