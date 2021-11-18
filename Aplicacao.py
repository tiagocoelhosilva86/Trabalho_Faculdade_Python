import sqlite3
from _ast import Import
from tkinter import *

from Imagens import Imagens
from NovoUsuario import NovoUsuario
from UsuariosDB import UsuariosDB


class Application:
    def __init__(self, master=None):
        self.root = master
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 20
        self.quintoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Tela de Login")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.novoUsuario = Button(self.quintoContainer)
        self.novoUsuario["text"] = "Cadastrar"
        self.novoUsuario["font"] = ("Calibri", "8")
        self.novoUsuario["width"] = 12
        self.novoUsuario["command"] = self.criarNovoUsuario
        self.novoUsuario.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()

        usuarioDb = UsuariosDB()

        if usuarioDb.validarUsuarioSenha(usuario, senha):
            self.mensagem["text"] = "Autenticado"
            self.root.destroy()
            Imagens()
        else:
            self.mensagem["text"] = "Erro na autenticação"

    def criarNovoUsuario(self):
        NovoUsuario()




root = Tk()
Application(root)
root.mainloop()