from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import Dados as Dados

tela = Tk()
tela.geometry("400x600")
tela.resizable(width=False, height=False)


frame1 = Frame(tela, width=400, height=150, bg="gray")
frame1.pack(side=TOP)

frame2 = Frame(tela, width=400, height=450, bg="#3B4040")
frame2.pack(side=BOTTOM)

imagem = PhotoImage(file="icons/zem.png",)


canvas = Canvas(frame1, width=150, height=150, bg="gray" ,highlightthickness=0)
canvas.create_oval(10, 20, 145, 145, width=5, fill="white")
canvas.create_image(79, 85, image=imagem)
canvas.place(x=120, y=-10)





LoLabel = Label(frame2, text="Login" ,bg='#3B4040',fg="white", font=('Arial 20 bold'))
LoLabel.place(x=150, y=10)

NameLabel = Label(frame2, text="Nome:", bg="#3B4040", fg="white", font=('Arial 20 bold'))
NameLabel.place(x=15, y=55)

NameEntry = ttk.Entry(frame2, width=25, font=('Arial 13 bold'))
NameEntry.place(x=115, y=63)

PassLabel = Label(frame2, text="Senha:", bg="#3B4040", fg="white", font=('Arial 20 bold'))
PassLabel.place(x=15, y=120)

PassEntry = ttk.Entry(frame2, width=25, font=('Arial 13 bold'), show="*")
PassEntry.place(x=115, y=130)

def login():
    nome = NameEntry.get()
    senha = PassEntry.get()

    Dados.cursor.execute("""
    SELECT * FROM Dados
    WHERE (nome = ? AND senha = ?)
    """,(nome, senha))
    verificar = Dados.cursor.fetchone()

    try:
        if(nome in verificar and senha in verificar):
            messagebox.showinfo(title="Informações de Login", message="Acesso Permitido")
            imagem["file"] = "icons/ok2.png"
    except:
        messagebox.showinfo(title="Informações de Login", message="Acesso Negado, Verifique se está Cadastrado")
        imagem["file"] = "icons/bravo.png"

b1 = Button(frame2, text="Login", width=20, font=('Helvetica'), command=login)
b1.place(x=120, y=200)

def cadastrar():
    LoLabel['text'] = "Cadastro"
    imagem['file'] = 'icons/calmo.png'
    LoLabel.place(x=145)
    b1.place(x=10000)
    b2.place(x=10000)
    EmailLabel = Label(frame2, text="Email:", font=('Arial 20 bold'), bg="#3B4040", fg="white")
    EmailLabel.place(x=15, y=190)

    EmailEntry = ttk.Entry(frame2, width=25, font=('Arial 13 bold'))
    EmailEntry.place(x=115, y=198)

    def confirmar():
        nome = NameEntry.get()
        senha = PassEntry.get()
        email = EmailEntry.get()

        if (nome == "" and senha == "" and email == "" or email == "" or nome == "" or senha == ""):
            messagebox.showinfo(title="Informações de Login", message="Preencha todos os campos")
            imagem["file"] = "icons/bravo3.png"
        else:
            Dados.cursor.execute("""
            INSERT INTO Dados (nome, email, senha) VALUES(?, ?, ?)
        """ ,(nome, email, senha))
            Dados.conn.commit()
            messagebox.showinfo(title="Informações de Login", message="Cadastro Concluido")
            imagem["file"] = "icons/blz.png"

    b3 = Button(frame2, width=20, text="Cadastrar", font="Helvetiva", command= confirmar)
    b3.place(x=120, y=250)

    def voltar():
        LoLabel["text"] = "Login"
        LoLabel.place(x=150)
        b3.place(x=10000)
        b4.place(x=10000)
        EmailLabel.place(x=10000)
        EmailEntry.place(x=10000)
        imagem["file"] = "icons/zem.png"
        b1.place(x=120)
        b2.place(x=120)

    b4 = Button(frame2, text="Voltar", width=20, font=('Helvetica'), command=voltar)
    b4.place(x=120, y=300)



b2 = Button(frame2, text="Cadastre-se", width=20, font=('Helvetica'), command=cadastrar)
b2.place(x=120, y=250)




tela.mainloop()
