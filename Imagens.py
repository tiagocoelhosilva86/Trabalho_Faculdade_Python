from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image


class Imagens:
    def __init__(self, usuarioDb):
        self.nome = ''
        self.caminho = ''
        self.usuario = usuarioDb
        self.root = Tk()
        self.root.title('Album de Fotos')

        self.primeiroContainer = Frame(self.root)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(self.root)
        self.segundoContainer["padx"] = 10
        self.segundoContainer.pack()

        self.canvas = Canvas(self.segundoContainer, width=800, height=600)
        self.canvas.pack()

        self.botao = Button(self.primeiroContainer,
                            text="Selecione", command=self.salvarImagem)
        self.botao.pack(side=LEFT)

        self.carregarImagens()

        self.root.mainloop()

    def salvarImagem(self):
        filetypes = [('imagens', '.jpg')]

        caminho = fd.askopenfilename(
            title='Open a file', initialdir='/', filetypes=filetypes)

        self.usuario.salvarImagem('', caminho)

        self.carregarImagens()

    def carregarImagens(self):

        count = 0
        posx = 1
        posy = 5
        for imagem in self.usuario.carregarImagens():

            img1 = Image.open(imagem[2])
            img1 = img1.resize((200, 200), Image.ANTIALIAS)

            photoImage = ImageTk.PhotoImage(img1)

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
