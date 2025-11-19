import os
from controllers.characterControllers import CharacterControllers
from controllers.monstersControllers import MonstersController
class Character():
    def __init__(self):
        self.options = ["1-Caçar", "2-Mover", "3-Negociar"]
        self.cities = CharacterControllers().selectAllCities
        self.move = CharacterControllers().moveCharacter
        self.monsters = MonstersController().selectMonsters
        self.dic_monster = {}
        self.count = 1

    def menuInteractions(self, nick):
        for menu in self.options:
            print(f"{menu}")
        option = int(input(f"Pensando... \n"))
        if option == 1:
            self.huntMonsters(nick)
        elif option == 2:
            self.moveCharacter(nick)

    def huntMonsters(self, nick):
        monsters = self.monsters(nick)
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

        print(f"Qual monstro deseja lutar ?")

    def moveCharacter(self, nick):
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

