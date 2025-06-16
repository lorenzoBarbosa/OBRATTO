CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS cliente (
id INTEGER PRIMARY KEY AUTOINCREMENT,
id_usuario INTEGER NOT NULL,
genero TEXT NOT NULL,
data_nascimento TEXT NOT NULL,
FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);
"""

INSERIR = """
INSERT INTO cliente (id_usuario, genero, data_nascimento)
VALUES (?, ?, ?);
"""

OBTER_TODOS = """
SELECT 
    c.id,
    u.nome,
    u.email,
    u.senha,
    u.cpf_cnpj,
    u.telefone,
    u.data_cadastro,
    u.endereco,
    u.cpf,
    c.genero,
    c.data_nascimento
FROM cliente c
JOIN usuario u ON c.id_usuario = u.id
ORDER BY u.nome;
"""

OBTER_POR_ID = """
SELECT 
    c.id,
    u.nome,
    u.email,
    u.senha,
    u.cpf_cnpj,
    u.telefone,
    u.data_cadastro,
    u.endereco,
    u.cpf,
    c.genero,
    c.data_nascimento
FROM cliente c
JOIN usuario u ON c.id_usuario = u.id
WHERE c.id = ?;
"""
UPDATE = """
UPDATE cliente
SET id_usuario = ?, genero = ?, data_nascimento = ?
WHERE id = ?;
"""

DELETE= """
DELETE FROM cliente
WHERE id = ?;
"""
