import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CEUcoin Wallet")
        self.root.geometry("800x800")  # Establecer un tamaño mediano

        # Crear botón para abrir la ventana de la billetera
        self.wallet_button = ttk.Button(self.root, text="Mi Wallet", command=lambda: self.open_wallet("CEUcoin.jpeg"))
        self.wallet_button.pack(pady=20)

    def open_wallet(self, image_path):
        # Crear una nueva ventana para la billetera
        wallet_window = tk.Toplevel(self.root)
        wallet_window.title("CEUcoin Wallet")
        wallet_window.geometry("800x800")  # Establecer el mismo tamaño mediano

        # Agregar una imagen usando Pillow para cargar imágenes JPEG
        img = Image.open(image_path)
        img = ImageTk.PhotoImage(img)
        img_label = tk.Label(wallet_window, image=img)
        img_label.image = img
        img_label.pack(pady=10)

        # Botones de enviar y recibir
        send_button = ttk.Button(wallet_window, text="Enviar", command=self.send_money)
        send_button.pack(side=tk.LEFT, padx=10)

        receive_button = ttk.Button(wallet_window, text="Recibir", command=self.receive_money)
        receive_button.pack(side=tk.RIGHT, padx=10)

    def send_money(self):
        # Lógica para enviar dinero

        # Crear una nueva ventana para que el usuario introduzca la dirección de la cartera y la cantidad
        send_money_window = tk.Toplevel(self.root)
        send_money_window.title("Enviar Dinero")

        # Cuadro de entrada para la dirección de la cartera
        label_address = tk.Label(send_money_window, text="Introduce la dirección de la cartera:")
        label_address.pack(pady=5)
        entry_address = tk.Entry(send_money_window)
        entry_address.pack(pady=5)

        # Cuadro de entrada para la cantidad
        label_amount = tk.Label(send_money_window, text="Introduce la cantidad a enviar:")
        label_amount.pack(pady=5)
        entry_amount = tk.Entry(send_money_window)
        entry_amount.pack(pady=5)

        # Botón para confirmar el envío
        confirm_button = ttk.Button(send_money_window, text="Confirmar", command=lambda: self.confirm_send(entry_address.get(), entry_amount.get()))
        confirm_button.pack(pady=10)

    def confirm_send(self, address, amount):
        # Lógica para confirmar el envío
        print(f"Enviando {amount} CEU a la dirección: {address}")

    def receive_money(self):
        # Lógica para recibir dinero
        print("Dinero recibido")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
