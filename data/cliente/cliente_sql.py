CRIAR_TABELA_CLIENTE = """
CREATE TABLE IF NOT EXISTS cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    genero TEXT NOT NULL,
    data_nascimento TEXT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);
"""


INSERIR_CLIENTE = """
INSERT INTO cliente (id_usuario, genero, data_nascimento)
VALUES (?, ?, ?);
"""


OBTER_CLIENTE = """
SELECT 
    c.id,
    c.id_usuario
    u.nome,
    u.email,
    u.senha,
    u.cpf_cnpj,
    u.telefone,
    u.data_cadastro,
    u.endereco,
    c.genero,
    c.data_nascimento
FROM cliente c
JOIN usuario u ON c.id_usuario = u.id
ORDER BY u.nome;
"""


OBTER_CLIENTE_POR_ID = """
SELECT 
    c.id,
    c.id_usuario,
    u.nome,
    u.email,
    u.senha,
    u.cpf_cnpj,
    u.telefone,
    u.data_cadastro,
    u.endereco,
    c.genero,
    c.data_nascimento
FROM cliente c
JOIN usuario u ON c.id_usuario = u.id
WHERE c.id = ?;
"""

ATUALIZAR_CLIENTE = """
UPDATE cliente
SET id_usuario = ?, genero = ?, data_nascimento = ?
WHERE id = ?;
"""

DELETAR_CLIENTE = """
DELETE FROM cliente
WHERE id = ?;
"""
