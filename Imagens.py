import os
from math import ceil
from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image


class Imagens:
    def __init__(self, usuarioDb):
        self.usuario = usuarioDb
        self.imagens = []
        self.root = Tk()
        self.quadroAtual = 1
        self.total_quadros = 1
        self.root.title('Album de Fotos')

        self.primeiroContainer = Frame(self.root)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(self.root)
        self.segundoContainer["padx"] = 10
        self.segundoContainer.pack()

        self.botaoAnterior = Button(self.primeiroContainer,
                                    text="Anterior", command=self.voltarQuadro)
        self.botaoAnterior.pack(side=LEFT)

        self.botao = Button(self.primeiroContainer,
                            text="Selecione", command=self.salvarImagem)
        self.botao.pack(side=LEFT)

        self.botaoProximo = Button(self.primeiroContainer,
                                   text="Proximo", command=self.proximoQuadro)
        self.botaoProximo.pack(side=LEFT)

        self.canvas = Canvas(self.root, width=600, height=600)
        self.canvas.pack()

        self.imagens = self.usuario.carregarImagens()
        
        self.qtdImagens = len(self.imagens)
        total = self.qtdImagens /9

        if(total > 1):
            self.total_quadros = ceil(total)

        self.carregarImagens()

        self.root.mainloop()

    def salvarImagem(self):
        filetypes = [('imagens', '.jpg')]

        caminho = fd.askopenfilename(
            title='Open a file', initialdir='/', filetypes=filetypes)

        # pega o nome do arquivo
        nome = os.path.basename(caminho)

        path = os.path.abspath(os.getcwd())

        image = Image.open(caminho)
        image.resize((200, 200), Image.ANTIALIAS)
        image.save(path+'\\imagens\\'+nome)

        self.usuario.salvarImagem('', "imagens/"+nome)
        self.imagens = self.usuario.carregarImagens()
        self.quadroAtual = 1
        
        self.qtdImagens = len(self.imagens)
        total = self.qtdImagens /9

        if(total > 1):
            self.total_quadros = ceil(total)
        
        self.carregarImagens()
    
    def carregarImagens(self):

        count = 0
        posx = 1
        posy = 5
        self.imagelist = []  # for storing those images

        self.canvas.delete('all')
        i = 1

        for imagem in self.imagens[(self.quadroAtual * 9 - 9): (self.quadroAtual * 9)]:

            img1 = Image.open(imagem[2])
            img1 = img1.resize((200, 200), Image.ANTIALIAS)
            photoImage = ImageTk.PhotoImage(img1)
            self.imagelist.append(photoImage)

            self.canvas.create_image(posy, posx, anchor=NW, image=photoImage)

            count = count + 1
            if count == 9:
                break

            if count == 0 or count == 3 or count == 6:
                posy = 5
            elif count == 1 or count == 4 or count == 7:
                posy = 210
            elif count == 2 or count == 5 or count == 8:
                posy = 415

            if count > 2 and count < 5:
                posx = 205
            elif count > 5 and count < 8:
                posx = 410

    def proximoQuadro(self):
        qtdImagens = len(self.imagens)

        if qtdImagens > 9 and self.quadroAtual < self.total_quadros:
            self.quadroAtual =  self.quadroAtual + 1
            self.carregarImagens()


    def voltarQuadro(self):
        if self.quadroAtual > 1:
            self.quadroAtual =  self.quadroAtual - 1
            self.carregarImagens()

