import os
try:
    from gui import Gui
except:
    os.system("cp -R tcl-tk /usr/local/Cellar/tcl-tk")
    from gui import Gui

myGui: Gui = Gui()
myGui.run()
