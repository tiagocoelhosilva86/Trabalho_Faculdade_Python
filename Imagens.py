from tkinter import *
from PIL import ImageTk, Image


class Imagens:
    def __init__(self, master=None):
        self.root = Tk()
        self.root.title('Album de Fotos')

        self.canvas = Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        # self.imagens1 = ImageTk.PhotoImage(Image.open("Img2.jpg"))  # PIL solution
        img1 = Image.open("imagens/Img1.jpg")
        img1 = img1.resize((200, 200), Image.ANTIALIAS)

        img2 = Image.open("imagens/Img2.jpg")
        img2 = img2.resize((200, 200), Image.ANTIALIAS)

        img3 = Image.open("imagens/Img3.jpg")
        img3 = img3.resize((200, 200), Image.ANTIALIAS)

        img4 = Image.open("imagens/Img4.jpg")
        img4 = img4.resize((200, 200), Image.ANTIALIAS)

        img5 = Image.open("imagens/Img5.jpg")
        img5 = img5.resize((200, 200), Image.ANTIALIAS)

        img6 = Image.open("imagens/Img6.jpg")
        img6 = img6.resize((200, 200), Image.ANTIALIAS)

        self.imagens1 = ImageTk.PhotoImage(img1)
        self.imagens2 = ImageTk.PhotoImage(img2)
        self.imagens3 = ImageTk.PhotoImage(img3)
        self.imagens4 = ImageTk.PhotoImage(img4)
        self.imagens5 = ImageTk.PhotoImage(img5)
        self.imagens6 = ImageTk.PhotoImage(img6)

        # self.l= Label(image=self.imagens1)
        self.canvas.create_image(20, 20, anchor=NW, image=self.imagens1)
        self.canvas.create_image(242, 20, anchor=NW, image=self.imagens2)
        self.canvas.create_image(464, 20, anchor=NW, image=self.imagens3)
        self.canvas.create_image(20, 290, anchor=NW, image=self.imagens4)
        self.canvas.create_image(242, 290, anchor=NW, image=self.imagens5)
        self.canvas.create_image(464, 290, anchor=NW, image=self.imagens6)

        self.root.mainloop()
