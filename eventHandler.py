import tkinter as tk
from tkinter.constants import ANCHOR, CENTER


class EventHandler:

    def __init__(self, status: int):
        print("wget returned : "+str(status))
        self.report(status)

    def report(self, status: int):
        win = tk.Toplevel()
        win.wm_title("Report")
        win.config(height=100, width=230)
        win.minsize(230, 100)
        win.resizable(False, False)
        textToShow = self.checkStatusValue(status)

        l = tk.Label(win, text=textToShow)
        l.pack()

        b = tk.Button(win, text="Okay", command=win.destroy)
        b.pack()

    def checkStatusValue(self, status: int) -> str:
        if status == 0 or status == 2048:
            return "Completed!"
        elif status == 2:
            return "Aborted by user"
        elif status == 512 or status == 256:
            return "Check text fields"
        else:
            return "Generic error"
