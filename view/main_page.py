import tkinter as tk
from tkinter import ttk


class MainPage(ttk.Frame):
    def __init__(self,
                 parent: tk.Tk,
                 controller,
                 *args, **kwargs):

        self.parent = parent
        self.controller = controller
        super().__init__(
            self.parent,
            bootstyle="primary",
            *args, **kwargs
        )
        self.pack()

        self.label = ttk.Label(self, text="hello world!")
        self.label.pack()
