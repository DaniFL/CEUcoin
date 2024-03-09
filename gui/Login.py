import customtkinter as ctk
from PIL import Image, ImageTk
from databaseManager.BlockchainManager import *


class Login:
    def __init__(self):

        # Creation of main window
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.geometry("400x600")

        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=30, padx=50, fill="both", expand=True)

        # Creation of components
        label = ctk.CTkLabel(master=self.frame, text="CEU COIN", font=("Roboto", 24))
        label.pack(pady=12, padx=10)

        logo_path = "images/CEUcoin.png"  # Cambia la ruta de la imagen según tu necesidad
        self.load_and_display_image(logo_path)

        self.username_txt = ctk.CTkEntry(master=self.frame, placeholder_text="username")
        self.username_txt.pack(pady=12, padx=10)

        self.password_txt = ctk.CTkEntry(master=self.frame, placeholder_text="password", show="*")
        self.password_txt.pack(pady=12, padx=10)

        login_btn = ctk.CTkButton(master=self.frame, text="Log in", command=self.login)
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

    def login(self):
        print("Test")
        user = BlockchainManager.check_user(self.username_txt.get, self.password_txt.get)
        if user == None :
            self.info_login.configure(text="Username or password incorrect")
        else:
            print("usuario existe aqui se abriria la otra ventana")

    # def signup(self):
    #     print("test")
    #     self.root.withdraw()
    #     prueba2 = Prueba2(self.root)

    def change_theme(self):
        ctk.set_appearance_mode("light")

    def run(self):
        self.root.mainloop()
        

if __name__ == "__main__":
    app = Login()
    app.run()

