import psycopg2
class ConnectionPostgreSQL():
    def __init__(self):
        pass

    @property
    def connectPostgress(self):

        conn = psycopg2.connect(database="rpg", 
                                user = "postgres", 
                                host = "172.18.0.2",
                                password = "catsarecool",
                                port = 5432)
        try:
            cur = conn.cursor()
            # Execute a command: create datacamp_courses table
            cur.execute("""SELECT 1=1;
                """)
            rows = cur.fetchall()
            # conn.close()
            for row in rows:
                if row: return conn
        except:
            print("Don't was possible connect to the database.")
    def authentic(self):
        pass