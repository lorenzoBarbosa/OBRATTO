CRIAR_TABELA_ORCAMENTO = """
CREATE TABLE IF NOT EXISTS orcamento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_fornecedor INTEGER NOT NULL,
    id_cliente INTEGER NOT NULL,
    valor_estimado REAL,
    data_solicitacao DATETIME,
    prazo_entrega DATETIME,
    status TEXT,
    descricao TEXT,
    FOREIGN KEY (id_fornecedor) REFERENCES fornecedor(id),
    FOREIGN KEY (id_cliente) REFERENCES cliente(id)
);
"""

INSERIR_ORCAMENTO = """
INSERT INTO orcamento (
    id_fornecedor,
    id_cliente,
    valor_estimado,
    data_solicitacao,
    prazo_entrega,
    status,
    descricao
) VALUES (?, ?, ?, ?, ?, ?, ?);
"""

OBTER_ORCAMENTO_POR_ID = """
SELECT 
    id,
    id_fornecedor,
    id_cliente,
    valor_estimado,
    data_solicitacao,
    prazo_entrega,
    status,
    descricao
FROM orcamento
WHERE id = ?;
"""

OBTER_TODOS_ORCAMENTOS = """
SELECT
    id,
    id_fornecedor,
    id_cliente,
    valor_estimado,
    data_solicitacao,
    prazo_entrega,
    status,
    descricao
FROM orcamento
ORDER BY id;
"""

# ATUALIZAR_ORCAMENTO_POR_ID = """
# UPDATE orcamento
# SET
#     id_fornecedor = ?,
#     id_cliente = ?,
#     valor_estimado = ?,
#     data_solicitacao = ?,
#     prazo_entrega = ?,
#     status = ?,
#     descricao = ?
# WHERE id = ?;
# """

ATUALIZAR_ORCAMENTO_POR_ID = """
UPDATE orcamento
SET
    id_fornecedor = ?,
    id_cliente = ?,
    valor_estimado = ?,
    data_solicitacao = ?,
    prazo_entrega = ?,
    status = ?,
    descricao = ?
WHERE id = ?;
"""

DELETAR_ORCAMENTO = """
DELETE FROM orcamento
WHERE id = ?;
"""
