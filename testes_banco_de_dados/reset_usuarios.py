from data.usuario import usuario_repo
from data.usuario.usuario_model import Usuario
from utils.security import criar_hash_senha
from datetime import datetime

# Apaga todos os usuários do banco de dados
def apagar_todos_usuarios():
    usuarios = usuario_repo.obter_usuarios_por_pagina(1, 1000)  # Ajuste o limite se necessário
    for usuario in usuarios:
        usuario_repo.deletar_usuario(usuario.id)
    print("Todos os usuários foram apagados.")

# Cria 2 usuários de cada tipo: Administrador, Fornecedor, Prestador, Cliente
def criar_usuarios_teste():
    tipos = ["Administrador", "Fornecedor", "Prestador", "Cliente"]
    for tipo in tipos:
        for i in range(1, 3):
            usuario = Usuario(
                id=None,
                nome=f"{tipo} Teste {i}",
                email=f"{tipo.lower()}{i}@teste.com",
                senha=criar_hash_senha(f"{tipo.lower()}123"),
                cpf_cnpj=f"0000000000{i}",
                telefone=f"(00) 00000-000{i}",
                endereco=f"Rua {tipo} {i}",
                tipo_usuario=tipo,
                data_cadastro=datetime.now()
            )
            usuario_repo.inserir_usuario(usuario)
    print("2 usuários de cada tipo criados com sucesso.")

if __name__ == "__main__":
    apagar_todos_usuarios()
    criar_usuarios_teste()
