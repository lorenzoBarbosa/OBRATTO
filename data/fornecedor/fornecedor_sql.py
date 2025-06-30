CRIAR_TABELA_FORNECEDOR = """
CREATE TABLE IF NOT EXISTS fornecedor (
    id INTEGER PRIMARY KEY, 
    razao_social TEXT NOT NULL,
    FOREIGN KEY (id) REFERENCES usuario(id) 
);
"""

INSERIR_FORNECEDOR = """
INSERT INTO fornecedor (id, razao_social)
VALUES (?, ?);
"""

OBTER_FORNECEDOR = """
SELECT
    f.id,
    u.nome,
    u.email,
    u.senha,
    u.cpf_cnpj,
    u.telefone,
    u.data_cadastro,
    u.endereco,
    f.razao_social,
    u.tipo_usuario
FROM fornecedor f
JOIN usuario u ON f.id = u.id
ORDER BY u.nome;
"""

OBTER_FORNECEDOR_POR_ID = """
SELECT
    f.id,
    u.nome,
    u.email,
    u.senha,
    u.cpf_cnpj,
    u.telefone,
    u.data_cadastro,
    u.endereco,
    f.razao_social,
    u.tipo_usuario
FROM fornecedor f
JOIN usuario u ON f.id = u.id
WHERE f.id = ?;
"""

ATUALIZAR_FORNECEDOR = """
UPDATE fornecedor
SET razao_social = ?
WHERE id = ?;
"""

DELETAR_FORNECEDOR = """
DELETE FROM fornecedor
WHERE id = ?;
"""