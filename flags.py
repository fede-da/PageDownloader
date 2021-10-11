from tkinter import Radiobutton, StringVar, Label, Tk


class Flags:
    b1: Radiobutton
    b2: Radiobutton
    v: StringVar

    def __init__(self, tk: Tk, r: int, c: int):
        Label(tk, text="Download").grid(row=r, column=c)
        self.v = StringVar(tk, "-r")
        modes = [
            ("This page", "EMPTY"),
            ("All pages", "-r")
        ]
        tmp_c: int = c+1
        for (k, value) in modes:
            Radiobutton(tk, text=k, value=value, variable=self.v).grid(
                row=r, column=tmp_c)
            tmp_c += 1

    def getValue(self) -> str:
        return "-r" if (self.v.get() == "-r") else ""
