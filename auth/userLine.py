
import os
from tkinter import Entry, Label, Button, Tk, messagebox
from tkinter import filedialog
from tkinter.constants import END


class UserLine:

    label: Label
    textField: Entry
    isEnabled: str

    def __init__(self, value: str, tk: Tk, textRow: int, aCol: int, w: int):
        self.isEnabled = value
        self.textField = Entry(tk, width=w, state=value,
                               bg='#dfdfdf', fg='black')
        self.label = Label(tk, text="Username/email")

        self.textField.grid(row=textRow, column=aCol+1, sticky="ew")
        self.label.grid(row=textRow, column=aCol)
        return

    def getData(self) -> str:
        return self.textField.get()

    def setChange(self, newValue: str) -> None:
        self.textField.configure(state=newValue)
