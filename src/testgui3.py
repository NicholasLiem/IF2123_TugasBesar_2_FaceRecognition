# import modul-modul yang diperlukan main program + gui
import tkinter as tk
import os
from PIL import ImageTk, Image
from tkinter import filedialog
import main as main
import imgparsing as imp
import matplotlib.pyplot as plt
import timehandling as t

# MainFrame Class
class MainFrame(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.titlefont = ("Helvetica", 18, "bold")
        self.title("Face Recognition by Eigenface")
        self.geometry("1000x600")

        container = tk.Frame()
        container.grid(row=0, column=0, sticky="nesw")

        self.listing = {}

        for p in (WelcomePage, LobbyPage):
            page_name = p.__name__
            frame = p(parent=container, controller=self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.listing[page_name] = frame

        self.up_frame('WelcomePage')

    def up_frame(self, page_name):
        page = self.listing[page_name]
        page.tkraise()
    
# Welcome page class
class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        l1 = tk.Label(self,text="WELCOME TO OUR APP",font=("Helvetica",20,"bold"),fg="black")
        l1.grid(row=0,column=0,padx=340,pady=20)

        btn = tk.Button(self, text=  "To Face Recognition Page", font = ("Helvetica",14), command=lambda: controller.up_frame("LobbyPage"))
        btn.grid(row=1,column=0, pady=10)

        img = ImageTk.PhotoImage(Image.open("doc/meme/idk.jpg").resize((356,356)))
        label = tk.Label(self, image = img)
        label.image = img
        label.grid(row=3,column=0)

# LobbyPage class for main feature, face recognition
class LobbyPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # frame untuk header (judul program dan garis bawah)
        frameTop = tk.Frame(self, padx=5,pady=5)
        frameTop.pack(pady=10,padx=10)

        # menampilkan judul program
        label = tk.Label(frameTop, text = "Face Recognition", font = ("Helvetica",30))
        label.pack(pady=10,padx=10)

        # membuat line untuk garis bawah judul program
        my_canvas = tk.Canvas(frameTop, width=900, height=10)
        my_canvas.pack()
        my_canvas.create_line(0,10,900,10,fill="black")

        # frame untuk body program (bagian insert data dan tampilan image)
        frameBody = tk.Frame(self, padx=5,pady=5)
        frameBody.pack(pady=0,padx=0)

        # frame dalam frameBody untuk bagian insert data dan tampilan hasil run program
        frame3 = tk.Frame(frameBody,padx=5,pady=5)
        frame3.pack(side="left",padx=5)

        # fungsi untuk open folder
        def openfoldername():
            global foldernames
            foldername = filedialog.askdirectory(title = 'Select your Test Folder',initialdir=os.getcwd())
            foldernames = cutstring(foldername)
            labelFolder.config(text=foldernames)
            return foldernames
        
        # menampilkan tulisan "Insert Your Dataset" pada frame3
        label1 = tk.Label(frame3, text = "Insert Your Dataset", font=("Helvetica",15))
        label1.grid(row=0,column=0,padx=10,pady=10)

        # button untuk memilih folder dataset
        btn1 = tk.Button(frame3, text="Choose Folder", font=("Helvetica",12), command = openfoldername)
        btn1.grid(row=1,column=0,padx=10)

        # menampilkan nama folder yang dipilih
        labelFolder = tk.Label(frame3, text="No Folder Choosen", font=("Helvetica",10), bg="#D3D3D3")
        labelFolder.grid(row=1,column=1)
        
        # menampilkan tulisan "Insert Your Image" pada frame3
        label2 = tk.Label(frame3, text="Insert Your Image", font=("Helvetica",15))
        label2.grid(row=2,column=0,padx=10,pady=10)

        # fungsi untuk mendapatkan nama image beserta extensionnya (.jpg) dari path image tsb
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
        
        # fungsi untuk membuka dan menampilkan image yang dipilih oleh user
        def open_img():
            # mengambil path dari image yang dipilih user
            x = openfilename()
            img = Image.open(x)
            img = img.resize((256, 256))
        
            # menampilkan image yang dibuka oleh user ke frame4
            img = ImageTk.PhotoImage(img)
            my_image = tk.Label(frame4, image=img)
            my_image.image = img
            my_image.grid(column=0,row=1)

            # mengambil nama image beserta extensionnya
            imagename = cutstring(x)

            # menampilkan nama image yang diplih user
            labelImage.config(text=imagename)
        
        # fungsi pendukung untuk membuka mengambil path dari file image
        def openfilename():
            global filename
            filename = filedialog.askopenfilename(title ='Choose your image',initialdir=os.getcwd())
            return filename

        # fungsi utama program untuk menjalankan face recognition untuk membandingkan 
        # image yang dipilih dengan image dalam dataset yang diuji
        def processRecognition():
            # mulai menghitung waktu proses
            t.tic()

            # proses face recognition
            database = []
            datalabel = []
            imp.read_training_data_set(foldernames,database,datalabel)
            hasil = main.process(database,cutstring(filename))
            idx = hasil[0]

            # selesai menghitung waktu proses
            t.tac()

            # mengambil execution time proses face recognition
            hour = f"{t.t_hour:02}"
            min = f"{t.t_min:02}"
            sec = f"{t.t_sec:02}"
            time = hour + "." + min + "." + sec

            # menampilkan execution time program
            labelTimeRes.config(text=time)

            # mengambil path image result yang cocok untuk kembali ditampilkan dalam gui
            path = os.getcwd() + "\\test\\database\\" + foldernames + "\\" + datalabel[idx]
            
            # menampilkan result image yang sesuai ke frame5
            resultImg = Image.open(path)
            resultImg = resultImg.resize((256,256))
            resultImg = ImageTk.PhotoImage(resultImg)
            res_img = tk.Label(frame5,image=resultImg)
            res_img.image = resultImg
            res_img.grid(column=0,row=1)

            # menampilkan nama image yang cocok dari hasil face recognition
            labelResult.config(text=datalabel[idx])

            # memproses percent_match dan menampilkannya
            w = hasil[1]
            nilai = hasil[2]
            k = hasil[3]
            persen = main.percent_match(w,nilai[idx],k)
            persen = round(persen,2)
            persen_text = str(persen) + "%"
            labelPersenRes.config(text=persen_text)

        # button untuk memilih image yang ingin dipakai
        btn2 = tk.Button(frame3, text="Choose Image", font=("Helvetica",12),command=open_img)
        btn2.grid(row=3,column=0,padx=15)

        # menampilkan nama image yang dipilih
        labelImage = tk.Label(frame3, text="No Image Choosen",font=("Helvetica",10), bg="#D3D3D3")
        labelImage.grid(row=3,column=1)

        # menampilkan nama image yang paling mendekati test image
        label3 = tk.Label(frame3, text="Result :", font=("Helvetica",13))
        label3.grid(row=4,column=0,pady=10)
        labelResult = tk.Label(frame3, text="Hasil Test", font=("Helvetica",13), fg="green")
        labelResult.grid(row=5,column=0)

        # menampilkan waktu execution time
        labelTime = tk.Label(frame3, text ="Execution Time :", font=("Helvetica",13))
        labelTime.grid(row=6,column=0,pady=10,padx=5)
        labelTimeRes = tk.Label(frame3, text = "Time Result", font=("Helvetica",13), fg = "green")
        labelTimeRes.grid(row=7, column=0)

        # menampilkan percent_match
        labelPersen = tk.Label(frame3, text = "Percent Matched :",font=("Helvetica",13), pady=10)
        labelPersen.grid(row=8,column=0)
        labelPersenRes = tk.Label(frame3, text="???", font=("Helvetica",13), fg="green")
        labelPersenRes.grid(row=8,column=1)

        # frame dalam frameBody untuk bagian menampilkan image test
        frame4 = tk.Frame(frameBody,padx=5,pady=5)
        frame4.pack(side="left",padx=5)

        # menampilkan tulisan "Test Image" pada frame4 (di bagian atas image test)
        label4 = tk.Label(frame4, text="Test Image", font=("Helvetica",15))
        label4.grid(column=0,row=0)

        # placeholder untuk image test
        placeHolderTest = ImageTk.PhotoImage(Image.open("src/img/img_placeholder.jpg").resize((256,256)))
        label = tk.Label(frame4, image = placeHolderTest)
        label.image = placeHolderTest
        label.grid(row=1,column=0)

        # frame dalam frameBody untuk bagian menampilkan image result
        frame5 = tk.Frame(frameBody,padx=5,pady=5)
        frame5.pack(side="left",padx=5)
        
        # menampilkan tulisan "Closest Result" pada frame5 (di bagian atas image result)
        label5 = tk.Label(frame5, text="Closest Result", font=("Helvetica",15))
        label5.grid(row=0,column=0)

        # placeholder untuk image result
        placeHolderRes = ImageTk.PhotoImage(Image.open("src/img/img_placeholder.jpg").resize((256,256)))
        labelRes = tk.Label(frame5, image = placeHolderRes)
        labelRes.image = placeHolderRes
        labelRes.grid(row=1,column=0)

        # frame untuk bagian bottom
        frameBottom = tk.Frame(self,padx=5, pady=5)
        frameBottom.pack(padx=10,pady=10)

        # button untuk berpindah ke welcome page
        btnWelcome = tk.Button(frameBottom, text="Back To Welcome", font=("Helvetica",12), command=lambda: controller.up_frame("WelcomePage"))
        btnWelcome.pack(side="left",padx=80)

        # button untuk mengeksekusi proses face recognition
        btnExecute = tk.Button(frameBottom, text="Proceed Recognition",font=("Helvetica",15,"bold"),command=processRecognition)
        btnExecute.pack(side="left",padx=210)


if __name__ == '__main__':
    app = MainFrame()
    app.resizable(False, False)
    app.mainloop()