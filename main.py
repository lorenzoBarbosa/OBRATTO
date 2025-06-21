import sqlite3


sql_criar_tabela_usuario = """
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL,
    cpf_cnpj TEXT NOT NULL,
    telefone TEXT NOT NULL,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    endereco TEXT NOT NULL
);
"""

sql_inserir_usuario1 = """
INSERT INTO usuario (nome, email, senha, cpf_cnpj, telefone, data_cadastro, endereco) 
VALUES ("Clara", "clara@gmail.com", "123456", "123456789", "(xx)xxxxxxxxx", "2025-06-20", "ifes");
"""


sql_inserir_usuario2 = """
INSERT INTO usuario (nome, email, senha, cpf_cnpj, telefone, data_cadastro, endereco) 
VALUES ("Joaquim", "joaquim@email.com", "senhaForte123", "98765432100", "(11)91234-5678", "2025-06-21", "ifes");
"""

with sqlite3.connect('banco_de_dados.db') as conn:
    cursor = conn.cursor()
    cursor.execute(sql_criar_tabela_usuario)
    cursor.execute(sql_inserir_usuario1)
    cursor.execute(sql_inserir_usuario2)
    conn.commit()

    