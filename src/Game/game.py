import os
import controllers.accountControllers as ca
import controllers.characterControllers as cc
ca_select = cc.CharacterControllers()
create = cc.CharacterControllers()
select = cc.CharacterControllers()
class Game():
    def __init__(self):
        pass

    def interfaceLogged(self, datas):
        id_login, name, email, login, nick, level = datas[0]
        id_cities = ca_select.selectCities
        info_character = {}
        count = 1
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
                        create.createCharacterAccount(nick, id_login, id_cities[0][0])
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    chars = select.selectCharacterAccount(login)
                    print("/" * 32, f"Seus personagens", "/" * 32)
                    print(" " * 32,f"Nome:")
                    for char in chars:
                        info_character.update({ 
                               f"{count}": {
                                    "Nome": char[0],
                                    "Level": char[1],
                                    "Strength": char[2], 
                                    "Defense": char[3], 
                                    "Health": char[4],
                                    "City": char[5]
                                }
                        })
                        print(" " * 32,f"{count}-{info_character[f"{count}"]["Nome"]}")
                        count+=1
                    option = int(input("Escolhe seu personagem\n"))
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"\
[{info_character[f"{option}"]["Nome"]}]\n \
Level: {info_character[f"{option}"]["Level"]}\n \
Força: {info_character[f"{option}"]["Strength"]}\n \
Defesa: {info_character[f"{option}"]["Defense"]}\n \
Vida: {info_character[f"{option}"]["Health"]}\n \
Você está em: {info_character[f"{option}"]["City"]}\n \
                          ")                                                
            elif option == 2:
                nick = input("Nick do personagem")
                create.createCharacterAccount(nick, id_login, id_cities[0][0]) 