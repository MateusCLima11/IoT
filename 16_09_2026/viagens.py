import customtkinter as ctk
ctk.set_appearance_mode('dark')



# funções ----------------------

def calcular():
    d = int(distancia.get())
    c = float(consumo.get())
    p = float(preco.get())

    formula = (d/c)*p

    resultado.configure(text=f'O Valor para a viagem é de R${formula:.2f}')


# janela ------------------
janela = ctk.CTk()
janela.geometry('500x400')
janela.resizable(False, False)
janela.title('Calculadora de Viagem')
janela.iconbitmap('travelmaplocationpin_109805.ico')

# -----------------------------------------------------------------------------

# corpo da janela -------------------------------------------------------------

titulo = ctk.CTkLabel(janela,
                    text='APP VIAGEM',
                    text_color='white',
                    font=('arial', 50))
titulo.pack()

distancia = ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    border_color='#FF8C00',
                    placeholder_text='Digite a distância da viagem em KM:...')
distancia.pack(padx=10, pady=20)



consumo = ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    border_color='#8E8E8E',
                    placeholder_text='Digite o consumo do seu veículo:...',
                    )
consumo.pack(padx=10, pady=20)



preco = ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    border_color='#ECA927',
                    placeholder_text='Digite o preço do combustível:...',
                    )
preco.pack(padx=10, pady=20)


botao = ctk.CTkButton(janela,
                    width=200,
                    height=40,
                    text='Calcular Gasto',
                    fg_color='green',
                    text_color='white',
                    cursor = 'hand2',
                    font=('arial',30),
                    command=calcular)
botao.pack(pady=10)


resultado = ctk.CTkLabel(janela,
                        text='',
                        text_color='white',
                        font=('arial',20))
resultado.pack(pady=10)



janela.mainloop()