
import os
import platform
from tkinter import Entry, Label, Tk, messagebox
from tkinter import filedialog
from tkinter.constants import END
if platform.system() == "Darwin":
    from tkmacosx import Button
else:
    from tkinter import Button


class FirstLine:

    label: Label
    textField: Entry
    browseButton: Button

    def __init__(self, tk: Tk, w: int):
        self.textField = Entry(tk, width=w, bg='#dfdfdf', fg='black')
        self.label = Label(tk, text="Destination folder")
        self.browseButton = Button(
            tk, text="Browse files", bg='#156fcf', fg='white', command=self.browseFiles)

        self.textField.grid(row=1, column=1, sticky="ew")
        self.label.grid(row=1, column=0)
        self.browseButton.grid(row=1, column=2)
        return

    def browseFiles(self) -> None:
        self.textField.delete("0", END)
        path = filedialog.askdirectory(
            initialdir=os.path.normpath("~/"), title="Example")
        self.textField.insert("0", path)

    def getData(self) -> str:
        return self.textField.get()
