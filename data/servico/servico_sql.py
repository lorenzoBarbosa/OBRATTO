CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS servico(
id_servico INTEGER PRIMARY KEY AUTOINCREMENT,
id_prestador INTEGER NOT NULL,
titulo TEXT NOT NULL,
descricao TEXT NOT NULL, 
categoria TEXT NOT NULL,
valor_base REAL NOT NULL,
FOREIGN KEY (id_prestador) REFERENCES prestador(id)
);
"""

INSERIR = """
INSERT INTO servico (id_prestador, titulo, descricao, categoria, valor_base)
VALUES  (?, ?, ?, ?, ?);
"""

OBTER_TODOS = """
SELECT 
    s.id_servico,
    s.id_prestador,
    u.nome AS nome_prestador,
    s.titulo,
    s.descricao,
    s.categoria,
    s.valor_base
FROM servico s
JOIN prestador p ON s.id_prestador = p.id
JOIN usuario u ON p.id_usuario = u.id   
ORDER BY s.titulo
"""    

OBTER_POR_ID = """
SELECT 
   s.id_servico,
   s.id_prestador,
   u.nome AS nome_prestador,
   s.titulo,
   s.descricao,
   s.categoria,
   s.valor_base
FROM servico s
JOIN prestador p ON s.id_prestador = p.id
JOIN usuario u ON p.id_usuario = u.id
WHERE s.id_servico = ?;
"""

UPDATE = """
UPDATE servico
SET id_prestador = ?, titulo = ?, descricao = ?, categoria = ?, valor_base = ?
WHERE id_servico = ?;
"""

DELETE= """
DELETE FROM servico
WHERE id_servico = ?;
"""