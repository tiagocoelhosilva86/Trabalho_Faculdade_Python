from tkinter import *

from UsuariosDB import UsuariosDB


class NovoUsuario:
    def __init__(self,master = None,  *args, **kwargs ):
        self.root = Tk()

        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(self.root)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(self.root)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(self.root)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(self.root)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(self.root)
        self.quintoContainer["pady"] = 20
        self.quintoContainer.pack()

        self.sextoContainer = Frame(self.root)
        self.sextoContainer["pady"] = 20
        self.sextoContainer.pack()

        self.setimoContainer = Frame(self.root)
        self.setimoContainer["pady"] = 20
        self.setimoContainer.pack()


        self.oitavoContainer = Frame(self.root)
        self.oitavoContainer["pady"] = 20
        self.oitavoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Tela de Cadastro")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.cpfLabel = Label(self.terceiroContainer, text="CPF", font=self.fontePadrao)
        self.cpfLabel.pack(side=LEFT)

        self.cpf = Entry(self.terceiroContainer)
        self.cpf["width"] = 30
        self.cpf["font"] = self.fontePadrao
        self.cpf.pack(side=LEFT)

        self.emailLabel = Label(self.quartoContainer, text="Email", font=self.fontePadrao)
        self.emailLabel.pack(side=LEFT)

        self.email = Entry(self.quartoContainer)
        self.email["width"] = 30
        self.email["font"] = self.fontePadrao
        self.email.pack(side=LEFT)

        self.usuarioLabel = Label(self.quintoContainer, text="Usuario", font=self.fontePadrao)
        self.usuarioLabel.pack(side=LEFT)

        self.usuario = Entry(self.quintoContainer)
        self.usuario["width"] = 30
        self.usuario["font"] = self.fontePadrao
        self.usuario.pack(side=LEFT)

        self.senhaLabel = Label(self.sextoContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.sextoContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.salvar = Button(self.setimoContainer)
        self.salvar["text"] = "Salvar"
        self.salvar["font"] = ("Calibri", "8")
        self.salvar["width"] = 12
        self.salvar["command"] = self.criarNovoUsuario
        self.salvar.pack()

        self.cancelar = Button(self.oitavoContainer)
        self.cancelar["text"] = "Cancelar"
        self.cancelar["font"] = ("Calibri", "8")
        self.cancelar["width"] = 12
        self.cancelar["command"] = self.fecharJanela
        self.cancelar.pack()

        self.mensagem = Label(self.setimoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        self.root.mainloop()

    def criarNovoUsuario(self):
        nome = self.nome.get()
        cpf = self.cpf.get()
        email = self.email.get()
        usuario = self.usuario.get()
        senha = self.senha.get()

        if nome != '' and cpf != '' and email != '' and usuario != '' and senha != '' :
            usuarioDb = UsuariosDB(0, nome, cpf, email, usuario, senha)
            if usuarioDb.insertUser() :
                self.mensagem["text"] = "Usuario salvo com sucesso"
            else :
                self.mensagem["text"] = "Falha ao salvar usuario"



    def fecharJanela(self):
        self.root.destroy()