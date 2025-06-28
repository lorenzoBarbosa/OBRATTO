import sqlite3
from contextlib import contextmanager
from datetime import datetime

def adapt_datetime_iso(val):
    """Adapta o objeto datetime do Python para o formato de texto ISO 8601."""
    return val.isoformat()

def convert_timestamp(val):
    """Converte a string de data/hora do banco de dados para um objeto datetime."""
    return datetime.fromisoformat(val.decode())

sqlite3.register_adapter(datetime, adapt_datetime_iso)
sqlite3.register_converter("timestamp", convert_timestamp)

DATABASE_FILE = "obratto.db"

@contextmanager
def open_connection():
    conn = sqlite3.connect(DATABASE_FILE, detect_types=sqlite3.PARSE_DECLTYPES)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()