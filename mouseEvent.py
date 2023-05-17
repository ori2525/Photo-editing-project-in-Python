from tkinter import END, filedialog, colorchooser
from tkinter.colorchooser import askcolor

import cv2
import imageio
import tkinter as tk
from PIL import Image, ImageTk
class image:
    def __init__(self,filePath):
        self.filePath = filePath
        self.image = imageio.imread(self.filePath)
        self.original_image = self.image.copy()
        self.start_point = 0
        self.end_point = 0
        self.cropping = False
        self.text_entry = None
        self.color = (255, 255, 255)
        self.display()

    def display(self):
        bgr_image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
        cv2.namedWindow("Image1")
        cv2.imshow('Image1', bgr_image)



    def draw_rect(self,event,x,y, flags, param):
        global ix,iy,draw
        if event==cv2.EVENT_LBUTTONDOWN:
            draw=True
            ix=x
            iy=y

        elif event == cv2.EVENT_LBUTTONUP:
           draw = False
           cv2.rectangle(self.image, (ix, iy), (x, y), (0,0,0))
           cv2.imshow("Image1", self.image)

        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            cv2.rectangle(self.image, (ix, iy), (x, y), (255, 255, 255))
            cv2.imshow("Image1", self.image)
    def send(self,event):
        ix=0
        iy=0
        draw=False
        cv2.imshow("Image1", self.image)
        cv2.setMouseCallback("Image1", self.draw_rect,param=draw)

    def add_text_action(self, event):
        top = tk.Tk()
        top.title("write your text")
        top.geometry('400x500')
        text = tk.Text(top)
        text.insert('0.0', "")
        text.insert(END, "")
        text.pack()
        button = tk.Button(top, text="Select color",width=30,height=5,bg="#B0E0E6", command=lambda: self.set_color(text))

        button.pack()
        cv2.imshow("Image1", self.image)
        cv2.setMouseCallback("Image1", self.add_text_to_picture, param=text)

    def set_color(self, text_widget):
        self.color = self.select_color()
        text_widget.focus()

    def select_color(self):
        color = askcolor()[0]
        return tuple(int(x) for x in color)

    def add_text_to_picture(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            words = param.get('0.0', END)
            cv2.putText(self.image, words, (x, y), cv2.FONT_ITALIC, 3, self.color, 5)
            cv2.imshow("Image1", self.image)
        elif event == cv2.EVENT_LBUTTONUP:
            cv2.setMouseCallback("Image1", lambda *args: None)

    # def add_text_action(self, event):
    #     top = tk.Tk()
    #     top.title("write your text")
    #     text = tk.Text(top)
    #     text.insert('0.0', "")
    #     text.insert(END, "")
    #     text.pack()
    #     button = tk.Button(top, text="Select color", command=self.select_color)
    #     button.pack()
    #
    #
    #     cv2.imshow("Image1", self.image)
    #     # cv2.setMouseCallback("Image1", self.add_text_to_picture, param=(text,self.select_color()))
    #
    # def select_color(self):
    #     color = askcolor()[0]
    #     return tuple(int(x) for x in color)
    #
    #
    #
    # def add_text_to_picture(self, event, x, y, flags, param):
    #     if event == cv2.EVENT_LBUTTONDOWN:
    #         # words = param.get('0.0', END)
    #         words = param[0].get('0.0', END)
    #         color = param[1]
    #         cv2.putText(self.image, words, (x, y), cv2.FONT_ITALIC, 3, color, 5)
    #
    #         # cv2.putText(self.image, words, (x, y), cv2.FONT_ITALIC, 3, param[1],5)
    #         cv2.imshow("Image1", self.image)
    #     elif event == cv2.EVENT_LBUTTONUP:
    #         cv2.setMouseCallback("Image1", lambda *args: None)

    # def open_text_window(self,event):
    #     window = tk.Tk()
    #     window.title("Enter Text")
    #     label = tk.Label(window, text="Enter Text:")
    #     label.pack()
    #     entry = tk.Entry(window)
    #     entry.pack()
    #     button = tk.Button(window, text="Add Text", command=lambda: self.add_text_to_image(entry.get()))
    #     button.pack()
    #     window.mainloop()

    def save(self,event):
        failpath1=filedialog.asksaveasfilename(defaultextension='.jpg')
        cv2.imwrite(failpath1,self.image)

    def cut(self, event):
        refPt = []
        cropping = False
        cv2.setMouseCallback('Image1', self.click_and_crop)
        pop = tk.Toplevel()
        pop.geometry("300x100")
        label = tk.Label(pop, text="גרור את העכבר על המקום ברצונך לחתוך")
        label.pack()
        pop.mainloop()

    # פונקציית הקלקה על החלון
    def click_and_crop(self, event, x, y, flags, param):
        global refPt, cropping
        # אם המשתמש לחץ על העכבר, החל תהליך חיתוך
        if event == cv2.EVENT_LBUTTONDOWN:
            refPt = [(x, y)]
            cropping = True
        # אם המשתמש שחרר את העכבר, השלם תהליך חיתוך
        elif event == cv2.EVENT_LBUTTONUP:
            refPt.append((x, y))
            cropping = False

            # עשיית חיתוך לפי הנקודות שהמשתמש בחר
            self.image = self.image[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]


            cv2.destroyWindow('Image1')
            # imageio.imwrite('cropped_example.jpg', cropped_img)
            # cv2.imshow("Image1", cropped_img)
            cv2.imshow("Image1", self.image)

    def chanecolor(self,event):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGRA2GRAY)
        cv2.imshow("Image1", self.image)












