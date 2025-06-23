CRIAR_TABELA_USUARIO = """
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


INSERIR_USUARIO = """
INSERT INTO usuario (nome, email, senha, cpf_cnpj, telefone, data_cadastro, endereco) 
VALUES (?, ?, ?, ?, ?, ?, ?);
"""


OBTER_USUARIO = """
SELECT 
id, nome, email, senha, cpf_cnpj, telefone, data_cadastro, endereco
FROM usuario
ORDER BY nome
""" 


OBTER_USUARIO_POR_ID = """
SELECT * FROM usuario WHERE id = ?;
"""


ATUALIZAR_USUARIO = """
UPDATE usuario
SET nome = ?,
    email = ?,
    senha = ?,
    cpf_cnpj = ?,
    telefone = ?,
    data_cadastro = ?,
    endereco = ?
WHERE id = ?
"""


ATUALIZAR_SENHA_USUARIO = """
UPDATE usuario
SET senha = ?
WHERE id = ?
"""

DELETAR_USUARIO = """
DELETE FROM usuario
WHERE id = ?
"""
