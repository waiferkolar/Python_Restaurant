from tkinter import *
import sqlite3
import tkinter.messagebox


class H:
    def __init__(self):
        self.conn = sqlite3.connect("restaurant.db")
        self.c = self.conn.cursor()

    def raiseFrame(self, frame):
        frame.tkraise()

    def createTable(self, sql):
        self.c.execute(sql)
        self.conn.commit()

    def insertNewDish(self, name, price):
        con = self.checkDishExist(name)
        if con : 
            tkinter.messagebox.showwarning("Be Careful","Dish with that name already exist!")
        else :
            sql = """INSERT INTO dishes (name,price) VALUES (?,?)"""
            self.c.execute(sql, (name, price))
            self.conn.commit()
            tkinter.messagebox.showinfo("Success", "New Dish created!")

    def checkDishExist(self, name):
        sql = """SELECT * FROM dishes WHERE name=?"""
        results =  self.c.execute(sql,[name])
        self.conn.commit()
        return len(results.fetchall()) > 0

