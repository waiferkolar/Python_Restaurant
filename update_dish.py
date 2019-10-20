from tkinter import * 


class UpdateDish:
    def __init__(self,master,h):
        self.master = master 
        self.h = h
        self.setUpUi()

    def setUpUi(self):
        self.title_lable = Label(self.master,text="Update Dish Page").pack()