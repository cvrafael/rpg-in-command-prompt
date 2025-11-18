import database.connection as dc
from psycopg2 import Error
cnct = dc.ConnectionPostgreSQL()

class ControllersAccount():
    def __init__(self,):
        self.conn = cnct.connectPostgress 
        self.cursor = self.conn.cursor()
        self.name = ""
        self.email = ""
        self.cpf = ""
    
    def selectAccount(self, email):
        try:
            self.cursor.execute(f"SELECT id FROM rpg.user_account WHERE email = '{email}';")
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
        finally:
            self.cursor.close()
            self.conn.close()
            return row
            
    def validateEmailAccount(self, email):

        try:
            self.cursor.execute(f"SELECT count(email) FROM rpg.user_account WHERE email = '{email}';")
            rows = self.cursor.fetchall()
            if rows:
                return rows
            return rows
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
        
    def validateLogin(self, login):
        try:
            self.cursor.execute(f"SELECT count(login) FROM rpg.login_account WHERE login = '{login}';")
            rows = self.cursor.fetchall()
            if rows:
                return rows
            return rows
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
    
    def createAccount(self, name, email, cpf):
        sql_insert_query = """
            INSERT INTO rpg.user_account (name, email, cpf)
            VALUES (%s, %s, %s)
        """
        try:
            self.cursor.execute(sql_insert_query, (name, email, cpf))
            self.conn.commit()
        except Error as e:
            print(f"Erro ao inserir dados: {e}")
            self.conn.rollback()
        finally:
            print("Conta cadastrada com sucesso!")

    def createLoginAccount(self, login, password, secret_key, id_user):
            sql_insert_query = """
                INSERT INTO rpg.login_account (login, password, secret_key, fk_id_user_account)
                VALUES (%s, %s, %s, %s)
            """
            try:
                self.cursor.execute(sql_insert_query, (login, password, secret_key, id_user))
                self.conn.commit()
            except Error as e:
                print(f"Erro ao inserir dados: {e}")
                self.conn.rollback()
            finally:
                self.cursor.close()
                self.conn.close()

    def createCharacterAccount(self, nick, id_login_account, fk_id_cities):
        print(f"createCharacterAccount: {fk_id_cities}")
        sql_insert_query = """
            INSERT INTO rpg.character (nick, fk_id_login_account, fk_id_cities)
            VALUES (%s, %s, %s)
        """
        try:
            self.cursor.execute(sql_insert_query, (nick, id_login_account, fk_id_cities))
            self.conn.commit()
        except Error as e:
            print(f"Erro ao inserir dados: {e}")
            self.conn.rollback()
        finally:
            self.cursor.close()
            self.conn.close()

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
            if rows:
                self.cursor.close()
                self.conn.close()
            return rows
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
            self.conn.rollback()

    def validateLoginAccount(self, login, password):
        sql_insert_query = f"""
            SELECT login, password FROM rpg.login_account WHERE login = '{login}' and password = '{password}'
        """
        try:
            self.cursor.execute(sql_insert_query)
            rows = self.cursor.fetchall()
            return rows

        except Error as e:
            print(f"Erro ao inserir dados: {e}")
            self.conn.rollback()

    def getLoginAccountInfos(self, login):
        sql_insert_query = f"""
            SELECT rl.id, ru.name, ru.email, rl.login, rc.nick, rc.level FROM rpg.user_account as ru
            INNER JOIN rpg.login_account as rl
            on ru.id = rl.fk_id_user_account
            LEFT JOIN rpg.character as rc
			on rc.fk_id_login_account = rl.id
            where rl.login = '{login}'
        """
        try:
            self.cursor.execute(sql_insert_query)
            rows = self.cursor.fetchall()
            if rows:
                self.cursor.close()
                self.conn.close()
            return rows

        except Error as e:
            print(f"Erro ao inserir dados: {e}")
            self.conn.rollback()
    
    @property
    def selectCities(self):
        try:
            self.cursor.execute(f"SELECT id FROM rpg.cities WHERE id = '1';")
            rows = self.cursor.fetchall()
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
        finally:
            self.cursor.close()
            self.conn.close()
            return rows