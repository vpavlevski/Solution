class EmailServerSettings:
    def __init__(self, server, port, username, password, retries):
        self.server = server
        self.port = port
        self.username = username
        self.password = password
        self.retries = retries

    @property
    def Server(self): return self.server

    @property
    def Port(self): return self.port

    @property
    def Username(self): return self.username

    @property
    def Password(self): return self.password

    @property
    def Retries(self): return self.retries

