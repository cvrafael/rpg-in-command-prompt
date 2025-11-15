import controllers.accountControllers as ca
create = ca.ControllersAccount()
select = ca.ControllersAccount()

class Character():
    def __init__(self):
        self.id_login_account = ""
        self.nick_character = ""
        self.fk_id_cities = ""

    def createCharacter(self, nick_character, id_login_account, fk_id_cities):
        create.createCharacterAccount(nick_character, id_login_account, fk_id_cities)

    def selectCharacter(self, login):
        chars = select.selectCharacterAccount(login)
        return chars


