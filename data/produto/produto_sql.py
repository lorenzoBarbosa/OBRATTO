CRIAR_TABELA_PRODUTO = """
CREATE TABLE IF NOT EXISTs PRODUTO (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
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
OBTER_PRODUTO_POR_NOME = """
SELECT * FROM PRODUTO
WHERE nome LIKE ?;
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
