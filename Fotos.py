try:
    import tkinter as tk
    import Tkinter as tk


def download_images():

    try:
        impo t urllib.request as url
    except ImportError:
        import urllib as url
    url.urlretrieve("https://i.stack.imgur.com/IgD2r.png", "lenna.png")
    url.urlretrieve("https://i.stack.imgur.com/sML82.gif", "lenna.gif")


if __== '__main__':
    download_images()
    root = tk.Tk()
    widget = tk.Label(root, compound='top')
    widget.lenna_image_png = tk.PhotoImage(file="lenna.png")
    widget.lenna_image_gif = tk.PhotoImage(file="lenna.gif")
    try:
        widget['text'] = "Lenna.png"
        widget['image'] = widget.lenna_image_png
    except:
        widget['text'] = "Lenna.gif"
        widget['image'] = widget.lenna_image_gif
    widget.pack()
    root.mainloop()