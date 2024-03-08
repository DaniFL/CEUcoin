import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

def login():
    print("Test")
    # print(str(username_txt) + str(password_txt))

root = customtkinter.CTk()
root.geometry("500x400")

frame = customtkinter.CTkFrame(master = root)
frame.pack(pady=30, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="CEU COIN")
label.pack(pady=12, padx=10)

username_txt = customtkinter.CTkEntry(master=frame, placeholder_text="username")
username_txt.pack(pady=12, padx=10)

password_txt = customtkinter.CTkEntry(master=frame, placeholder_text="password", show="*")
password_txt.pack(pady=12, padx=10)

login_btn = customtkinter.CTkButton(master=frame, text="Log in", command=login)
login_btn.pack(pady=12, padx=10)

signup_btn = customtkinter.CTkButton(master=frame, text="Sign up", command=login)
signup_btn.pack(pady=12, padx=10)

root.mainloop()

