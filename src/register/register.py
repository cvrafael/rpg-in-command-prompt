
import getpass
import login.login as ll
import controllers.accountControllers as ca

create = ca.ControllersAccount()
select = ca.ControllersAccount()
logging = ll.Login()
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
    def createAccountDatas(self):
        self.name = input("Nome: ")
        self.email = input("E-mail: ")
        self.cpf = input("CPF: ")
        self.login = input("login: ")
        self.password = getpass.getpass("Senha: ")
        self.confirm_password = getpass.getpass("Confirme-senha: ")
        self.secret_key = input("Chave secreta: ")
        create.createAccount(self.name, self.email, self.cpf )
        id_user = select.selectAccount(self.email)
        create.createLoginAccount(self.login, self.password, self.secret_key, id_user)
        return logging.loginAccount
    
