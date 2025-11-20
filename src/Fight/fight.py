import random
import time
import os
class Fight:
    def __init__(self):
        pass

    def fighter(self, char, monster):
        dic_monster = {}
        dic_char = {}
        monster_name, strength_monster, defense_monster, health_monster = monster
        char_name, level, strength_char, defense_char, health_char, city = char

        print(monster_name, strength_monster, defense_monster, health_monster)
        print(char_name, level, strength_char, defense_char, health_char, city)

        dic_monster.update({
            "Name": monster_name,
            "Strength": strength_monster,
            "Defense": defense_monster,
            "Health": health_monster
        })

        dic_char.update({
            "Level": level,
            "Name": char_name,
            "Strength": strength_char,
            "Defense": defense_char,
            "Health": health_char
        })

        while True:

            numero_aleatorio = random.randint(1, 10)

            if numero_aleatorio == 10:
            
                print("Você entrou em combate!")
            
                if int(dic_char["Strength"]) >= int(dic_monster["Strength"]):
            
                    dic_monster["Health"] = int(dic_monster["Health"]) - 10
            
                    dic_monster.update({"Health": int(dic_monster["Health"])})

                    os.system('cls' if os.name == 'nt' else 'clear')
            
                    print(f"{dic_monster["Name"]} está com: {int(dic_monster["Health"])} de vida.")
            
                    if int(dic_monster["Health"]) <= 0:
                        print(f"Você matou {dic_monster["Name"]}")
                        break
            
                    time.sleep(0.8)
            
                    continue
            
            if numero_aleatorio == 2:
            
                dic_char["Health"] = int(dic_char["Health"]) - 5
        
                dic_char.update({"Health": int(dic_char["Health"])})

                os.system('cls' if os.name == 'nt' else 'clear')
        
                print(f"Você tomou 10 de dano. Sua vida está em: {int(dic_char["Health"])}")
            
                if int(dic_char["Health"]) <= 0:
                    print(f"Você morreu!")
                    break
            
                time.sleep(0.8)
        
                continue
                

