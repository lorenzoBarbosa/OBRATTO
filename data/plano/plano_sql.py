CRIAR_TABELA_PLANO = """
CREATE TABLE IF NOT EXISTS plano(
    id_plano INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_plano TEXT NOT NULL,
    valor_mensal REAL NOT NULL,
    limite_servico INTEGER NOT NULL,
    tipo_plano TEXT NOT NULL,
    descricao TEXT NOT NULL
);
"""


INSERIR_PLANO = """
INSERT INTO plano (nome_plano, valor_mensal, limite_servico, tipo_plano, descricao)
VALUES (?, ?, ?, ?, ?)
"""

OBTER_TODOS_OS_PLANOS = """
SELECT * FROM plano 
ORDER BY id_plano
"""

OBTER_PLANO_POR_NOME = """         
SELECT
    p.id_plano,
    p.nome_plano,
    p.valor_mensal,
    p.limite_servico,
    p.tipo_plano,
    p.descricao
FROM plano p
WHERE p.nome_plano = ?
ORDER BY p.nome_plano
"""

OBTER_PLANO_POR_ID = """               
SELECT
    p.id_plano,
    p.nome_plano,
    p.valor_mensal,
    p.limite_servico,
    p.tipo_plano,
    p.descricao
FROM plano p
WHERE p.id_plano = ?
ORDER BY p.id_plano
"""



ATUALIZAR_PLANO_POR_NOME = """
UPDATE plano
SET 
    nome_plano = ?,
    valor_mensal = ?,
    limite_servico = ?,
    tipo_plano = ?,
    descricao = ?
WHERE id_plano = ?
"""

DELETAR_PLANO = """
DELETE FROM plano
WHERE id_plano = ?
"""
