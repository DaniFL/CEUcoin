import customtkinter as ctk
from PIL import Image, ImageTk


class Prueba:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.geometry("400x600")

        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=30, padx=60, fill="both", expand=True)

        label = ctk.CTkLabel(master=self.frame, text="CEU COIN", font=("Roboto", 24))
        label.pack(pady=12, padx=10)

        logo_path = "CEUcoin.png"  # Cambia la ruta de la imagen según tu necesidad
        self.load_and_display_image(logo_path)

        self.username_txt = ctk.CTkEntry(master=self.frame, placeholder_text="username")
        self.username_txt.pack(pady=12, padx=10)

        self.password_txt = ctk.CTkEntry(master=self.frame, placeholder_text="password", show="*")
        self.password_txt.pack(pady=12, padx=10)

        login_btn = ctk.CTkButton(master=self.frame, text="Log in", command=self.login)
        login_btn.pack(pady=12, padx=10)

        signup_btn = ctk.CTkButton(master=self.frame, text="Sign up", command=self.change_theme)
        signup_btn.pack(pady=12, padx=10)

    def load_and_display_image(self, image_path):
        logo_img = Image.open(image_path)
        logo_img = ImageTk.PhotoImage(logo_img)
        logo_label = ctk.CTkLabel(master=self.frame, image=logo_img, text="")
        logo_label.image = logo_img  # Para evitar que el recolector de basura lo elimine
        logo_label.pack(pady=20)

    def login(self):
        print("Test")
        if hasattr(self, "info_login"):
            self.info_login.destroy()
        self.info_login = ctk.CTkLabel(master=self.frame, text="Username or password incorrect")
        self.info_login.pack(pady=10)

    def change_theme(self):
        ctk.set_appearance_mode("light")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Prueba()
    app.run()
