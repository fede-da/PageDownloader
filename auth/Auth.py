from auth.pwdLine import PwdLine
from auth.userLine import UserLine
from auth.enabler import Enabler
from tkinter import StringVar, Tk


class Auth:
    ul: UserLine
    pl: PwdLine
    en: Enabler

    def __init__(self, tk: Tk, row: int, col: int, w: int):
        self.ul = UserLine("disabled", tk, row+1, col, w)
        self.pl = PwdLine("disabled", tk, row+2, col, w)
        self.en = Enabler(tk, row, col, self.ul, self.pl)

    def getValues(self) -> list[str]:
        if self.en.getValue() == "disabled":
            return ["", ""]
        else:
            return [self.ul.getData(), self.pl.getData()]
