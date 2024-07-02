import sqlite3

# Nombre del archivo de la base de datos SQLite
db_file = 'clientes_pedidos.db'

# Conectar a la base de datos (creará el archivo si no existe)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Crear la tabla Clientes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clients (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT,
        phone TEXT
    )
''')

# Crear la tabla Pedidos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Delivery (
        id INTEGER PRIMARY KEY,
        Client_id INTEGER,
        description TEXT,
        FOREIGN KEY (Client_id) REFERENCES Clients (id)
    )
''')

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print(f'Se ha creado la base de datos "{db_file}" con las tablas Clientes y Pedidos.')
