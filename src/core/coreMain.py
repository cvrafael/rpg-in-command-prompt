import register.register as rr
import login.login as ll
register = rr.Register()
login = ll.Login()
class CoreMain():
    def __init__(self,):
        self._interface = "Bem vindo ao RPG - Reinado do Dragão!"
        self.options = ["1 - Cadastrar", "2 - Logar", "Escolha uma das opções: "]
    
    @property
    def layoutWelcome(self, ):
        print("/" * 64)
        print(" " * 10, self._interface)
        print("/" * 64)

    @property
    def menu(self,):
        for i in self.options:
            print(" " * 20, i)
        while True:
            try:
                option = int( input())

                if option == 1:
                    register.createAccount
                    break
                elif option == 2:
                    login.loginAccount
                    break
                else: 
                    print(f"{option} não é uma opção valida!")
                    continue
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")




            