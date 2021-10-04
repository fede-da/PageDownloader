class CommandBuilder:
    command: str = ""
    url: str = ""
    path: str = ""
    username: str = ""
    pwd: str = ""
    pdf: str = ""

    def __init__(self):
        self.command: str = "wget -r "
        self.url: str = ""
        self.path: str = ""
        self.username: str = ""
        self.pwd: str = ""
        self.pdf: str = ""

    def getUrl(self) -> str:
        return self.url

    def getPath(self) -> str:
        return self.path

    def getUsername(self) -> str:
        return self.username

    def getPwd(self) -> str:
        return self.pwd

    def getPdf(self) -> str:
        return self.pdf

    def setUrl(self, newUrl: str):
        self.url = newUrl

    def setPath(self, newPath: str):
        self.path = newPath

    def setUsername(self, newUsername: str):
        self.username = "--user=" + newUsername

    def setPwd(self, newPwd: str):
        self.pwd = "--password=" + newPwd

    def setPdf(self, toAdd: bool):
        ''' function() if condition : function2() ->
        if condition is true then function() else function2()
        '''
        self.pdf = " - A *pdf " if toAdd else self.pdf

    def returnCommand(self) -> str:
        return self.command + self.getPdf() + self.getUsername() + self.getPwd() + self.getUrl() + "-P" + self.getPath()

    def returnTestCommand(self) -> str:
        '''  Works on mac, not sure windows '''
        return " ls -la " + self.getPdf() + self.getUsername() + self.getPwd() + self.getUrl() + self.getPath()

    def printCommand(self):
        print(self.returnCommand())
