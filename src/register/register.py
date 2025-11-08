
import getpass
import login.login as login
logging = login.Login()
class Register():
    def __init__(self, ):
        self.name = ""
        self.name = ""
        self.email = ""
        self.cpf = ""
        self.login = ""
        self.password = ""
        self.confirm_password = ""
        self.secret_key = ""

    @property
    def createAccount(self):
        self.name = input("Nome: ")
        self.email = input("E-mail: ")
        self.cpf = input("CPF: ")
        self.login = input("login: ")
        self.password = getpass.getpass("Password: ")
        self.confirm_password = getpass.getpass("Confirm-password: ")
        self.secret_key = input("Secret key: ")
        print("Account created with succesfully!!")
        
        return logging.loginAccount
    
