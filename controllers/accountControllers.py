import database.connection as dc
from psycopg2 import Error

cnct = dc.ConnectionPostgreSQL()

class ControllersAccount:
    def __init__(self):
        self.conn = cnct.connectPostgress 
        self.cursor = self.conn.cursor()
        self.name = ""
        self.email = ""
        self.cpf = ""

    def selectAccount(self):
        try:
            self.cursor.execute("SELECT * FROM rpg.user_account;")
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
        finally:
            self.cursor.close()
            self.conn.close()

    def createAccount(self, name, email, cpf):
        sql_insert_query = """
            INSERT INTO rpg.user_account (name, email, cpf)
            VALUES (%s, %s, %s)
        """
        try:
            self.cursor.execute(sql_insert_query, (name, email, cpf))
            self.conn.commit()

            print(f"{self.cursor.rowcount} registro(s) inserido(s) com sucesso.")
        except Error as e:
            print(f"Erro ao inserir dados: {e}")
            self.conn.rollback()
        finally:
            self.cursor.close()
            self.conn.close()
            print("Conexão com o banco de dados encerrada.")
