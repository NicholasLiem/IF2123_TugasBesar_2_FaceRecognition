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


# # Create a button and place it into the window using grid layout
#         btn = tk.Button(self, text ='Click To Upload Image', command = open_img).grid(row = 1, columnspan = 4)

#     def open_img():
#             # Select the Imagename  from a folder
#             x = openfilename()
        
#             # opens the image
#             img = Image.open(x)
            
#             # resize the image and apply a high-quality down sampling filter
#             img = img.resize((250, 250), Image.ANTIALIAS)
        
#             # PhotoImage class is used to add image to widgets, icons etc
#             img = ImageTk.PhotoImage(img)
        
#             # create a label
#             panel = Label(root, image = img)
            
#             # set the image as img
#             panel.image = img
#             panel.grid(row = 2)

#         def openfilename():
#         # open file dialog box to select image
#         # The dialogue box has a title "Open"
#             filename = filedialog.askopenfilename(title ='"pen')
#             return filename