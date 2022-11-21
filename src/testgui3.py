import tkinter as tk
import os
from PIL import ImageTk, Image
from tkinter import filedialog
import main as main
import imgparsing as imp
import matplotlib.pyplot as plt
import timehandling as t

class MainFrame(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.titlefont = ("Helvetica", 18, "bold")
        self.title("Face Recognition by Eigenface")
        self.geometry("1000x600")

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
        
        l1 = tk.Label(self,text="WELCOME TO OUR APP",font=16,fg="black")
        l1.grid(row=0,column=0,padx=400,pady=25)

        # img = ImageTk.PhotoImage(Image.open("doc/meme/sample.png").resize((512, 512)))
        # label = tk.Label(self, image = img)
        # label.image = img
        # label.pack()

        btn = tk.Button(self, text=  "To Face Recognition Page", command=lambda: controller.up_frame("LobbyPage"))
        btn.grid(row=1,column=0, pady=10)

        btn2 = tk.Button(self, text = "To Webcam Page", command = lambda: controller.up_frame("WebcamPage"))
        btn2.grid(row=2,column=0, pady=10)

# Class ini buat lobby page di mana kita bisa upload gambar, tunjukkin gambar yang cocok (fitur spek)
class LobbyPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        frameTop = tk.Frame(self, padx=5,pady=5)
        frameTop.pack(pady=10,padx=10)

        label = tk.Label(frameTop, text = "Face Recognition", font = ("Helvetica",30))
        label.pack(pady=10,padx=10)

        my_canvas = tk.Canvas(frameTop, width=900, height=10)
        my_canvas.pack()

        my_canvas.create_line(0,10,900,10,fill="black")

        frameBody = tk.Frame(self, padx=5,pady=5)
        frameBody.pack(pady=20,padx=20)

        frame3 = tk.Frame(frameBody,padx=5,pady=5,width=300)
        frame3.pack(side="left",padx=5)

        
        def openfoldername():
            global foldernames
            foldername = filedialog.askdirectory(title = 'Select your Test Folder',initialdir=os.getcwd())
            foldernames = cutstring(foldername)
            labelFolder.config(text=foldernames)
            return foldernames
        
        label1 = tk.Label(frame3, text = "Insert Your Dataset", font=("Helvetica",15))
        label1.grid(row=0,column=0,padx=10,pady=10)

        btn1 = tk.Button(frame3, text="Choose Folder", font=("Helvetica",12), command = openfoldername)
        btn1.grid(row=1,column=0,padx=10)

        labelFolder = tk.Label(frame3, text="No Folder", font=("Helvetica",10))
        labelFolder.grid(row=1,column=1)
        
        label2 = tk.Label(frame3, text="Insert Your Image", font=("Helvetica",15))
        label2.grid(row=2,column=0,padx=10,pady=10)

        def cutstring(s):
            simpan = ""
            reverse = ""
            for i in range(len(s)):
                if s[len(s)-1-i] != '/':
                    simpan+=s[len(s)-1-i]
                else:
                    break
            for i in range(len(simpan)):
                reverse += simpan[len(simpan)-1-i]
            return reverse
            
        def open_img():
            x = openfilename()
            img = Image.open(x)
            img = img.resize((256, 256))
        
            # PhotoImage class is used to add image to widgets, icons etc
            img = ImageTk.PhotoImage(img)
            my_image = tk.Label(frame4, image=img)
            my_image.image = img
            my_image.grid(column=0,row=1)
            imagename = cutstring(x)
            labelImage.config(text=imagename)
        
        def openfilename():
            global filename
            filename = filedialog.askopenfilename(title ='Choose your image',initialdir=os.getcwd())
            return filename

        def processRecognition():
            t.tic()
            database = []
            datalabel = []
            imp.read_training_data_set(foldernames,database,datalabel)
            idx = main.process(database,cutstring(filename))
            t.tac()

            hour = f"{t.t_hour:02}"
            min = f"{t.t_min:02}"
            sec = f"{t.t_sec:02}"
            time = hour + "." + min + "." + sec

            path = os.getcwd() + "\\test\\database\\" + foldernames + "\\" + datalabel[idx]
            labelTimeRes.config(text=time)
            
            resultImg = Image.open(path)
            resultImg = resultImg.resize((256,256))
            resultImg = ImageTk.PhotoImage(resultImg)
            res_img = tk.Label(frame5,image=resultImg)
            res_img.image = resultImg
            res_img.grid(column=0,row=1)
            labelResult.config(text=datalabel[idx])

        btn2 = tk.Button(frame3, text="Choose Image", font=("Helvetica",12),command=open_img)
        btn2.grid(row=3,column=0,padx=10)


        labelImage = tk.Label(frame3, text="No Image",font=("Helvetica",10))
        labelImage.grid(row=3,column=1)

        label3 = tk.Label(frame3, text="Result :", font=("Helvetica",13))
        label3.grid(row=4,column=0,pady=15)

        labelResult = tk.Label(frame3, text="Hasil Test", font=("Helvetica",13), fg="green")
        labelResult.grid(row=5,column=0)

        labelTime = tk.Label(frame3, text ="Execution Time :", font=("Helvetica",13))
        labelTime.grid(row=6,column=0,pady=15,padx=5)

        labelTimeRes = tk.Label(frame3, text = "Time Result", font=("Helvetica",13), fg = "green")
        labelTimeRes.grid(row=7, column=0)

        frame4 = tk.Frame(frameBody,padx=5,pady=5,width=300)
        frame4.pack(side="left",padx=5)

        label4 = tk.Label(frame4, text="Test Image", font=("Helvetica",15))
        label4.grid(column=0,row=0)

        frame_image = tk.Frame(frame4,width=256,height=256,highlightbackground="black",highlightthickness=1)
        frame_image.grid(row=1,column=0)

        frame5 = tk.Frame(frameBody,padx=5,pady=5,width=300)
        frame5.pack(side="left",padx=5)
        
        label5 = tk.Label(frame5, text="Closest Result", font=("Helvetica",15))
        label5.grid(row=0,column=0)

        frame_result = tk.Frame(frame5,width=256,height=256,highlightbackground="black",highlightthickness=1)
        frame_result.grid(row=1,column=0)

        frameBottom = tk.Frame(self,padx=5, pady=5)
        frameBottom.pack(padx=10,pady=10)

        btnWelcome = tk.Button(frameBottom, text="Welcome Page", command=lambda: controller.up_frame("WelcomePage"), justify="right")
        btnWelcome.pack(side="left",padx=75)

        btnExecute = tk.Button(frameBottom, text="Proceed Recognition",font=("Helvetica",15,"bold"),command=processRecognition)
        btnExecute.pack(side="left",padx=100)

        btnWebcam = tk.Button(frameBottom, text="Webcam Page", command =lambda: controller.up_frame("WebcamPage"), justify="left")
        btnWebcam.pack(side="right",padx=100)


# Class ini buat webcam page di mana kita bisa ngecapture gambar, tunjukkin gambar yang cocok juga (bonus)
class WebcamPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        frameTop = tk.Frame(self, padx=5,pady=5)
        frameTop.pack(pady=10,padx=10)

        label = tk.Label(frameTop, text = "Live Webcam Recognition", font = ("Helvetica",30))
        label.pack(pady=10,padx=10)

        my_canvas = tk.Canvas(frameTop, width=900, height=10)
        my_canvas.pack()

        my_canvas.create_line(0,10,900,10,fill="black")

        frameBody = tk.Frame(self,padx=5,pady=5)
        frameBody.pack(pady=20,padx=20)

        frame1 = tk.Frame(frameBody, padx=5, pady=5)
        frame1.pack(side="left",padx=5)

        label1 = tk.Label(frame1,text="Insert Your Image Folder",font=("Helvetica",15))
        label1.grid(column=0,row=0,padx=10,pady=10)

        btn1 = tk.Button(frame1,text="Choose Folder",font=("Helvetica",13))
        btn1.grid(column=0,row=1,padx=10)

        labelFolder = tk.Label(frame1,text="No Folder Selected",font=("Helvetica",12))
        labelFolder.grid(column=1,row=1)

        frame2 = tk.Frame(frameBody, padx=5, pady=5)
        frame2.pack(side="left",padx=5)

        labelWebcam = tk.Label(frame2,text="Webcam View",font=("Helvetica",12))
        labelWebcam.grid(column=0,row=0)

        frame_webcam = tk.Label(self,width=20,height=20,highlightbackground="black",highlightthickness="1")
        frame_webcam.pack()

        btn = tk.Button(self, text=  "To Face Recognition Page", command=lambda: controller.up_frame("LobbyPage"))
        btn.pack()


        btn2 = tk.Button(self, text = "To Welcome Page", command = lambda: controller.up_frame("WelcomePage"))
        btn2.pack()

if __name__ == '__main__':
    app = MainFrame()
    app.resizable(False, False)
    app.mainloop()