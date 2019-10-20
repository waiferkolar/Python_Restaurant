from tkinter import *


class ShowDishes:
    def __init__(self, master, h):
        self.master = master
        self.h = h
        self.setUpUi()

    def setUpUi(self):
        self.title_lable = Label(self.master, text="Show Dishes").pack()
