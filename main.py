import tkinter as tk

from ttkbootstrap import Style

from controller import Controller

if __name__ == "__main__":

    # Initialize Tk GUI in main thread
    root = tk.Tk()
    style = Style(theme="simplex")  # https://ttkbootstrap.readthedocs.io/en/latest/themes.html

    # Configure root page properties
    # root.resizable(width=False, height=False)  # Don't allow resizing
    root.title("improved-fortnight")

    # Create controller object
    controller = Controller(root)

    # Start Tk GUI in main thread
    root.mainloop()
