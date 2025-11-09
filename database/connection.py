import psycopg2
from psycopg2 import Error
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
            row = cur.fetchall()
            if row[0][0] == True: 
                return conn
            else:
                print("Don't was possivel connect to the database.")
        except Error as e:
            print(f"Don't was possible connect to the database.{e}")
            conn.rollback()
    def authentic(self):
        pass