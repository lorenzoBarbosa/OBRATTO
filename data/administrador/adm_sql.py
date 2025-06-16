CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS administrador (
id INTEGER PRIMARY KEY AUTOINCREMENT,
id_usuario INTEGER FOREIGN KEY REFERENCES usuario(id),
"""

INSERIR = """
INSERT INTO cliente (nome, email, senha, cpf_cnpj, telefone, data_cadastro, endereco, cpf) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

OBTER_TODOS = """
SELECT 
    a.id, 
    u.nome, 
    u.email, 
    u.senha, 
    u.cpf_cnpj, 
    u.telefone, 
    u.data_cadastro, 
    u.endereco, 
    u.cpf
FROM administrador a
JOIN usuario u ON a.id_usuario = u.id
ORDER BY u.nome
"""


UPDATE_ADMINISTRADOR = """
UPDATE administrador
SET id_usuario = ?
WHERE id = ?
"""
#OBTER_POR_ID = """



DELETE_ADMINISTRADOR = """
DELETE FROM administrador
WHERE id = ?
"""