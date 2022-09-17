import tkinter as tk

from view.main_page import MainPage


# This is a controller
class Controller:
    def __init__(self,
                 root: tk.Tk):

        # Create tkinter container in root
        self.root = root
        self.container = tk.Frame(self.root)
        self.container.pack()

        self.main_page = MainPage(self.root, self)
