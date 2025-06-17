CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS fornecedor (
id INTEGER PRIMARY KEY AUTOINCREMENT,
id_usuario INTEGER NOT NULL,
razao_social TEXT NOT NULL,
FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);
"""

INSERIR = """
INSERT INTO fornecedor (id_usuario, razao_social)
VALUES (?, ?);
"""

OBTER_TODOS = """
SELECT 
    f.id,
    u.nome,
    u.email,
    u.senha,
    u.cpf_cnpj,
    u.telefone,
    u.data_cadastro,
    u.endereco,
    u.cpf,
    f.razao_social
FROM fornecedor f
JOIN usuario u ON f.id_usuario = u.id
ORDER BY u.nome;
"""

OBTER_POR_ID = """
SELECT 
    f.id,
    u.nome,
    u.email,
    u.senha,
    u.cpf_cnpj,
    u.telefone,
    u.data_cadastro,
    u.endereco,
    u.cpf,
    f.razao_social
FROM fornecedor f
JOIN usuario u ON f.id_usuario = u.id
WHERE f.id = ?;
"""
UPDATE = """
UPDATE fornecedor
SET id_usuario = ?, razao_social = ?
WHERE id = ?;
"""

DELETE= """
DELETE FROM fornecedor
WHERE id = ?;
"""
