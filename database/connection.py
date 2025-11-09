import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

class ConnectionPostgreSQL():
    def __init__(self):
        pass

    @property
    def connectPostgress(self):

        conn = psycopg2.connect(database=os.getenv('DATABASE'), 
                                user = os.getenv('USERNAME'), 
                                host = os.getenv('HOST'),
                                password = os.getenv('PASSWORD'),
                                port = os.getenv('PORT'))
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