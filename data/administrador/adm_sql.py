CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS administrador (
id INTEGER PRIMARY KEY AUTOINCREMENT, )
"""

INSERIR = """
INSERT INTO cliente (nome, email, senha, cpf_cnpj, telefone, data_cadastro, endereco, cpf) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

OBTER_TODOS = """
SELECT 
id, nome, email, senha, cpf_cnpj, telefone, data_cadastro, endereco, cpf
FROM usuario
ORDER BY nome
""" 