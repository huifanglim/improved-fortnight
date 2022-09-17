import tkinter as tk

from ttkbootstrap import Style

if __name__ == "__main__":

    # Initialize Tk GUI in main thread
    root = tk.Tk()
    style = Style(theme="simplex")  # https://ttkbootstrap.readthedocs.io/en/latest/themes.html

    # Configure root page properties
    root.resizable(width=False, height=False)    # Don't allow resizing
    root.title("improved-fortnight")

    # Start Tk GUI in main thread
    root.mainloop()
