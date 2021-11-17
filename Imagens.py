from tkinter import *

from PIL.Image import ImageTransformHandler


class Imagens:
    def __init__(self):
        self.root = Tk()
        self.root.title('Album de Fotos')
        self.root.iconbitmap('imagens/Img1.jpg')

        self.imagens1 = ImageTransformHandler.PhotoImagen(Image.open('imagens/Img1.jpg'))
        self.imagens2 = ImageTK.PhotoImagen(Image.open('imagens/Img2.jpg'))
        self.imagens3 = ImageTK.PhotoImagen(Image.open('imagens/Img3.jpg'))
        self.imagens4 = ImageTK.PhotoImagen(Image.open('imagens/Img4.jpg'))
        self.imagens5 = ImageTK.PhotoImagen(Image.open('imagens/Img5.jpg'))
        self.imagens6 = ImageTK.PhotoImagen(Image.open('imagens/Img6.jpg'))

        self.imagens = [imagens1,imagens2,imagens3,imagens4,imagens5,imagens6]

        # imagens = Label(imagens=imagens1)
        self.imagens.grid(row=0,columm=0,columnspan=3)

        self.button_votar = Button(self.root, text="<<", command=self.back, state=DISABLED)
        self.button_exit = Button(self.root, text="Sair do programa", command=self.root.quit)
        self.button_proximo = Button(self.root, text=">>", command=lambda: self.forward(2))

        self.button_votar.grid(row=1, column=0)
        self.button_exit.grid(row=1, column=1)
        self.button_proximo.grid(row=1, column=2)

        self.root.mainloop()

    def forward(imagens_number):
        global  imagens
        global  button_voltar
        global  button_proximo

        my_label.grid_forget()
        my_label = Label(imagens = imagens_list[imagens_number-1])
        button_proximo = Button(root,text=">>",command=lambda:forward(imagens_number+1))
        button_voltar = Button(root,text="<<",command=lambda :back(imagens_number-1))

        if imagens_number == 5:
            button_proximo = Button(root,text=">>",state=DISABLED)


        my_label.grid(row=0,column=0,columnspan=3)
        button_voltar.grid(row=1,column=0)
        button_proximo.grid(row=1, column=2)

    def back(imagens_number):
        global my_label
        global button_votar
        global button_proximo

        my_label.grid_forget()
        my_label = Label(imagens=imagens_list[imagens_number - 1])
        button_proximo = Button(root, text=">>", command=lambda: forward(imagens_number + 1))
        button_voltar = Button(root, text="<<", command=lambda: back(imagens_number - 1))

        if imagens_number == 1:
            button_votar = Button(root,text="<<",state=DISABLED)

        my_label.grid(row=0, column=0, columnspan=3)
        button_voltar.grid(row=1, column=0)
        button_proximo.grid(row=1, column=2)





