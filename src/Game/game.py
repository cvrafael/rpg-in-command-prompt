import os
import controllers.characterControllers as cc
import controllers.accountControllers as ca
from character.character import Character
login_account_infos = ca.ControllersAccount()
ca_select = cc.CharacterControllers()
create = cc.CharacterControllers()
select = cc.CharacterControllers()
class Game():
    def __init__(self,):
        self.character = Character()

    def interfaceLogged(self, datas):
        id_login, name, email, login, nick, level, *_ = datas[0]
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
                        id_cities = ca_select.selectCities
                        create.createCharacterAccount(nick, id_login, id_cities[0][0])
                        self.windowLoggedWelcome(id_login, name, email, login, nick, level)
                        ca_select.conn.close()
                        ca_select.cursor.close()
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    chars = select.selectCharacterAccount(login)
                    print("/" * 32, f"Seus personagens", "/" * 32)
                    for char in chars:
                        info_character.update({ 
                               f"{count}": {
                                    "Name": char[0],
                                    "Level": char[1],
                                    "Strength": char[2], 
                                    "Defense": char[3], 
                                    "Health": char[4],
                                    "City": char[5]
                                }
                        })
                        print(" " * 32,f"{count}-{info_character[f"{count}"]["Name"]}")
                        count+=1

                    option = int(input("Escolhe seu personagem\n"))

                    if option > len(info_character):
                        print("Você não tem essa quantidade de personagens.")
                        continue
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"\
[{info_character[f"{option}"]["Name"]}]\n \
Level: {info_character[f"{option}"]["Level"]}\n \
Força: {info_character[f"{option}"]["Strength"]}\n \
Defesa: {info_character[f"{option}"]["Defense"]}\n \
Vida: {info_character[f"{option}"]["Health"]}\n \
Você está em: {info_character[f"{option}"]["City"]}\n \
                          ") 
                    
                    #Method to call menus. Caçar, Mover, Loja
                    self.character.menuInteractions(info_character[f"{option}"]["Name"]) 
                    self.characterMoved(login)                                  
            elif option == 2:
                nick = input("Nick do personagem: ")
                os.system('cls' if os.name == 'nt' else 'clear')
                create.createCharacterAccount(nick, id_login, id_cities[0][0])
                self.windowLoggedWelcome(id_login, name, email, login, nick, level)
                ca_select.conn.close()
                ca_select.cursor.close()

    def windowLoggedWelcome(self,id_login, name, email, login, nick, level):
        info_character = {}
        count = 1
        id_cities = ca_select.selectCities
        print("/" * 32, f"Bem-Vindo, {name}", "/" * 32)
        print(" " * 32, f"Informações", " " * 32)
        print(" " * 32, f"E-mail: {email}", " " * 32)
        print(" " * 32, f"Login: {login}", " " * 32)
        print(" " * 32, f"1 - Meus personagens", " " * 32)
        print(" " * 32, f"2 - Criar novo personagem", " " * 32)

        while True:
            option = int(input())
            if option == 1:
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
                nick = input("Nick do personagem: ")
                os.system('cls' if os.name == 'nt' else 'clear')
                create.createCharacterAccount(nick, id_login, id_cities[0][0])
                account_infos = login_account_infos.getLoginAccountInfos(login)
                self.interfaceLogged(account_infos)
                ca_select.conn.close()
                ca_select.cursor.close()

    def characterMoved(self, login_account):
        info_character = {}
        chars = select.selectCharacterAccount(login_account)
        os.system('cls' if os.name == 'nt' else 'clear')
        for char in chars:
            info_character.update({ 
                        "Nome": char[0],
                        "Level": char[1],
                        "Strength": char[2], 
                        "Defense": char[3], 
                        "Health": char[4],
                        "City": char[5]
            })
        print(f"\
[{info_character["Nome"]}]\n \
Level: {info_character["Level"]}\n \
Força: {info_character["Strength"]}\n \
Defesa: {info_character["Defense"]}\n \
Vida: {info_character["Health"]}\n \
Você está em: {info_character["City"]}\n \
                          ") 
        self.character.menuInteractions(info_character["Nome"])