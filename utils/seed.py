from data.administrador.administrador_repo import criar_tabela_administrador
from data.fornecedor.fornecedor_repo import criar_tabela_fornecedor
from data.prestador.prestador_repo import criar_tabela_prestador
from data.usuario.usuario_repo import criar_tabela_usuario

def criar_tabelas():
    criar_tabela_usuario()
    criar_tabela_administrador()
    criar_tabela_prestador()
    criar_tabela_fornecedor()