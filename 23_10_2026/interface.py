import customtkinter as ctk
import qrcode

ctk.set_appearance_mode("dark")

# Janela -------------------------
janela = ctk.CTk()
janela.geometry("400x500")
janela.title("Sistema Gerador de QR Code")
janela.resizable(False, False)
# ---------------------------------

imagem_qrcode = None

def gerar_qrcode():
    global imagem_qrcode
    texto = entrada.get().strip()

    if texto:
        # Converte o objeto QR Code para a imagem PIL nativa (.get_image())
        qr_pil = qrcode.make(texto).get_image()
        
        # Converte para o formato aceito pelo CustomTkinter
        imagem_qrcode = ctk.CTkImage(light_image=qr_pil, dark_image=qr_pil, size=(230, 230))
        
        # Exibe a imagem no label e remove mensagem de aviso
        resultado.configure(image=imagem_qrcode, text="")
    else:
        resultado.configure(text="Digite um URL ou PIX válido", image=None)

# Elementos da janela -------------------------
titulo = ctk.CTkLabel(
    janela,
    text="Sistema Gerador de QR Code",
    text_color="yellow",
    font=("Arial", 20, "bold")
)
titulo.pack(pady=(20, 10))

entrada = ctk.CTkEntry(
    janela,
    placeholder_text="Digite o URL ou PIX",
    width=300,
    height=40,
    border_color="yellow"
)
entrada.pack(pady=10)

botao = ctk.CTkButton(
    janela,
    width=140,
    height=32,
    fg_color="white",
    text="Gerar QR Code",
    text_color="black",
    hover_color="silver",
    cursor="hand2",
    command=gerar_qrcode
)
botao.pack(pady=10)

resultado = ctk.CTkLabel(janela, text="")
resultado.pack(pady=10)

janela.mainloop()