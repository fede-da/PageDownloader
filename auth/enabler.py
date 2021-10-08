from tkinter import Radiobutton, StringVar, Tk, Label
from auth.pwdLine import PwdLine

from auth.userLine import UserLine


class Enabler:
    b1: Radiobutton
    b2: Radiobutton
    v: StringVar
    ul: UserLine
    pl: PwdLine

    def __init__(self, tk: Tk, r: int, c: int, userLine: UserLine, pwdLine: PwdLine):
        Label(tk, text=" username/email and password?").grid(row=r, column=c)
        self.ul = userLine
        self.pl = pwdLine
        self.v = StringVar(tk, "disabled")
        modes = [
            ("Yes", "normal"),
            ("No", "disabled")
        ]
        tmp_c: int = c+1
        for (k, value) in modes:
            Radiobutton(tk, text=k, value=value, variable=self.v,
                        command=self.changeValue).grid(row=r, column=tmp_c)
            tmp_c += 1

    def changeValue(self) -> None:
        newVal = self.v.get()
        print(newVal)
        self.ul.setChange(newVal)
        self.pl.setChange(newVal)

    def getValue(self) -> str:
        return self.v.get()
