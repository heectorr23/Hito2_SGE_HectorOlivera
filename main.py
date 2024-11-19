import tkinter as tk
from tkinterdnd2 import TkinterDnD
from ui import AlcoholHealthApp

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = AlcoholHealthApp(root)
    root.mainloop()