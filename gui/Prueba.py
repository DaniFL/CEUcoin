import customtkinter
from tkinter import PhotoImage
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

def login():
    print("Test")
    print(username_txt.get() + " " + password_txt.get())

def change_theme():
    customtkinter.set_appearance_mode("light")

root = customtkinter.CTk()
root.geometry("400x600")

frame = customtkinter.CTkFrame(master = root)
frame.pack(pady=30, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="CEU COIN", font=("Roboto", 24))
label.pack(pady=12, padx=10)

# logo_path = "CEUcoin.png"  # Cambia la ruta de la imagen según tu necesidad
# img_logo = Image.open(logo_path)
# img_logo = ImageTk.PhotoImage(img_logo)
# logo_label = customtkinter.CTkLabel(master=frame, image=img_logo, text="")
# logo_label.image = img_logo
logo = PhotoImage(file="CEUcoin.png")
logo_label = customtkinter.CTkLabel(master=frame, image=logo, text="")
logo_label.pack(pady=20)

username_txt = customtkinter.CTkEntry(master=frame, placeholder_text="username")
username_txt.pack(pady=12, padx=10)

password_txt = customtkinter.CTkEntry(master=frame, placeholder_text="password", show="*")
password_txt.pack(pady=12, padx=10)

login_btn = customtkinter.CTkButton(master=frame, text="Log in", command=login)
login_btn.pack(pady=12, padx=10)

signup_btn = customtkinter.CTkButton(master=frame, text="Sign up", command=change_theme)
signup_btn.pack(pady=12, padx=10)

root.mainloop()

