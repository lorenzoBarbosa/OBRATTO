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


OBTER_TODOS_OS_ORCAMENTOS = """
SELECT * FROM orcamento
ORDER BY id
"""

OBTER_ORCAMENTO_POR_VALOR_ESTIMADO= """
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
WHERE o.valor_estimado = ?
ORDER BY o.id
"""

# FROM anuncio = representa que todas as características vem da tabela anuncio 
# JoIN fornecedor = representa que as características da tabela fornecedor serão unidas com a tabela anuncio
# JOIN apenas se relaciona por ID

OBTER_ORCAMENTO_POR_ID = """
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


OBTER_ANUNCIO_PAGINADO = """
SELECT
    a.id_anuncio,
    a.nome_anuncio,
    a.id_fornecedor,
    a.data_criacao,
    a.descricao,
    a.preco,
    f.nome AS nome_fornecedor
FROM anuncio a
JOIN fornecedor f ON a.id_fornecedor = f.id
ORDER BY a.id_anuncio
LIMIT ? OFFSET ?
"""

OBTER_ANUNCIO_POR_TERMO_PAGINADO = """
SELECT
    a.id_anuncio,
    a.nome_anuncio,
    a.id_fornecedor,
    a.data_criacao,
    a.descricao,
    a.preco,
    f.nome AS nome_fornecedor
FROM anuncio a
JOIN fornecedor f ON a.id_fornecedor = f.id
WHERE a.nome_anuncio LIKE ? or a.id_anuncio LIKE ? or f.nome LIKE ?
ORDER BY a.id_anuncio
LIMIT ? OFFSET ?
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



