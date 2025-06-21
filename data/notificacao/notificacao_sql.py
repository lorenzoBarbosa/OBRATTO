CRIAR_TABELA_NOTIFICACAO = """
CREATE TABLE IF NOT EXISTS notificacao (
    id_notificacao INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    mensagem TEXT NOT NULL,
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tipo_notificacao TEXT NOT NULL,
    vizualizar INTEGER DEFAULT 0,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);
"""


INSERIR_NOTIFICACAO = """
INSERT INTO notificacao (id_usuario, mensagem, data_hora, tipo_noficacao, vizualizar)
VALUES (?, ?, ?, ?, ?);
"""


OBTER_NOTIFICACAO = """
SELECT 
    n.id_notificacao,
    n.id_usuario,
    n.mensagem,
    n.data_hora,
    n.tipo_notificacao,
    n.vizualizar
FROM notificacao n
ORDER BY n.data_hora DESC;
"""


OBTER_NOTIFICACAO_POR_ID = """
SELECT 
    n.id_notificacao,
    n.id_usuario,
    n.mensagem,
    n.data_hora,
    n.tipo_notificacao,
    n.vizualizar
FROM notificacao n
WHERE n.id_notificacao = ?;
"""


ATUALIZAR_NOTIFICACAO = """
UPDATE notificacao
SET id_usuario = ?,
    mensagem = ?,
    data_hora = ?,
    tipo_notificacao = ?,
    vizualizar = ?
WHERE id_notificacao = ?;
"""


DELETAR_NOTIFICACAO = """
DELETE FROM notificacao
WHERE id_notificacao = ?;
"""
