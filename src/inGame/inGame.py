class InGame():
    def __init__(self):
        pass

    def interfaceLogged(self, datas):
        name, email, login, city = datas[0]
        print("/" * 32, f"Bem-Vindo, {name}", "/" * 32)
        print(" " * 32, f"Informações", " " * 32)
        print(" " * 32, f"email: {email}", " " * 32)
        print(" " * 32, f"login: {login}", " " * 32)
        print(" " * 32, f"Você está em: {city}", " " * 32)