import tkinter as tk
from tkinter import ttk
import pyqrcode
import png

class App():
    def __init__(self):

        self.window = tk.Tk()
        self.window.title("QRCode")
        self.window.geometry("280x380")
        self.window.config(background= "#fef1ac")
        self.window.resizable(False,False)


    def create_qrcode(self):
        _name = self.name_entry.get()
        _url = self.url_entry.get()
        _scale = self.scale.get()
        _scale = int(_scale)

        qrcode_img = pyqrcode.create(_url)
        qrcode_img.png(f"{_name}",scale=_scale)

    def interface(self):

        # Label
        title_label = tk.Label(text="QRCode",background="#fef1ac",fg="#000000",font="Anton 17 bold")
        title_label.place(width=100,height=40,x=90,y=10)

        url_label = tk.Label(self.window,text="URL",background="#fef1ac",fg="#000000",font="Arial 13 bold")
        url_label.place(width=60,height=60,x=10,y=60)

        name_label = tk.Label(self.window,text="Name (.png)",background="#fef1ac",fg="#000000",font="Arial 13 bold")
        name_label.place(width=120,height=60,x=14,y=140)

        scala_label = tk.Label(self.window,text="Scale",background="#fef1ac",fg="#000000",font="Arial 13 bold")
        scala_label.place(width=90,height=60,x=0,y=220)

        scala_label_6 = tk.Label(self.window,text="6",background="#fef1ac",fg="#000000",font="Arial 13 bold")
        scala_label_6.place(width=20,height=15,x=17,y=270)

        scala_label_20 = tk.Label(self.window,text="20",background="#fef1ac",fg="#000000",font="Arial 13 bold")
        scala_label_20.place(width=20,height=15,x=152,y=270)

        # Entry

        self.url_entry = tk.Entry(self.window,background="#f3eec4",fg="#000000")
        self.url_entry.place(width=210,height=26,x=35,y=110)

        self.name_entry = tk.Entry(self.window,background="#f3eec4",fg="#000000")
        self.name_entry.place(width=210,height=26,x=35,y=190)

        # Scala

        self.scale = ttk.Scale(self.window,from_=6,to=20)
        self.scale.place(x=42,y=270)
     
        # Button

        button = tk.Button(self.window,text="Create",relief="flat",background="#5f9763",activebackground="#8dafbd",command= self.create_qrcode)
        button.place(width=75,height=30,x=102,y=315)

    def execute(self):
        self.interface()
        self.window.mainloop()

if __name__ == "__main__":
    app = App()
    app.execute()
