from tkinter import *
import tkinter.messagebox


class InsertDishes:
    def __init__(self, master, h):
        self.master = master
        self.h = h
        self.setUpUi()

    def setUpUi(self):
        self.title_l = Label(self.master, text="Insert Dish")
        self.title_l.grid(row=0, columnspan=2)

        self.name_l = Label(self.master, text="Dish name")
        self.name_l.grid(row=1, column=0)

        self.name_e = Entry(self.master)
        self.name_e.grid(row=1, column=1)

        self.price_l = Label(self.master, text="Dish Price")
        self.price_l.grid(row=2, column=0)

        self.price_e = Entry(self.master)
        self.price_e.grid(row=2, column=1)

        self.addBtn = Button(self.master, text="Add", command=self.insertDish)
        self.addBtn.grid(row=3, column=1, sticky="e")

    def insertDish(self):
        name = self.name_e.get()
        price = self.price_e.get()
        # sql = """
        # CREATE TABLE IF NOT EXISTS dishes(
        #     id INTEGER PRIMARY KEY AUTOINCREMENT,
        #     name VARCHAR (100) NOT NULL,
        #     price INTEGER (6) NOT NULL
        # )
        # """
        # self.h.createTable(sql)
        self.h.insertNewDish(name,price)
