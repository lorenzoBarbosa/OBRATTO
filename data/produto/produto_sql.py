CRIAR_TABELA_PRODUTO = """
CREATE TABLE IF NOT EXISTS PRODUTO (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    descricao TEXT,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL
);
"""

INSERIR_PRODUTO = """
INSERT INTO PRODUTO (id, nome, descricao, preco, quantidade)
VALUES (?, ?, ?, ?, ?);
"""

OBTER_PRODUTO = """
SELECT id, nome, descricao, preco, quantidade
FROM PRODUTO
WHERE id = ?;
"""

OBTER_PRODUTO_POR_ID = """
SELECT * FROM PRODUTO 
WHERE id = ?;
"""

OBTER_PRODUTO_POR_PAGINA = """
SELECT * FROM PRODUTO
ORDER BY id
LIMIT ? OFFSET ?;
"""

ATUALIZAR_PRODUTO = """
UPDATE PRODUTO
SET nome = ?,
    descricao = ?,
    preco = ?,  
    quantidade = ?
WHERE id = ?;
"""

DELETAR_PRODUTO = """
DELETE FROM PRODUTO
WHERE id = ?;
"""
