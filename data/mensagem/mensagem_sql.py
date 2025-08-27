CRIAR_TABELA_MENSAGEM = """
CREATE TABLE IF NOT EXISTS mensagem (
    id_mensagem INTEGER PRIMARY KEY AUTOINCREMENT,
    id_remetente INTEGER,
    id_destinatario INTEGER,
    conteudo TEXT,
    data_hora TEXT,
    nome_remetente TEXT,
    nome_destinatario TEXT     
);
"""

INSERIR_MENSAGEM = """
INSERT INTO mensagem (
    id_remetente,
    id_destinatario,
    conteudo,
    data_hora,
    nome_remetente,
    nome_destinatario
) VALUES (?, ?, ?, ?, ?, ?)
"""


OBTER_MENSAGEM = """
SELECT 
    m.id_mensagem,
    m.id_remetente,
    m.id_destinatario,
    m.conteudo,
    m.data_hora,
    remetente.nome AS nome_remetente,
    destinatario.nome AS nome_destinatario
FROM mensagem m
JOIN usuario remetente ON m.id_remetente = remetente.id
JOIN usuario destinatario ON m.id_destinatario = destinatario.id
ORDER BY m.data_hora DESC;
"""

OBTER_MENSAGEM_POR_ID = """
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

OBTER_MENSAGEM_POR_PAGINA = """
SELECT * FROM mensagem
ORDER BY id_mensagem
LIMIT ? OFFSET ?;
"""

ATUALIZAR_MENSAGEM = """
UPDATE mensagem
SET id_remetente = ?,
    id_destinatario = ?,
    conteudo = ?,
    data_hora = ?
WHERE id_mensagem = ?;
"""

DELETAR_MENSAGEM = """
DELETE FROM mensagem
WHERE id_mensagem = ?;
"""