CRIAR_TABELA_ANUNCIO = """
CREATE TABLE IF NOT EXISTS anuncio(
    id_anuncio INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_anuncio TEXT NOT NULL,
    id_fornecedor INTEGER NOT NULL,
    data_criacao TEXT NOT NULL,
    descricao TEXT NOT NULL,
    preco REAL NOT NULL,
    FOREIGN KEY (id_fornecedor) REFERENCES fornecedor(id)
);
"""

INSERIR_ANUNCIO = """
INSERT INTO anuncio (nome_anuncio, id_fornecedor, data_criacao, descricao, preco)
VALUES (?, ?, ?, ?, ?)
"""

OBTER_TODOS_ANUNCIOS = """
SELECT * FROM anuncio
ORDER BY id_anuncio
"""

OBTER_ANUNCIO_POR_NOME = """
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
WHERE a.nome_anuncio = ?
ORDER BY a.id_anuncio
"""

# FROM anuncio = representa que todas as características vem da tabela anuncio 
# JoIN fornecedor = representa que as características da tabela fornecedor serão unidas com a tabela anuncio
# JOIN apenas se relaciona por ID

OBTER_ANUNCIO_POR_ID = """
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
WHERE a.id_anuncio = ?
ORDER BY a.id_anuncio
"""


ATUALIZAR_ANUNCIO_POR_NOME = """
UPDATE anuncio
SET nome_anuncio = ?,
    id_forncedor = ?,
    data_criacao = ?,
    descricao = ?,
    preco = ? 
WHERE nome_anuncio = ?
"""

DELETAR_ANUNCIO = """
DELETE FROM anuncio
WHERE id_anuncio = ?
"""



