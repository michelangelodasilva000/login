import sqlite3

conn = sqlite3.connect('Dados.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Dados (
          id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          nome TEXT NOT NULL,
          email TEXT NOT NULL,
          senha TEXT NOT NULL
    )
""")

print('Conectado ao banco de dados')