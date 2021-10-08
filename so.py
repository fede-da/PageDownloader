import tkinter as tk
from tkinter import messagebox
import os

ROOT = tk.Tk()
body_Str = "Body of Dialog"

title_Str = "Title"

os.system("osascript -e \'Tell application \"System Events\" to display dialog \"" +
          body_Str+"\" with title \""+title_Str+"\"\'")

ROOT.withdraw()
# the input dialog

# check it out

ROOT.mainloop()
