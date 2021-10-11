
import os
from tkinter import Entry, Label, Button, Tk, messagebox
from tkinter import filedialog
from tkinter.constants import END


class SecondLine:

    label: Label
    textField: Entry

    def __init__(self, tk: Tk, w: int):
        self.textField = Entry(tk, width=w, bg='#dfdfdf', fg='black')
        self.label = Label(tk, text="Url:")

        self.textField.grid(row=2, column=1, sticky="ew")
        self.label.grid(row=2, column=0)
        return

    def getData(self) -> str:
        return self.textField.get()
