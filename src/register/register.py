
import getpass
import hashlib
import login.login as ll
import controllers.accountControllers as ca
hs = hashlib.sha256()
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

    def securyPassword(self, password):
        hs.update(password.encode(encoding="utf-8", errors="strict"))
        return hs.hexdigest()

    @property
    def createAccountDatas(self):
        self.name = input("Nome: ")
        while True:
            self.email = input("E-mail: ")
            validate_email = create.validateEmailAccount(self.email)
            if validate_email[0][0] == 1:
                print("Este email já existe!") 
                continue
            else:
                break
        self.cpf = input("CPF: ")
        while True:
            self.login = input("login: ")
            validate_login = create.validateLogin(self.login)
            if validate_login[0][0] == 1:
                print("Este login já existe!") 
                continue
            else:
                break  
        self.password = getpass.getpass("Senha: ")
        encrypt_pasword = self.securyPassword(self.password)
        self.confirm_password = getpass.getpass("Confirme-senha: ")
        self.secret_key = input("Chave secreta: ")
        create.createAccount(self.name, self.email, self.cpf )
        id_user = select.selectAccount(self.email)
        create.createLoginAccount(self.login, encrypt_pasword, self.secret_key, id_user)
        return logging.loginAccount
    
 
