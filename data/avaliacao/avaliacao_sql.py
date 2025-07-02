CRIAR_TABELA_AVALIACAO= """
CREATE TABLE IF NOT EXISTS avaliacao(
    id_avaliacao INTEGER PRIMARY KEY AUTOINCREMENT,
    id_avaliador INTEGER NOT NULL,
    id_avaliado INTEGER NOT NULL,
    nota  REAL NOT NULL,
    data_avaliacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    descricao TEXT NOT NULL,
    FOREIGN KEY (id_avaliador) REFERENCES cliente(id),      
    FOREIGN KEY (id_avaliado) REFERENCES prestador(id)
);
"""

INSERIR_AVALIACAO = """
INSERT INTO avaliacao (id_avaliador, id_avaliado, nota, data_avaliacao, descricao)
VALUES  (?, ?, ?, ?, ?);
""" 

OBTER_TODOS = """
SELECT
    a.id_avaliacao,
    a.id_avaliador,
    a.id_avaliado,
    a.nota,
    a.data_avaliacao,
    a.descricao,
    u1.nome AS nome_avaliador,
    u2.nome AS nome_avaliado
FROM avaliacao a
LEFT JOIN usuario u1 ON a.id_avaliador = u1.id
LEFT JOIN usuario u2 ON a.id_avaliado = u2.id

"""

OBTER_AVALIACAO_POR_ID = """
SELECT 
    av.id_avaliacao,
    av.id_avaliador,
    av.id_avaliado,
    av.nota,
    av.data_avaliacao,
    av.descricao
FROM avaliacao av
WHERE av.id_avaliacao = ?;
"""

OBTER_AVALIACAO_POR_PAGINA = """
SELECT * FROM avaliacao
ORDER BY id_avaliacao
LIMIT ? OFFSET ?;
"""

ATUALIZAR_AVALIACAO = """
UPDATE avaliacao
SET id_avaliador = ?,
    id_avaliado = ?, 
    nota = ?, 
    data_avaliacao = ?,
    descricao = ?
WHERE id_avaliacao = ?;
"""

DELETAR_AVALIACAO= """
DELETE FROM avaliacao
WHERE id_avaliacao = ?;
"""