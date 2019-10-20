from tkinter import *
from topmenu import *
from H import *
from insert_dishe import *
from update_dish import *
from show_dish import *

class App(H):
    def __init__(self,master):
        self.master = master
        self.frames = {}
        self.h = H()
        self.setUpUi()

    def setUpUi(self):
        self.frames["insert_dishes"] = Frame(self.master)
        self.frames["update_dishes"] = Frame(self.master)
        self.frames["show_dishes"] = Frame(self.master)

        TopMenu(self.master,self.h,self.frames)

        InsertDishes(self.frames["insert_dishes"],self.h)
        UpdateDish(self.frames["update_dishes"], self.h)
        ShowDishes(self.frames["show_dishes"], self.h)

        for frame in self.frames.values():
            frame.grid(row=0,column=0,sticky="news")

        self.h.raiseFrame(self.frames["show_dishes"])




root = Tk()
App(root)
root.geometry("500x300+200+200")
root.mainloop()
