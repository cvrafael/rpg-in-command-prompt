import getpass
class Login:
    def __init__(self,):
        self.LOGIN = "Entre com sua conta"
        self.login = ""
        self.password = ""

    @property
    def loginAccount(self):
        print("/" * 64)
        print(" " * 10, self.LOGIN)
        print("/" * 64)
        self.login = input("Usuário: ")
        self.password = getpass.getpass("Senha: ")
        return print("Você está logado.")