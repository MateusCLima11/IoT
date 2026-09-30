import customtkinter as ctk
ctk.set_appearance_mode('dark')



# funções ----------------------

def calcular():
    try:
        n1 = float(nota1.get())
        n2 = float(nota2.get())
        n3 = float(nota3.get())

        if (0 <= n1 <=10 and 0 <= n2 <=10 and 0 <= n3 <=10) !=True:
            resultado.configure(text='As notas devem estar entre 0 e 10.', text_color='orange')
            return

        media = (n1+n2+n3)/3

        if media >=5:
            resultado.configure(
                text=f'Média: {media:.2f} - Aprovado', text_color='green')
        else:
            resultado.configure(
                text=f'Média: {media:.2f} - Reprovado', text_color='red')
    except ValueError:
        resultado.configure(text='Digite somente números válidos.', text_color= 'orange')

# janela ------------------
janela = ctk.CTk('#1c1c1b')
janela.geometry('600x450')
janela.resizable(False, False)
janela.title('Sistema Escolar 2026')
janela.iconbitmap('ic_school_128_28729.ico')

# -----------------------------------------------------------------------------

# corpo da janela -------------------------------------------------------------

titulo = ctk.CTkLabel(janela,
                    text='Sistema Escolar',
                    text_color='yellow',
                    font=('arial', 50, 'bold'))
titulo.pack()

nota1 = ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    border_color='#FF8C00',
                    placeholder_text='Digite a sua 1ª nota:...')
nota1.pack(padx=10, pady=20)

nota2 = ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    border_color='#FF8C00',
                    placeholder_text='Digite a sua 2ª nota:...')
nota2.pack(padx=10, pady=20)

nota3 = ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    border_color='#FF8C00',
                    placeholder_text='Digite a sua 3ª nota:...')
nota3.pack(padx=10, pady=20)

botao = ctk.CTkButton(janela,
                    width=200,
                    height=40,
                    text='Calcular Média',
                    fg_color='green',
                    text_color='yellow',
                    cursor = 'hand2',
                    font=('arial',30),
                    hover_color="#053105",
                    command=calcular)
botao.pack(pady=10)


resultado = ctk.CTkLabel(janela,
                        text='',
                        text_color='white',
                        font=('arial',20))
resultado.pack(pady=10)



janela.mainloop()