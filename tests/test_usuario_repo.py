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