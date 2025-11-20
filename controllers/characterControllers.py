from database.connection import ConnectionPostgreSQL
from psycopg2 import Error

class CharacterControllers(ConnectionPostgreSQL):
    def __init__(self,):
        self.conn = ConnectionPostgreSQL().connectPostgress
        self.cursor = self.conn.cursor()

    def createCharacterAccount(self, nick, id_login_account, fk_id_cities):
        sql_insert_query = """
            INSERT INTO rpg.character (nick, fk_id_login_account, fk_id_cities)
            VALUES (%s, %s, %s)
        """
        try:
            self.cursor.execute(sql_insert_query, (nick, id_login_account, fk_id_cities))
            self.conn.commit()
        except Error as e:
            print(f"createCharacterAccount Erro ao inserir dados: {e}")
            self.conn.rollback()

    def selectCharacterAccount(self, login):
        sql_select_query = f"""
            SELECT rc.nick, rc.level, rc.strength, rc.defense, rc.health, rci.city FROM rpg.user_account as ru
            INNER JOIN rpg.login_account as rl
            on ru.id = rl.fk_id_user_account
			LEFT JOIN rpg.character as rc
			on rc.fk_id_login_account = rl.id
            INNER JOIN rpg.cities as rci
			on rc.fk_id_cities = rci.id
            where rl.login = '{login}'
        """
        try:
            self.cursor.execute(sql_select_query)
            rows = self.cursor.fetchall()
            return rows
        except Error as e:
            print(f"selectCharacterAccount Erro ao buscar dados: {e}")
            self.conn.rollback()

    def selectOneCharacterAccount(self, nick):
        sql_select_query = f"""
            SELECT rc.nick, rc.level, rc.strength, rc.defense, rc.health, rci.city FROM rpg.user_account as ru
            INNER JOIN rpg.login_account as rl
            on ru.id = rl.fk_id_user_account
			LEFT JOIN rpg.character as rc
			on rc.fk_id_login_account = rl.id
            INNER JOIN rpg.cities as rci
			on rc.fk_id_cities = rci.id
            where rc.nick = '{nick}'
        """
        try:
            self.cursor.execute(sql_select_query)
            rows = self.cursor.fetchall()
            return rows
        except Error as e:
            print(f"selectCharacterAccount Erro ao buscar dados: {e}")
            self.conn.rollback()
    
    @property
    def selectCities(self):
        try:
            self.cursor.execute(f"SELECT id FROM rpg.cities WHERE id = '1';")
            rows = self.cursor.fetchall()
        except Error as e:
            print(f"selectCities Erro ao buscar dados: {e}")
        finally:
            return rows
        
    @property
    def selectAllCities(self):
        try:
            self.cursor.execute(f"SELECT * FROM rpg.cities ORDER BY id ASC;")
            rows = self.cursor.fetchall()
        except Error as e:
            print(f"selectAllCities Erro ao buscar dados: {e}")
        finally:
            return rows
        
    def moveCharacterInTheCity(self, id_city, nick):
        sql_update_query = f"""
            UPDATE rpg."character"
            SET  fk_id_cities = '{id_city}'
            WHERE nick = '{nick}';
        """
        try:
            self.cursor.execute(sql_update_query)
            self.conn.commit()
        except Error as e:
            print(f"moveCharacter Erro ao inserir dados: {e}")
            self.conn.rollback()