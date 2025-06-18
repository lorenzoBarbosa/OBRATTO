CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS mensagem (
id_mensagem INTEGER PRIMARY KEY AUTOINCREMENT,
id_remetente INTEGER NOT NULL,
id_destinatario INTEGER NOT NULL,
conteudo TEXT NOT NULL,
data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (id_remetente) REFERENCES usuario(id),
FOREIGN KEY (id_destinatario) REFERENCES usuario(id)
);
"""

INSERIR = """
INSERT INTO mensagem (id_remetente, id_destinatario, conteudo, data_hora)
VALUES  (?, ?, ?, ?);
"""

OBTER_TODOS = """
SELECT 
    m.id_mensagem,
    remetente.nome AS nome_remetente,
    destinatario.nome AS nome_destinatario,
    m.conteudo,
    m.data_hora
FROM mensagem m
JOIN usuario remetente ON m.id_remetente = remetente.id
JOIN usuario destinatario ON m.id_destinatario = destinatario.id
ORDER BY m.data_hora DESC;
"""

OBTER_POR_ID = """
SELECT 
    m.id_mensagem,
    remetente.id AS id_remetente,
    destinatario.id AS id_destinatario,
    m.conteudo,
    m.data_hora
FROM mensagem m
JOIN usuario remetente ON m.id_remetente = remetente.id
JOIN usuario destinatario ON m.id_destinatario = destinatario.id
WHERE m.id_mensagem = ?;
"""

UPDATE = """
UPDATE mensagem
SET id_remetente = ?, id_destinatario = ?, conteudo = ?, data_hora = ?
WHERE id_mensagem = ?;
"""

DELETE= """
DELETE FROM mensagem
WHERE id_mensagem = ?;
"""