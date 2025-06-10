CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS usuario (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
email TEXT NOT NULL,
senha TEXT NOT NULL,
cpf_cnpj TEXT NOT NULL,
telefone TEXT NOT NULL,
data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
endereco TEXT NOT NULL,
cpf TEXT NOT NULL)
"""

INSERIR = """
INSERT INTO cliente (nome, email, senha, cpf_cnpj, telefone, data_cadastro, endereco, cpf) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

OBTER_TODOS = """
SELECT 
id, nome, email, senha, cpf_cnpj, telefone, data_cadastro, endereco, cpf
FROM usuario
ORDER BY nome
""" 