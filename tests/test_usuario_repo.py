import sys
import os
from data.usuario.usuario_repo import*
from data.usuario.usuario_model import Usuario

class TestUsuarioRepo:
    def test_criar_tabela_usuario(self, test_db):
        #Arrange
        #Act
        resultado = criar_tabela_usuario()
        #Assert
        assert resultado == True,"A criação da tabela deveria retornar True"

    def test_inserir_usuario(self, test_db):
        #Arrange
        criar_tabela_usuario()
        usuario_teste = Usuario(0,"Usuario Teste", "email", "senha", "12345678901", "99999999999", "2023-10-01 12:00:00", "Endereco Teste")
        #Act
        id_usuario_inserido = inserir_usuario(usuario_teste)
        #Assert
        usuario_db = obter_usuario_por_id(id_usuario_inserido)
        assert usuario_db is not None, "A categoria inserida não deveria ser None"
        assert usuario_db.id == 1, "O ID do usuário inserido deveria ser 1"
        assert usuario_db.nome == "Usuario Teste", "O nome do usuário inserido não confere"

    def test_atualizar_usuario(self, test_db):
        #Arrange
        criar_tabela_usuario()
        usuario_teste = Usuario(0,"Usuario Teste", "email", "senha", "12345678901", "99999999999", "2023-10-01 12:00:00", "Endereco Teste")
        id_usuario_inserido = inserir_usuario(usuario_teste)
        usuario_inserido = obter_usuario_por_id(id_usuario_inserido)
        #Act
        usuario_inserido.nome = "Usuario Atualizado"
        resultado = atualizar_usuario(usuario_inserido)
        #Assert
        assert resultado == True, "A alteração do usuário deveria retornar True"
        usuario_db = obter_usuario_por_id(id_usuario_inserido)
        assert usuario_db.nome == "Usuario Atualizado", "O nome do usuário alterado não confere"

    def test_atualizar_senha_usuario(self, test_db):
        # Arrange
        criar_tabela_usuario()
        usuario_teste = Usuario(0, "Usuario Teste", "email@example.com", "senha_antiga", "12345678901", "99999999999", "2023-10-01 12:00:00", "Endereco Teste")
        id_usuario_inserido = inserir_usuario(usuario_teste)
        # Act
        resultado = atualizar_senha_usuario(id_usuario_inserido, "141516")
        # Assert
        usuario_inserido = obter_usuario_por_id(id_usuario_inserido)
        assert resultado == True, "A atualização da senha deveria retornar True"
        usuario_db = obter_usuario_por_id(id_usuario_inserido)
        assert usuario_db.senha == nova_senha, "A senha do usuário não foi atualizada corretamente"

    def test_obter_usuario_por_pagina(self, test_db):
        # Arrange
        criar_tabela_usuario()
        for i in range(10):
            usuario = Usuario(0, f"Usuario Teste {i + 1}", f"email{i +1}@example.com", "senha", "12345678901", "99999999999", "2023-10-01 12:00:00", f"Endereco Teste {i + 1}")
            inserir_usuario(usuario)
        # Act
        usuarios_1 = obter_usuario_por_pagina(1, 10)  
        usuarios_2 = obter_usuario_por_pagina(2, 4)
        usuarios_3 = obter_usuario_por_pagina(3, 4)
        # Assert
        assert len(usuarios_1) == 10, "Deveria retornar 10 usuários na primeira página"
        assert len(usuarios_2) == 4, "Deveria retornar 4 usuários na segunda página"
        assert len(usuarios_3) == 2, "Deveria retornar 2 usuários na terceira página"
        assert usuario_3[0].id == 8, "O ID do primeiro usuário da terceira página do tamanho 4 deveria ser 8"



    def test_obter_usuario_por_id(self, test_db):
        # Arrange
        criar_tabela_usuario()
        usuario_teste = Usuario(0,"Usuario Teste", "email", "senha", "12345678901", "99999999999", "2023-10-01 12:00:00", "Endereco Teste")
        id_usuario_inserido = inserir_usuario(usuario_teste)
        # Act
        usuario_db = obter_usuario_por_id(id_usuario_inserido)
        # Assert
        assert usuario_db is not None, "O usuário obtido não deveria ser None"
        assert usuario_db.id == id_usuario_inserido, "O ID do usuário obtido não confere"
        assert usuario_db.nome == usuario_teste.nome, "O nome do usuário buscado deveria er igual ao nome do usuário inserido"

    def test_deletar_usuario(self, test_db):
        # Arrange
        criar_tabela_usuario()
        usuario_teste = Usuario(0, "Usuario Teste", "email@example.com", "12345678901", "99999999999", "2023-10-01 12:00:00", "Endereco Teste")
        id_usuario_inserido = inserir_usuario(usuario_teste)
        # Act
        resultado = deletar_usuario(id_usuario_inserido)
        # Assert
        assert resultado == True, "A exclusão do usuário deveria retornar True"
        usuario_deletado = obter_usuario_por_id(id_usuario_inserido)
        assert usuario_deletado is None, "O usuário deletado não deveria ser None"