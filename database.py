# Database Management Banking
import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    user="root",
    password="root",
    database="bank"
)

cursor = mydb.cursor()


def db_query(str):
    cursor.execute(str)
    resultat = cursor.fetchall()
    return resultat


def createcustomertable():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers
    (username VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL,
    name VARCHAR(20) NOT NULL,
    age INTEGER NOT NULL,
    city VARCHAR(20) NOT NULL,
    balance INTEGER NOT NULL,
    account_number INTEGER NOT NULL,
    status BOOLEAN NOT NULL)
    ''')


mydb.commit()

if __name__ == "__main__":
    createcustomertable()
