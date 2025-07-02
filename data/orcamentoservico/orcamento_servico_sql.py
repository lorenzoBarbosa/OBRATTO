CRIAR_TABELA_ORCAMENTO_SERVICO = """
CREATE TABLE IF NOT EXISTS orcamento_servico(
    id_orcamento INTEGER PRIMARY KEY AUTOINCREMENT,
    id_servico INTEGER NOT NULL,    
    id_prestador INTEGER NOT NULL,
    id_cliente INTEGER NOT NULL, 
    valor_estimado REAL NOT NULL,
    data_solicitacao DATE NOT NULL,
    prazo_entrega DATE NOT NULL,
    status TEXT NOT NULL,
    descricao TEXT NOT NULL,
    FOREIGN KEY (id_servico) REFERENCES servico(id_servico),
    FOREIGN KEY (id_prestador) REFERENCES prestador(id),
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_usuario)
);
"""

INSERIR_ORCAMENTO_SERVICO= """
INSERT INTO orcamento_servico (id_servico, id_prestador, id_cliente, valor_estimado, data_solicitacao, prazo_entrega, status, descricao)
VALUES  (?, ?, ?, ?, ?, ?, ?, ?);
"""

OBTER_ORCAMENTO_SERVICO = """
SELECT 
    o.id_orcamento,
    o.id_servico,
    o.id_prestador,
    o.id_cliente,
    o.valor_estimado,
    o.data_solicitacao,
    o.prazo_entrega,
    o.status,
    o.descricao,
    u_prestador.nome AS nome_prestador,
    u_cliente.nome AS nome_cliente,
    s.titulo AS titulo_servico
FROM orcamento_servico o
JOIN prestador p ON o.id_prestador = p.id
JOIN usuario u_prestador ON p.id = u_prestador.id
JOIN cliente c ON o.id_cliente = c.id_usuario
JOIN usuario u_cliente ON c.id_usuario = u_cliente.id
JOIN servico s ON o.id_servico = s.id_servico
ORDER BY o.data_solicitacao DESC;
"""    

OBTER_ORCAMENTO_SERVICO_POR_ID = """
SELECT 
    o.id_orcamento,
    o.id_servico,
    o.id_prestador,
    o.id_cliente,
    o.valor_estimado,
    o.data_solicitacao,
    o.prazo_entrega,
    o.status,
    o.descricao,
    u_prestador.nome AS nome_prestador,
    u_cliente.nome AS nome_cliente,
    s.titulo AS titulo_servico
FROM orcamento_servico o
JOIN prestador p ON o.id_prestador = p.id
JOIN usuario u_prestador ON p.id = u_prestador.id
JOIN cliente c ON o.id_cliente = c.id_usuario
JOIN usuario u_cliente ON c.id_usuario = u_cliente.id
JOIN servico s ON o.id_servico = s.id_servico
WHERE o.id_orcamento = ?;
"""

OBTER_ORCAMENTO_SERVICO_POR_PAGINA = """
SELECT 
    os.*,
    u_prestador.nome AS nome_prestador,
    u_cliente.nome AS nome_cliente,
    s.titulo AS titulo_servico
FROM orcamento_servico os
JOIN usuario u_prestador ON os.id_prestador = u_prestador.id
JOIN usuario u_cliente ON os.id_cliente = u_cliente.id
JOIN servico s ON os.id_servico = s.id_servico
ORDER BY os.data_solicitacao DESC
LIMIT ? OFFSET ?;

"""

ATUALIZAR_ORCAMENTO_SERVICO = """
UPDATE orcamento_servico
SET id_servico = ?,
    id_prestador = ?,
    id_cliente = ?,
    valor_estimado = ?,
    data_solicitacao = ?,
    prazo_entrega = ?,
    status = ?,
    descricao = ?
WHERE id_orcamento = ?;
"""

DELETAR_ORCAMENTO_SERVICO = """
DELETE FROM orcamento_servico
WHERE id_orcamento = ?;
"""