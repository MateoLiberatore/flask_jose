import sqlite3


db_file = 'clientes_pedidos.db'

conn = sqlite3.connect(db_file)
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clients (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT,
        phone TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Delivery (
        id INTEGER PRIMARY KEY,
        Client_id INTEGER,
        description TEXT,
        FOREIGN KEY (Client_id) REFERENCES Clients (id)
    )
''')


conn.commit()
conn.close()

print(f'Se ha creado la base de datos "{db_file}" con las tablas Clientes y Pedidos.')
