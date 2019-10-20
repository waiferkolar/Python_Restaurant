from tkinter import *


class TopMenu:
    def __init__(self, master,h, frames):
        self.master = master
        self.h = h
        self.frames = frames
        self.setUpUi()

    def setUpUi(self):
        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)

        self.dishMenu = Menu(self.menubar)

        self.dishMenu.add_command(
            label="All Dishes", command=lambda: self.h.raiseFrame(self.frames["show_dishes"]))
        self.dishMenu.add_command(
            label="Insert", command=lambda: self.h.raiseFrame(self.frames["insert_dishes"]))
        self.dishMenu.add_command(
            label="Update", command=lambda: self.h.raiseFrame(self.frames["update_dishes"]))

        self.menubar.add_cascade(label="Dishes", menu=self.dishMenu)
