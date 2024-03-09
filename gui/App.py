import customtkinter as ctk
from gui.Menu import Menu
from PIL import Image, ImageTk
from databaseManager.BlockchainManager import BlockchainManager

class App:
    def __init__(self, blockchainmanager):
        self.blockchainmanager = blockchainmanager
        self.root = ctk.CTk()
        self.root.title("CEUcoin Wallet")
        self.root.geometry("600x600")  # Establecer un tamaño mediano
        self.root.resizable(False, False)

        # Cargar la imagen del logo en la primera ventana
        logo_path = "images/ceulogo.png" 
        pil_image = Image.open(logo_path)
        tk_image = ImageTk.PhotoImage(pil_image)  # Crear un PhotoImage de tkinter compatible

        # Mostrar la imagen en un CTkLabel
        logo_label = ctk.CTkLabel(self.root, image=tk_image, text="")
        logo_label.image = tk_image  # Guardar referencia a la imagen
        logo_label.pack(pady=10)

        # Crear botón para abrir la ventana de la billetera
        self.wallet_button = ctk.CTkButton(self.root, text="Go to my Wallet", command=lambda: self.open_wallet(self.blockchainmanager))
        self.wallet_button.pack(pady=10)

    def open_wallet(self, blockchainmanager):
        self.root.destroy()
        menu_app = Menu(blockchainmanager)
        menu_app.run()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    blockchainmanager = BlockchainManager()  # Asegúrate de crear una instancia aquí
    app = App(blockchainmanager)
    app.run()
