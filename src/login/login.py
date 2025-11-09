import getpass
import controllers.accountControllers as ca
import inGame.inGame as ii

in_game = ii.InGame()
validate_login = ca.ControllersAccount()
login_account_infos = ca.ControllersAccount()

class Login():
    def __init__(self,):
        self.LOGIN = "Entre com sua conta"
        self.login = ""
        self.password = ""

    @property
    def loginAccount(self):
        while True:
            print("/" * 64)
            print(" " * 10, self.LOGIN)
            print("/" * 64)
            self.login = input("Usuário: ")
            self.password = getpass.getpass("Senha: ")
            validate = validate_login.validateLoginAccount(self.login, self.password)
            if validate:
                if self.login == validate[0][0] and self.password == validate[0][1]:
                    print("Logado com sucesso!")
                    account_infos = login_account_infos.getLoginAccountInfos(self.login)
                    print(f"{account_infos}")
                    break
                else:
                    print("Usuario ou senha incorreto. Tente novamente.")
                    continue
            else: 
                print("Usuario ou senha incorreto. Tente novamente.")
                continue
        # Here will be the entrance to the game
        return in_game.interfaceLogged(account_infos)
        