CRIAR_TABELA_CLIENTE = """
CREATE TABLE IF NOT EXISTS cliente (
    id INTEGER PRIMARY KEY,
    genero TEXT NOT NULL,
    data_nascimento TEXT NOT NULL,
    FOREIGN KEY (id) REFERENCES usuario(id) ON DELETE CASCADE
);
"""

INSERIR_CLIENTE = """
INSERT INTO cliente (id, genero, data_nascimento)
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
    u.tipo_usuario,
    c.genero,
    c.data_nascimento
FROM cliente c
JOIN usuario u ON c.id = u.id
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
    u.tipo_usuario,
    c.genero,
    c.data_nascimento
FROM cliente c
JOIN usuario u ON c.id = u.id
WHERE c.id = ?;
"""
ATUALIZAR_CLIENTE = """
UPDATE cliente
SET genero = ?, data_nascimento = ?
WHERE id = ?;
"""
DELETAR_CLIENTE = """
DELETE FROM cliente
WHERE id = ?;
"""