
import os
from tkinter import Entry, Label, Button, Tk, messagebox
from tkinter import filedialog
from tkinter.constants import END


class FirstLine:

    label: Label
    textField: Entry
    browseButton: Button

    def __init__(self, tk: Tk, w: int):
        self.textField = Entry(tk, width=w)
        self.label = Label(tk, text="Dove vuoi scaricare i file?")
        self.browseButton = Button(
            tk, text="Browse files", command=self.browseFiles)

        self.textField.grid(row=1, column=1, sticky="ew")
        self.label.grid(row=1, column=0)
        self.browseButton.grid(row=1, column=2)
        return

    def leggiTesto(self):
        messagebox.showinfo(
            title="Hai scritto :", message=self.textField.get())
        self.textField.delete("0", END)

    def browseFiles(self) -> None:
        self.textField.delete("0", END)
        path = filedialog.askdirectory(
            initialdir=os.path.normpath("~/"), title="Example")
        self.textField.insert("0", path)

    def getData(self) -> str:
        return self.textField.get()
