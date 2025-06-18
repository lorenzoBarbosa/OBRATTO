CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS avaliacao(
id_avaliacao INTEGER PRIMARY KEY AUTOINCREMENT,
id_avaliador INTEGER NOT NULL,
id_avaliado INTEGER NOT NULL,
nota  REAL NOT NULL,
data_avaliacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
descricao TEXT NOT NULL,
FOREIGN KEY (id_avaliador) REFERENCES usuario(id),
FOREIGN KEY (id_avaliado) REFERENCES usuario(id)
);
"""

INSERIR = """
INSERT INTO avaliacao (id_avaliador, id_avaliado, nota, data_avaliacao, descricao)
VALUES  (?, ?, ?, ?, ?);
"""

OBTER_TODOS = """
SELECT 
    a.id_avaliacao,
    u_avaliador.nome AS nome_avaliador,
    u_avaliado.nome AS nome_avaliado,
    a.nota,
    a.descricao,
    a.data_avaliacao
FROM avaliacao a
JOIN cliente c_avaliador ON a.id_avaliador = c_avaliador.id
JOIN usuario u_avaliador ON c_avaliador.id_usuario = u_avaliador.id
JOIN prestador p_avaliado ON a.id_avaliado = p_avaliado.id
JOIN usuario u_avaliado ON p_avaliado.id_usuario = u_avaliado.id
ORDER BY a.data_avaliacao DESC;
"""    

OBTER_POR_ID = """
SELECT 
    a.id_avaliacao,
    u_avaliador.nome AS nome_avaliador,
    u_avaliado.nome AS nome_avaliado,
    a.nota,
    a.descricao,
    a.data_avaliacao
FROM avaliacao a
JOIN cliente c_avaliador ON a.id_avaliador = c_avaliador.id
JOIN usuario u_avaliador ON c_avaliador.id_usuario = u_avaliador.id
JOIN prestador p_avaliado ON a.id_avaliado = p_avaliado.id
JOIN usuario u_avaliado ON p_avaliado.id_usuario = u_avaliado.id
WHERE a.id_avaliacao = ?
"""

UPDATE = """
UPDATE avaliacao
SET id_avaliador = ?, id_avaliado = ?, nota = ?, data_avaliacao = ?, descricao = ?
WHERE id_avaliacao = ?;
"""

DELETE= """
DELETE FROM avaliacao
WHERE id_avaliacao = ?;
"""