import character.character as cc
import controllers.accountControllers as ca
ca_select = ca.ControllersAccount()
create = cc.Character()
select = cc.Character()
class InGame():
    def __init__(self):
        pass

    def interfaceLogged(self, datas):
        id_login, name, email, login, nick, level = datas[0]
        id_cities = ca_select.selectCities
        print(f"id_cities: {id_cities[0][0]}")
        print("/" * 32, f"Bem-Vindo, {name}", "/" * 32)
        print(" " * 32, f"Informações", " " * 32)
        print(" " * 32, f"E-mail: {email}", " " * 32)
        print(" " * 32, f"Login: {login}", " " * 32)
        print(" " * 32, f"1 - Meus personagens", " " * 32)
        print(" " * 32, f"2 - Criar novo personagem", " " * 32)

        while True:
            option = int(input())
            if option == 1:
                if nick == None:
                    print(f"Você ainda não tem um personagem. Deseja criar ?")
                    print("1 - Para sim.")
                    print("2 - Para não.")
                    option = int(input())
                    if option == 1:
                        nick = input("Nick do personagem")
                        create.createCharacter(nick, id_login, id_cities[0][0])
                else:
                    chars = select.selectCharacter(login)
                    print("/" * 32, f"Seus personagens", "/" * 32)
                    for char in chars:
                        print(" " * 32, f"{char[0]} - level {char[1]}", " " * 32)
            elif option == 2:
                nick = input("Nick do personagem")
                create.createCharacter(nick, id_login, id_cities[0][0])