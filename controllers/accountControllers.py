import database.connection as dc
from psycopg2 import Error
cnct = dc.ConnectionPostgreSQL()

class ControllersAccount():
    def __init__(self, ):
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
                print("Conta cadastrada com sucesso!")

    def validateLoginAccount(self, login, password):
        sql_insert_query = f"""
            SELECT login, password FROM rpg.login_account WHERE login = '{login}' and password = '{password}'
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
            