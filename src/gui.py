import tkinter as tk

class ExampleView(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        title = tk.Label(self, text="Face Recognition", font=("Helvetica", 24))
        title.pack(side="top", fill="x", pady=10)

if __name__=='__main__':
    root = tk.Tk()
    view = ExampleView(root)
    view.pack(side="top", fill="both", expand=True)
    root.mainloop()

    