from eventHandler import EventHandler
import os
os.environ['PATH'] = '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin' + \
    os.environ['PATH']
'''La riga sopra perchè py2app se ne frega delle variabili di ambiente'''


class CommandBuilder:
    command: str = ""
    url: str = ""
    path: str = ""
    username: str = ""
    pwd: str = ""
    pdf: str = ""
    flag: str = ""

    def __init__(self):
        self.command = "wget "
        self.url = ""
        self.path = ""
        self.username = ""
        self.pwd = ""
        self.pdf = ""
        self.flag = ""

    def getFlag(self) -> str:
        return self.flag+" "

    def getUrl(self) -> str:
        return self.url

    def getPath(self) -> str:
        return self.path

    def getUsername(self) -> str:
        if self.username == "":
            return ""
        else:
            return "--user=" + self.username + " "

    def getPwd(self) -> str:
        if self.pwd == "":
            return " "
        else:
            return "--password=" + self.pwd+" "

    def getPdf(self) -> str:
        return self.pdf

    def setFlag(self, f: str):
        self.flag = f

    def setUrl(self, newUrl: str):
        self.url = newUrl

    def setPath(self, newPath: str):
        self.path = newPath

    def setUsername(self, newUsername: str):
        self.username = newUsername

    def setPwd(self, newPwd: str):
        self.pwd = newPwd

    def setPdf(self, toAdd: str):
        ''' function() if condition : function2() ->
        if condition is true then function() else function2()
        '''
        self.pdf = toAdd

    def returnTestCommand(self) -> str:
        '''  Works on mac, not sure windows '''
        return " ls -la " + self.getPdf() + self.getUsername() + self.getPwd() + self.getUrl() + self.getPath()

    def setCommands(self, lista: list) -> None:
        self.setPath(lista[0])
        self.setUrl(lista[1])
        self.setUsername(lista[2])
        self.setPwd(lista[3])
        self.setFlag(lista[4])
        return None

    def returnCommand(self) -> str:
        return self.command + self.getFlag() + self.getUsername() + self.getPwd() + self.getUrl() + " -P " + self.getPath()

    def printCommand(self):
        print(self.returnCommand())

    def run(self):
        self.printCommand()
        EventHandler(os.system(self.returnCommand()))

    def setTestCommands(self, lista: list) -> None:
        self.setPath(lista[0])
        self.setUrl(lista[1])
        self.username = lista[2]
        self.pwd = lista[3]
        self.setPdf(lista[4])
        return None

    def runTest(self):
        string = self.getPath() + self.getUrl() + self.getPdf() + \
            self.getUsername() + self.getPwd()
        print(string)
        os.system(string)
