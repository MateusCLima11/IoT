import customtkinter as ctk
ctk.set_appearance_mode('dark')



# janela ------------------
janela = ctk.CTk()
janela.geometry('500x350')
janela.resizable(False, False)
janela.title('Acesso Sócio Esquadrão - 2026')
janela.iconbitmap('security-protection-protect-key-password-login_108554.ico')

# -----------------------------------------------------------------------------

# corpo da janela -------------------------------------------------------------

titulo = ctk.CTkLabel(janela,
                    text='Sistema de Login',
                    text_color='#41d141',
                    font=('arial', 50))
titulo.pack()

login = ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    border_color='#41d141',
                    placeholder_text='Digite seu login:...')
login.pack(pady=20)



senha = ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    border_color='#41d141',
                    placeholder_text='Digite sua senha:...',
                    show='🤷‍♂️')
senha.pack()

botao = ctk.CTkButton(janela,
                    width=200,
                    height=40,
                    text='Acessar',
                    fg_color='#41d141',
                    text_color='white',
                    cursor = 'hand2',
                    font=('arial',30))
botao.pack(pady=30)





janela.mainloop()