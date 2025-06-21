CRIAR_TABELA_ADMINISTRADOR = """
CREATE TABLE IF NOT EXISTS administrador (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);
"""


INSERIR_ADMINISTRADOR = """
INSERT INTO administrador (id_usuario)                
VALUES (?)                                                                   
"""

OBTER_TODOS_ADMINISTRADORES = """     
SELECT 
    ad.id AS id,
    u.id AS id_usuario,
    u.nome AS nome,
    u.email AS email,
    u.senha AS senha,
    u.cpf_cnpj AS cpf_cnpj,
    u.telefone AS telefone,
    u.data_cadastro AS data_cadastro,
    u.endereco AS endereco,
    u.cpf AS cpf
FROM administrador ad
JOIN usuario u ON ad.id_usuario = u.id
ORDER BY u.nome;
"""

OBTER_ADMINISTRADOR_POR_ID = """                 
SELECT
    ad.id AS id,
    u.id AS id_usuario,
    u.nome AS nome,
    u.email AS email,
    u.senha AS senha,
    u.cpf_cnpj AS cpf_cnpj,
    u.telefone AS telefone,
    u.data_cadastro AS data_cadastro,
    u.endereco AS endereco,
    u.cpf AS cpf
FROM administrador ad
JOIN usuario u ON ad.id_usuario = u.id
WHERE ad.id = ?
ORDER BY ad.id;
"""


ATUALIZAR_ADMINISTRADOR = """
UPDATE administrador
SET id_usuario = ?
WHERE id = ?
"""

DELETAR_ADMINISTRADOR = """
DELETE FROM administrador
WHERE id = ?
"""