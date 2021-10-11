import os
import platform
from tkinter.constants import END

from eventHandler import EventHandler
if platform.system() == "Darwin":
    from tkmacosx import Button
else:
    from tkinter import Button
from tkinter import Tk
from CommandBuilder import CommandBuilder

from FirstLine import FirstLine
from SecondLine import SecondLine
from auth.Auth import Auth
from flags import Flags


class Gui:
    tk: Tk
    fl: FirstLine
    sl: SecondLine
    auth: Auth
    cb: CommandBuilder
    flags: Flags
    download: Button

    def __init__(self):
        self.tk = Tk()
        self.defineSpecs()

        self.cb = CommandBuilder()
        self.fl = FirstLine(self.tk, 40)
        self.sl = SecondLine(self.tk, 40)
        self.auth = Auth(self.tk, 3, 0, 40)
        self.flags = Flags(self.tk, 6, 0)
        self.download = Button(self.tk, text="Download", bg='#156fcf', fg='white',
                               command=self.runCommand).grid(column=1, row=7)

    def run(self):
        self.tk.mainloop()

    def getCommands(self) -> list:
        return [
            self.fl.getData(),
            self.sl.getData(),
            self.auth.getValues()[0],
            self.auth.getValues()[1],
            self.flags.getValue(),
        ]

    def defineSpecs(self):
        self.tk.title("PageDownloader")
        self.tk.eval('tk::PlaceWindow . center')
        window_width = 700
        window_height = 220
        self.tk.minsize(window_width, window_height)
        self.tk.resizable(False, False)

    def printCommands(self):
        for elem in self.commands:
            print(elem)

    def runTestCommand(self):
        self.setCommands()
        self.printCommands()
        self.cb.setTestCommands(self.commands)
        self.cb.runTest()

    def runCommand(self):
        self.cb.setCommands(self.getCommands())
        EventHandler(self.cb.run())
