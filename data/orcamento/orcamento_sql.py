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
INSERT INTO orcamento (id_fornecedor, id_cliente, valor_estimado, data_solicitacao, prazo_entrega, status, descricao)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""


OBTER_ORCAMENTO_POR_ID = """
SELECT 
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



# FROM anuncio = representa que todas as características vem da tabela anuncio 
# JoIN fornecedor = representa que as características da tabela fornecedor serão unidas com a tabela anuncio
# JOIN apenas se relaciona por ID

OBTER_TODOS_ORCAMENTOS = """
SELECT
    o.id,
    o.valor_estimado,
    o.data_solicitacao,
    o.prazo_entrega,
    o.status,
    o.descricao,
    f.id AS id_fornecedor,
    c.id AS id_cliente
FROM orcamento o
JOIN fornecedor f ON o.id_fornecedor = f.id
JOIN cliente c ON o.id_cliente = c.id
WHERE o.id = ?
ORDER BY o.id
"""



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
WHERE id = ?
"""

DELETAR_ORCAMENTO = """
DELETE FROM orcamento
WHERE id = ?
"""



