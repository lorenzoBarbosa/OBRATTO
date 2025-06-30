CRIAR_TABELA_PRESTADOR = """
CREATE TABLE IF NOT EXISTS prestador (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL UNIQUE,
    area_atuacao TEXT NOT NULL,
    tipo_pessoa TEXT NOT NULL,
    razao_social TEXT,
    descricao_servicos TEXT,
    FOREIGN KEY(id_usuario) REFERENCES usuario(id) ON DELETE CASCADE
);
"""

INSERIR_PRESTADOR = """
INSERT INTO prestador (id_usuario, area_atuacao, tipo_pessoa, razao_social, descricao_servicos)
VALUES (?, ?, ?, ?, ?);
"""


OBTER_PRESTADOR = """
SELECT 
    p.id,
    u.nome,
    u.email,
    u.senha,
    u.cpf_cnpj,
    u.telefone,
    u.data_cadastro,
    u.endereco,
    p.area_atuacao,
    p.tipo_pessoa,
    p.razao_social,
    p.descricao_servicos
FROM prestador p
JOIN usuario u ON p.id = u.id
ORDER BY u.nome;
"""


OBTER_PRESTADOR = """
SELECT
    u.id AS id_usuario,
    u.nome,
    u.email,
    u.telefone,
    p.area_atuacao,
    p.tipo_pessoa,
    p.razao_social,
    p.descricao_servicos
FROM prestador p
JOIN usuario u ON p.id_usuario = u.id
ORDER BY u.nome;
"""


ATUALIZAR_PRESTADOR = """
UPDATE prestador
SET area_atuacao = ?,
    tipo_pessoa = ?,
    razao_social = ?,
    descricao_servicos = ?
WHERE id = ?;
"""


DELETAR_PRESTADOR = """
DELETE FROM prestador
WHERE id = ?;
"""
