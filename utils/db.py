import sqlite3

def open_connection():
    conn = sqlite3.connect('banco_de_dados.db') 
    conn.row_factory = sqlite3.Row
    return conn
