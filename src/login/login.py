import getpass
import os
import hashlib
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
            print(f"self.pássword: {len(self.password)}")
            hs = hashlib.sha256()
            hs.update(self.password.encode())
            print(f"hs.hexdigest(): {hs.hexdigest()}")
            validate = validate_login.validateLoginAccount(self.login, hs.hexdigest())
            print(f"validate: {validate}")
            if validate != []:
                if self.login == validate[0][0] and hs.hexdigest() == validate[0][1]:
                    print("Logado com sucesso!")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    account_infos = login_account_infos.getLoginAccountInfos(self.login)
                    validate_login.conn.close()
                    validate_login.cursor.close()
                    break
                else:
                    print("Usuario ou senha incorreto. Tente novamente.")
                    continue
            else: 
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Usuario ou senha incorreto. Tente novamente.")
                continue
        # Here will be the entrance to the game
        return in_game.interfaceLogged(account_infos)
        