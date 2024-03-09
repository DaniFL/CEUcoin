import customtkinter as ctk

class Prueba2:
    def __init__(self, root):
        self.root = root

        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=30, padx=50, fill="both", expand=True)

        hello_lbl = ctk.CTkLabel(master=self.frame, text="HELLO", font=("Roboto", 24))
        hello_lbl.pack(pady=12, padx=10)

        back_btn = ctk.CTkButton(master=self.frame, text="Back", command=self.go_back)

    def go_back(self):
        self.frame.destroy()


        