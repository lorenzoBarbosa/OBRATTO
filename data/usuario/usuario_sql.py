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

OBTER_USUARIO_POR_EMAIL = """
SELECT ID, nome, email, senha, cpf_cnpj, telefone, data_cadastro, endereco, tipo_usuario
FROM usuario
WHERE email = ?;
"""

OBTER_USUARIO_POR_ID = """
SELECT * FROM usuario WHERE id = ?;
"""

OBTER_USUARIO_POR_PAGINA = """
SELECT id, nome, email, cpf_cnpj, telefone, data_cadastro, endereco, tipo_usuario
FROM usuario
ORDER BY nome ASC
LIMIT ? OFFSET ?;
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
ATUALIZAR_TIPO_USUARIO = """
UPDATE usuario
SET tipo_usuario = ?
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
