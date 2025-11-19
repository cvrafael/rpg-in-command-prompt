from database.connection import ConnectionPostgreSQL
from psycopg2 import Error

class MonstersController(ConnectionPostgreSQL):
    def __init__(self,):
        self.conn = ConnectionPostgreSQL().connectPostgress
        self.cursor = self.conn.cursor()

    def selectMonsters(self, nick):
        sql_select_query = f"""
            SELECT rm.monster, rm.strength, rm.defense, rm.health
				FROM rpg.character as rch		
				INNER JOIN rpg.login_account as rl
				on rch.fk_id_login_account = rl.id
                INNER JOIN rpg.cities as rc
                on rch.fk_id_cities = rc.id
				INNER JOIN rpg.monsters as rm	
				on rc.id = rm.fk_id_cities
                WHERE rch.nick = '{nick}'
        """
        try:
            self.cursor.execute(sql_select_query)
            rows = self.cursor.fetchall()
            if rows:
                self.cursor.close()
                self.conn.close()
            return rows
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
            self.conn.rollback()