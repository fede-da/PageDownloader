import os


class EventHandler:

    def __init__(self, s: int):
        print("Valore di ritorno della wget: "+str(s))
        self.showCompleted() if s == 0 or s == 2048 else self.showError()

    def showError(self):
        body_Str = "Errore durante esecuzione, ricontrolla i dati"

        title_Str = "Report :"

        os.system("osascript -e \'Tell application \"System Events\" to display dialog \"" +
                  body_Str+"\" with title \""+title_Str+"\"\'")

    def showCompleted(self):
        body_Str = "Nessun problema!"

        title_Str = "Download riuscito"

        os.system("osascript -e \'Tell application \"System Events\" to display dialog \"" +
                  body_Str+"\" with title \""+title_Str+"\"\'")
