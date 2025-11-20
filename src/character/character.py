import os
from controllers.characterControllers import CharacterControllers
from controllers.monstersControllers import MonstersController
from Fight.fight import Fight
class Character():
    def __init__(self):
        self.options = ["1-Caçar", "2-Mover", "3-Negociar"]
        self.cities = CharacterControllers().selectAllCities
        self.move = CharacterControllers().moveCharacterInTheCity
        self.select = CharacterControllers().selectCharacterAccount
        self.select_char = CharacterControllers().selectOneCharacterAccount
        self.monsters = MonstersController().selectMonsters
        self.fight = Fight().fighter
        self.dic_monster = {}
        self.count = 0

    def menuInteractions(self, nick, login):
        for menu in self.options:
            print(f"{menu}")
        option = int(input(f"Pensando... \n"))
        print(f"option: {option}")

        if option == 1:
            self.huntMonsters(nick, login)
        elif option == 2:
            self.moveCharacter(nick, login)

    def huntMonsters(self, nick, login):
        monsters = self.monsters(nick)
        char = self.select_char(nick)
        for monster in monsters:
            self.dic_monster.update({
                f"{self.count}":{
                "Name": monster[0],
                "Strength": monster[1],
                "Defense": monster[2],
                "Health": monster[3]
                }
            })
            print(f"{self.count}-{self.dic_monster[f"{self.count}"]["Name"]} - Força: {self.dic_monster[f"{self.count}"]["Strength"]} - Defesa: {self.dic_monster[f"{self.count}"]["Defense"]} - Vida: {self.dic_monster[f"{self.count}"]["Health"]}")
            self.count+=1

        option = int(input("Qual monstro deseja lutar ?"))
        try:
            self.fight(char[0], monsters[option])
        except KeyError:
            print(f"Digite um numero de monstro válido! ")
            self.menuInteractions(nick, login)


    def moveCharacter(self, nick, login):
        count = 0
        for city in self.cities:
            print(f"{city[0]} {city[1]}")
            count +=1
        option = int(input("Digite o número da cidade: "))
        if option > len(self.cities):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Digite um número de cidade valida!")
            self.menuInteractions(nick)
        else:
            self.move(option, nick)
            self.characterMoved(login)

    def characterMoved(self, login_account):

        info_character = {}

        chars = self.select(login_account)

        os.system('cls' if os.name == 'nt' else 'clear')

        for char in chars:

            info_character.update({ 
                        "Name": char[0],
                        "Level": char[1],
                        "Strength": char[2], 
                        "Defense": char[3], 
                        "Health": char[4],
                        "City": char[5]
            })

        print(f"[{info_character["Name"]}]") 
        print(f"Level: {info_character["Level"]}") 
        print(f"Força: {info_character["Strength"]}") 
        print(f"Defesa: {info_character["Defense"]}") 
        print(f"Vida: {info_character["Health"]}") 
        print(f"Você está em: {info_character["City"]}") 

        self.menuInteractions(info_character["Name"], login_account)
        self.characterMoved2(login_account)

    def characterMoved2(self, login_account):

        info_character = {}

        chars = self.select(login_account)

        os.system('cls' if os.name == 'nt' else 'clear')

        for char in chars:

            info_character.update({ 
                        "Name": char[0],
                        "Level": char[1],
                        "Strength": char[2], 
                        "Defense": char[3], 
                        "Health": char[4],
                        "City": char[5]
            })

        print(f"[{info_character["Name"]}]") 
        print(f"Level: {info_character["Level"]}") 
        print(f"Força: {info_character["Strength"]}") 
        print(f"Defesa: {info_character["Defense"]}") 
        print(f"Vida: {info_character["Health"]}") 
        print(f"Você está em: {info_character["City"]}\n") 

        self.menuInteractions(info_character["Name"], login_account)
        self.characterMoved(login_account)