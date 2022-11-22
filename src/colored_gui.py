import customtkinter
import tkinter as tk
from PIL import Image, ImageTk
import os 
import main as main
import imgparsing as imp
import timehandling as t
from tkinter import filedialog

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # set background color to dark gray
        App.configure(self,fg_color="#383838")
        self.geometry("1100x650")
        self.title("Face Recognition By Eigenface")

        # top frame
        frame = customtkinter.CTkFrame(master=self,
                               width=1050,
                               height=125,
                               corner_radius=10,
                               fg_color = "#3C4048",
                               border_color="white",
                               border_width=1)
        frame.pack(padx=10, pady=10)

        text_var = tk.StringVar(value="FACE RECOGNITION")
        label = customtkinter.CTkLabel(master=frame,
                                    textvariable=text_var,
                                    text_font=("Helvetica",33),
                                    corner_radius=8)
        label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # frame for displaying test image and closest result image
        frameImage = customtkinter.CTkFrame(master=self,corner_radius=10,fg_color="#383838")
        frameImage.pack(pady=0,padx=50,side="right")

        # frame for displaying statistic result
        frameHasil = customtkinter.CTkFrame(master=self,corner_radius=10,width=450,fg_color="#3C4048",border_width=1,border_color="white")
        frameHasil.pack(pady=0,padx=50,side="left")

        label1 = customtkinter.CTkLabel(master=frameHasil, text = "Insert Your Dataset", text_font=("Helvetica",12,"bold"))
        label1.grid(row=0,column=0,padx=10,pady=10)

        def openfoldername():
            global foldernames
            foldername = filedialog.askdirectory(title = 'Select your Test Folder',initialdir=os.getcwd())
            foldernames = cutstring(foldername)
            labelFolder.configure(text=foldernames)
            return foldernames
        
        btn1 = customtkinter.CTkButton(master=frameHasil, width=100,height=32,border_width=1, text="Choose Folder",command=openfoldername)
        btn1.grid(row=1,column=0,padx=10)

        labelFolder = customtkinter.CTkLabel(master=frameHasil, text="No Folder Choosen")
        labelFolder.grid(row=1,column=1)
        
        label2 = customtkinter.CTkLabel(master=frameHasil, text="Insert Your Image", text_font = ("Helvetica",12,"bold"))
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
        
        # fungsi untuk membuka dan menampilkan image yang dipilih oleh user
        def open_img():
            # mengambil path dari image yang dipilih user
            x = openfilename()
            img = Image.open(x)
            img = img.resize((256, 256))
        
            # menampilkan image yang dibuka oleh user ke frame4
            img = ImageTk.PhotoImage(img)
            my_image = tk.Label(frameTest, image=img)
            my_image.image = img
            my_image.grid(column=0,row=1)

            # mengambil nama image beserta extensionnya
            imagename = cutstring(x)

            # menampilkan nama image yang diplih user
            labelImage.configure(text=imagename)
        
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
            label6.configure(text=time)

            # mengambil path image result yang cocok untuk kembali ditampilkan dalam gui
            path = os.getcwd() + "\\test\\database\\" + foldernames + "\\" + datalabel[idx]
            
            # menampilkan result image yang sesuai ke frame5
            resultImg = Image.open(path)
            resultImg = resultImg.resize((256,256))
            resultImg = ImageTk.PhotoImage(resultImg)
            res_img = tk.Label(frameHasilTest,image=resultImg)
            res_img.image = resultImg
            res_img.grid(column=0,row=1)

            # menampilkan nama image yang cocok dari hasil face recognition
            label4.configure(text=datalabel[idx])

            # memproses percent_match dan menampilkannya
            w = hasil[1]
            nilai = hasil[2]
            k = hasil[3]
            persen = main.percent_match(w,nilai[idx],k)
            persen = round(persen,2)
            persen_text = str(persen) + "%"
            label8.configure(text=persen_text)

        btn2 = customtkinter.CTkButton(master=frameHasil, width=100,height=32,border_width=1, text="Choose Image",command=open_img)
        btn2.grid(row=3,column=0,padx=10)

        labelImage = customtkinter.CTkLabel(master=frameHasil, text="No Image Choosen")
        labelImage.grid(row=3,column=1)

        label3 = customtkinter.CTkLabel(master=frameHasil, text="Result :", text_font=("Helvetica",12,"bold"))
        label3.grid(row=4,column=0,pady=5)

        label4 = customtkinter.CTkLabel(master=frameHasil, text="Test Result", text_font=("Helvetica",11))
        label4.grid(row=5,column=0,pady=0)

        label5 = customtkinter.CTkLabel(master=frameHasil, text="Execution Time :", text_font=("Helvetica",12,"bold"))
        label5.grid(row=6,column=0,pady=5)

        label6 = customtkinter.CTkLabel(master=frameHasil, text="Time Result", text_font=("Helvetica",12,"bold"))
        label6.grid(row=7,column=0,pady=5)

        label7 = customtkinter.CTkLabel(master=frameHasil, text="Percent Matched :", text_font=("Helvetica",12,"bold"))
        label7.grid(row=8,column=0,pady=5)

        label8 = customtkinter.CTkLabel(master=frameHasil, text="???", text_font=("Helvetica",11,"bold"))
        label8.grid(row=8,column=1,padx=5)

        # labelDummy = customtkinter.CTkLabel(master=frameHasil, text=" ")
        # labelDummy.grid(row=0,column=2)

        btnExecute = customtkinter.CTkButton(master=self, text="Proceed Recognition", text_font=("Helvetica",14,"bold"), border_width=1, command=processRecognition)
        btnExecute.place(relx=0.62, rely=0.9)

        frameTest = customtkinter.CTkFrame(master=frameImage,corner_radius=10,fg_color="white")
        frameTest.pack(side="left",padx=30)

        frameHasilTest = customtkinter.CTkFrame(master=frameImage,corner_radius=10,fg_color="white")
        frameHasilTest.pack(side="right")

        labelTestImage = customtkinter.CTkLabel(master=frameTest,text="Test Image", text_font=("Helvetica",12,"bold"), text_color="black")
        labelTestImage.grid(column=0,row=0,)

        labelHasilTest = customtkinter.CTkLabel(master=frameHasilTest,text="Closest Result", text_font=("Helvetica",12,"bold"), text_color="black")
        labelHasilTest.grid(column=0,row=0)

        placeHolderTest = ImageTk.PhotoImage(Image.open("src/img/img_placeholder.jpg").resize((256,256)))
        label = tk.Label(frameTest, image = placeHolderTest)
        label.image = placeHolderTest
        label.grid(row=1,column=0)

        placeHolderRes = ImageTk.PhotoImage(Image.open("src/img/img_placeholder.jpg").resize((256,256)))
        label = tk.Label(frameHasilTest, image = placeHolderRes)
        label.image = placeHolderRes
        label.grid(row=1,column=0)


if __name__ == '__main__':
    app = App()
    app.resizable(False, False)
    app.mainloop()