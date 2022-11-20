import tkinter as tk
import os
from PIL import ImageTk, Image
from tkinter import filedialog

class MainFrame(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.titlefont = ("Helvetica", 18, "bold")
        self.title("Face Recognition by Eigenface")
        self.geometry("800x600")

        container = tk.Frame()
        container.grid(row=0, column=0, sticky="nesw")

        self.listing = {}

        for p in (WelcomePage, LobbyPage, WebcamPage):
            page_name = p.__name__
            frame = p(parent=container, controller=self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.listing[page_name] = frame

        self.up_frame('WelcomePage')

    def up_frame(self, page_name):
        page = self.listing[page_name]
        page.tkraise()
    
# Class ini buat welcome pagenya
class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        img = ImageTk.PhotoImage(Image.open("doc/meme/idk.jpg").resize((512, 512)))
        label = tk.Label(self, image = img)
        label.image = img
        label.pack()

        btn = tk.Button(self, text=  "To Main Program", command=lambda: controller.up_frame("LobbyPage"))
        btn.pack()

# Class ini buat lobby page di mana kita bisa upload gambar, tunjukkin gambar yang cocok (fitur spek)
class LobbyPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text = "Upload Page\n")
        label.pack()

        # btn = tk.Button(self, text=  "To Webcam Page", command=lambda: controller.up_frame("WebcamPage"))
        # btn.pack()

        def open_img():
            x = openfilename()
            img = Image.open(x)
            img = img.resize((256, 256), Image.ANTIALIAS)
        
            # PhotoImage class is used to add image to widgets, icons etc
            img = ImageTk.PhotoImage(img)
            panel = tk.Label(self, image = img)
            panel.image = img
            panel.grid(row = 2)

        def openfilename():
            filename = filedialog.askopenfilename(title ='Choose your image')
            return filename

        btn = tk.Button(self, text ='Click To Upload Image', command = open_img)
        btn.pack()

# Class ini buat webcam page di mana kita bisa ngecapture gambar, tunjukkin gambar yang cocok juga (bonus)
class WebcamPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text = "Webcam Page\n")
        label.pack()

        btn = tk.Button(self, text=  "To Lobby Page", command=lambda: controller.up_frame("LobbyPage"))
        btn.pack()

if __name__ == '__main__':
    app = MainFrame()
    app.resizable(False, False) 
    app.mainloop()