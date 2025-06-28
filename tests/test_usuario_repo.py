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

    def test_obter_usuario_por_email(self, test_db):
            # Arrange
            criar_tabela_usuario()
            email_unico = "email_unico_para_teste@email.com"
            usuario_teste = Usuario(0, "Usuario Unico", email_unico, "senha", "11122233344", "77777777777", datetime.now(), "Endereco Unico")
            inserir_usuario(usuario_teste)
            # Act
            usuario_db = obter_usuario_por_email(email_unico)
            # Assert
            assert usuario_db is not None, "Deveria ter encontrado um usuário com o email especificado"
            assert usuario_db.email == email_unico

    def test_obter_usuario_por_id(self, test_db):
        # Arrange
        criar_tabela_usuario()
        email_unico = "id_test@email.com"
        usuario_original = Usuario(
            id=0,
            nome="Usuario ID Test",
            email=email_unico,
            senha="senha_id",
            cpf_cnpj="55544433322",
            telefone="11222334455",
            data_cadastro=datetime.now(),
            endereco="Endereco Teste ID"
        )
        id_inserido = inserir_usuario(usuario_original)
        # Act
        usuario_encontrado = obter_usuario_por_id(id_inserido)
        # Assert
        assert usuario_encontrado is not None, "A busca por ID não deveria retornar None"
        assert usuario_encontrado.id == id_inserido, "O ID do usuário encontrado não corresponde ao ID inserido"
        assert usuario_encontrado.email == email_unico, "O email do usuário encontrado não corresponde ao original"
        assert usuario_encontrado.nome == "Usuario ID Test", "O nome do usuário encontrado não corresponde ao original"

    def test_obter_usuarios_por_pagina(self, test_db):
        # Arrange
        criar_tabela_usuario()
        for i in range(15):
            usuario = Usuario(
                id=0,
                nome=f"Usuario Paginado {i}",
                email=f"paginado{i}@teste.com",
                senha="senha_paginada",
                cpf_cnpj=f"1111111111{i:02}",
                telefone="33444556677",
                data_cadastro=datetime.now(),
                endereco="Endereco Paginado"
            )
            inserir_usuario(usuario)
        usuarios_pagina_1 = obter_usuarios_por_pagina(pagina=1, limite=10)
        usuarios_pagina_2 = obter_usuarios_por_pagina(pagina=2, limite=10)
        usuarios_pagina_3 = obter_usuarios_por_pagina(pagina=3, limite=10)
        # Assert
        assert len(usuarios_pagina_1) == 10, "A primeira página deveria conter 10 usuários"
        assert len(usuarios_pagina_2) == 5, "A segunda página deveria conter os 5 usuários restantes"
        assert len(usuarios_pagina_3) == 0, "A terceira página não deveria conter nenhum usuário"
        # Opcional
        ids_pagina_1 = {u.id for u in usuarios_pagina_1}
        ids_pagina_2 = {u.id for u in usuarios_pagina_2}
        assert ids_pagina_1.isdisjoint(ids_pagina_2), "Os usuários da página 1 não devem se repetir na página 2"
