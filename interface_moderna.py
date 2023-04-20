import customtkinter

customtkinter.set_appearance_mode('dark')

customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.geometry('500x350')

texto = ''

def login():
    usuario = entry1.get()
    senha = entry2.get()
    if usuario == 'usuario' and senha == 'dev':
        msg= 'Autenticado\n'
    else:
        msg = 'Erro na autenticação\n'
    mensagem.insert('0.0', msg)


frame = customtkinter.CTkFrame(master = root)
frame.pack(pady = 20, padx = 60, fill = 'both', expand = True)

label = customtkinter.CTkLabel(master= frame, text = 'Sistema de Login', font = ('Roboto', 24))
label.pack(pady = 12, padx = 10)

entry1 = customtkinter.CTkEntry(master = frame, placeholder_text= 'Usuario')
entry1.pack(pady= 12, padx = 10)

entry2 = customtkinter.CTkEntry(master = frame, placeholder_text= 'Senha', show = '*')
entry2.pack(pady= 12, padx = 10)

button = customtkinter.CTkButton(master = frame, text = 'logar', command = login)
button.pack(pady = 12, padx = 10)

checkbox = customtkinter.CTkCheckBox(master = frame, text = 'Salvar senha' )
checkbox.pack(pady = 12, padx = 10)

mensagem = customtkinter.CTkTextbox(master= frame, font = ('Arial', 12))
mensagem.pack(pady = 12, padx = 10)

root.mainloop()