CRIAR_TABELA_PRESTADOR = """
CREATE TABLE IF NOT EXISTS prestador (
    id INTEGER PRIMARY KEY,
    area_atuacao TEXT NOT NULL,
    tipo_pessoa TEXT NOT NULL,
    razao_social TEXT,
    descricao_servicos TEXT,
    FOREIGN KEY (id) REFERENCES usuario(id)
);
"""

# SQL para inserir um novo registro na tabela 'prestador'.
# O ID é fornecido pela inserção prévia na tabela 'usuario'.
INSERIR_PRESTADOR = """
INSERT INTO prestador (id, area_atuacao, tipo_pessoa, razao_social, descricao_servicos)
VALUES (?, ?, ?, ?, ?);
"""

# SQL para obter todos os prestadores, juntando com os dados da tabela 'usuario'.
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
    p.descricao_servicos,
    u.tipo_usuario
FROM prestador p
JOIN usuario u ON p.id = u.id
ORDER BY u.nome;
"""

# SQL para obter um prestador específico pelo seu ID, juntando com os dados da tabela 'usuario'.
# A coluna 'p.id_usuario' foi removida pois o join é feito pelo próprio 'id'.
OBTER_PRESTADOR_POR_ID = """
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
    p.descricao_servicos,
    u.tipo_usuario
FROM prestador p
JOIN usuario u ON p.id = u.id
WHERE p.id = ?;
"""

# SQL para atualizar os dados específicos de um prestador.
ATUALIZAR_PRESTADOR = """
UPDATE prestador
SET area_atuacao = ?, tipo_pessoa = ?, razao_social = ?, descricao_servicos = ?
WHERE id = ?;
"""

# SQL para deletar um prestador. A deleção na tabela 'usuario' deve ser tratada em cascata ou separadamente.
DELETAR_PRESTADOR = """
DELETE FROM prestador WHERE id = ?;
"""