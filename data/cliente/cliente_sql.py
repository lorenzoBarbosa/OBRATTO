CRIAR_TABELA_CLIENTE = """
CREATE TABLE IF NOT EXISTS cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL UNIQUE,
    genero TEXT,
    data_nascimento DATE,
    FOREIGN KEY(id_usuario) REFERENCES usuario(id) ON DELETE CASCADE
);
"""

INSERIR_CLIENTE = """
INSERT INTO cliente (id_usuario, genero, data_nascimento)
VALUES (?, ?, ?);
"""

OBTER_CLIENTE = """
SELECT
    u.id,
    u.nome,
    u.email,
    u.senha,
    u.cpf_cnpj,
    u.telefone,
    u.data_cadastro,
    u.endereco,
    u.tipo_usuario
FROM cliente c
JOIN usuario u ON c.id_usuario = u.id
ORDER BY u.nome;
"""


OBTER_CLIENTE_POR_ID = """
SELECT
    u.id,
    u.nome,
    u.email,
    u.senha,
    u.cpf_cnpj,
    u.telefone,
    u.data_cadastro,
    u.endereco,
    u.tipo_usuario
FROM cliente c
JOIN usuario u ON c.id_usuario = u.id -- CONDIÇÃO DE JOIN CORRIGIDA
WHERE c.id = ?; -- Busca pelo ID da tabela 'cliente'
"""

ATUALIZAR_CLIENTE = """
UPDATE cliente
SET genero = ?,
    data_nascimento = ?
WHERE id = ?;
"""

DELETAR_CLIENTE = """
DELETE FROM cliente
WHERE id = ?;
"""
