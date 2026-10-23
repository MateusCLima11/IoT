import customtkinter as ctk
import qrcode
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")

# janela -------------------------
janela = ctk.CTk()
janela.geometry("400x500")
janela.title("Sistema Gerador de QR Code")
janela.resizable(False, False)
# ---------------------------------

imagem_qrcode = None


# Elementos da janela -------------------------
titulo = ctk.CTkLabel(janela,
                    text="Sistema Gerador de QR Code",
                    text_color="yellow",
                    font=("Arial", 30))
titulo.pack(pady=10)

# ------------------------------------------------------

entrada = ctk.CTkEntry(janela,
                        placeholder_text="Digite o URL ou PIX",
                        width=300,
                        height=40,
                        border_color="yellow",)
entrada.pack(pady=10)

# ---------------------------------------------------------------

# Botão para gerar o QR Code
botao = ctk.CTkButton(janela,
                    width=100,
                    height=20,
                    fg_color="white",
                    text="Gerar QR Code",
                    text_color="black",
                    hover_color="silver",
                    cursor="hand2",
                    command=lambda: gerar_qrcode(entrada.get()))
botao.pack(pady=10)
# ---------------------------------------------------------------

# Mostrar o resultado do QR Code
resultado = ctk.CTkLabel(janela,
                        text="",)
resultado.pack(pady=10)
# ---------------------------------------------------------------




janela.mainloop()