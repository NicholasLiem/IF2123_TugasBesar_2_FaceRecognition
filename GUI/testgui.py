# from tkinter import *
# from PIL import ImageTk, Image
# from tkinter import filedialog 
# import os 
# root = Tk()
# root.title("Face Recognition")


# def open():
#     global my_image
#     root.filename = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select an Image", filetypes=(("png files", "*.png"),("jpg files", "*.jpg")))
#     my_label = Label(root, text = root.filename).pack()
#     my_image = ImageTk.PhotoImage(Image.open(root.filename))
#     my_image_label = Label(image=my_image).pack()

# my_btn = Button(root, text="Open File", command=open).pack()
# root.mainloop()


# from tkinter import *
# from PIL import ImageTk, Image
# from tkinter import filedialog
# import os
# window = Tk()
# window.title("Face Recognition")
# window.geometry("500x400")



# frame1 = Frame(window,width=20,highlightbackground="black",highlightthickness=1)

# frame1.grid(row=0,column=0,padx=20,pady=20,ipadx=0,ipady=0)

# l1 = Label(frame1, text="Text Placeholder",fg="blue",font=(14))
# l1.grid(row=0,column=0,padx=10,pady=10)


# def open():
#     global my_image
#     frame1.filename = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select an Image", filetypes=(("png files", "*.png"),("jpg files", "*.jpg")))
#     # my_label = Label(frame1, text = frame1.filename).pack()
#     my_image = ImageTk.PhotoImage(Image.open(frame1.filename))
#     my_image_label = Label(frame1,image=my_image)
#     my_image_label.grid(row=0,column=0,padx=0,pady=0)

# button1 = Button(window,text="Choose folder",fg="blue",font=(16),command=open)
# button1.grid(padx=20,pady=5,sticky=W)

# window.mainloop()


import tkinter as tk

class MainFrame(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.titlefont = ("Helvetica", 18, "bold")
        self.title("Face Recognition by Eigenface brought to you by HTS Team")
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
    

class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text = "Welcome Page\n")
        label.pack()

        btn = tk.Button(self, text=  "To Page Upload", command=lambda: controller.up_frame("LobbyPage"))
        btn.pack()

class LobbyPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text = "Upload Page\n")
        label.pack()

        btn = tk.Button(self, text=  "To Webcam Page", command=lambda: controller.up_frame("WebcamPage"))
        btn.pack()

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
    app.mainloop()