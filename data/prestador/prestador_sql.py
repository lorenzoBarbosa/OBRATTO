CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS prestador (
id INTEGER PRIMARY KEY AUTOINCREMENT,
id INTEGER NOT NULL,
area_atuacao TEXT NOT NULL,
tipo_pessoa TEXT NOT NULL, 
razao_social TEXT,
descricao_servicos TEXT,
FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);
"""

INSERIR = """
INSERT INTO prestador (id, area_atuacao, tipo_pessoa, razao_social, descricao_servicos)
VALUES (?, ?, ?, ?, ?);
"""

OBTER_TODOS = """
SELECT 
    p.id,
    u.nome,
    u.email,
    u.senha,
    u.cpf_cnpj,
    u.telefone,
    u.data_cadastro,
    u.endereco,
    u.cpf,
    p.area_atuacao,
    p.tipo_pessoa,
    p.razao_social,
    p.descricao_servicos
FROM prestador p
JOIN usuario u ON p.id = u.id
ORDER BY u.nome;
"""

OBTER_POR_ID = """
SELECT 
    p.id,
    u.nome,
    u.email,
    u.senha,
    u.cpf_cnpj,
    u.telefone,
    u.data_cadastro,
    u.endereco,
    u.cpf,
    p.area_atuacao,
    p.tipo_pessoa,
    p.razao_social,
    p.descricao_servicos
FROM prestador p
JOIN usuario u ON p.id = u.id
WHERE p.id = ?;
"""
UPDATE = """
UPDATE prestador
SET id = ?, area_atuacao = ?, tipo_pessoa = ?, razao_social = ?, descricao_servicos = ?
WHERE id = ?;
"""

DELETE= """
DELETE FROM prestador
WHERE id = ?;
"""
