import sqlite3

def open_connection():
    conn = sqlite3.connect('#')
    conn.row_factory = sqlite3.Row  # para acessar colunas como dicionário: row["id"], row["nome"], etc.
    return conn
