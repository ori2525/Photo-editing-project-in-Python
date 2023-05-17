from tkinter import *
import cv2
from tkinter import filedialog


from sqlalchemy.sql.functions import dense_rank

from mouseEvent import image

class window:
    def __init__(self):
        self.wind=Tk()
        self.img=None
        self.wind.title("My photo editor")
        self.wind.configure(bg="white")


        self.btn1=Button(self.wind , text="Picture cutting",width=25,height=5,font="Broadway",bg="#EFEFEF")
        self.btn2 = Button(self.wind, text="Select a picture",width=25,height=5,font="Algerian",bg="#87CEFA",command=self.selectimage)
        self.btn3 = Button(self.wind, text="Add text",width=25,height=5,font="Broadway",bg="#EFEFEF")
        self.btn4 = Button(self.wind, text="Add a shape",width=25,height=5,font="Broadway",bg="#EFEFEF")
        self.btn5 = Button(self.wind, text="save",width=25,height=5,font="Algerian",bg="#B0E0E6")
        self.btn6 = Button(self.wind, text="exit",width=25,height=5,font="Algerian",bg="#B0E0E6",command=self.exitt)
        self.btn7 = Button(self.wind, text="monochromatic", width=25, height=5, font="Broadway", bg="#EFEFEF")
        self.entry=Entry(self.wind)

        self.position()

        self.wind.mainloop()
    def position(self):
        self.btn2.grid(row=0,column=0,pady=10,columnspan=2, sticky="NSEW")
        self.btn1.grid(row=1, column=0, sticky="NSEW")
        self.btn3.grid(row=1, column=1,sticky="NSEW")
        self.btn4.grid(row=2, column=0, sticky="NSEW")
        self.btn5.grid(row=3, column=0,pady=10,sticky="NSEW")
        self.btn6.grid(row=3, column=1,pady=10, sticky="NSEW")
        self.btn7.grid(row=2, column=1,sticky="NSEW")

    def selectimage(self):
        file_name=filedialog.askopenfilename()
        self.img=image(file_name)
        self.events()
    def events(self):
        self.btn4.bind("<Button-1>",self.img.send)
        self.btn3.bind("<Button-1>",self.img.add_text_action)
        self.btn5.bind("<Button-1>",self.img.save)
        self.btn1.bind("<Button-1>",self.img.cut)
        self.btn7.bind("<Button-1>",self.img.chanecolor)

    def exitt(self):
        self.wind.destroy()

w=window()
