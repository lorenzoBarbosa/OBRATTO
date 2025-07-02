import sqlite3
import pytest
from datetime import datetime
from data.mensagem.mensagem_repo import obter_mensagem_por_pagina
from data.mensagem.mensagem_model import Mensagem
from data.mensagem.mensagem_repo import (
    criar_tabela_mensagem,
    inserir_mensagem,
    obter_mensagem,
    obter_mensagem_por_id,
    atualizar_mensagem,
    deletar_mensagem
)
from data.usuario.usuario_repo import criar_tabela_usuario, inserir_usuario
from data.usuario.usuario_model import Usuario

class TestMensagemRepo:

    def test_criar_tabela_mensagem(self, test_db):
        # Arrange
        criar_tabela_usuario()
        # Act
        resultado = criar_tabela_mensagem()
        # Assert
        assert resultado is True, "A criação da tabela fornecedor deveria retornar True"

    def inserir_mensagem_para_teste(self):
        criar_tabela_usuario()
        criar_tabela_mensagem()
        mensagem = Mensagem(
            id_mensagem=0,
            id_remetente=1,
            id_destinatario=2,
            conteudo="Olá, tudo bem?",
            data_hora=datetime.now(),
            nome_remetente="Fulano",
            nome_destinatario="Ciclano"
        )
        return inserir_mensagem(mensagem)

    def test_inserir_mensagem(self, test_db):
        criar_tabela_usuario()
        criar_tabela_mensagem()

        mensagem = Mensagem(
            id_mensagem=0,
            id_remetente=1,
            id_destinatario=2,
            conteudo="Olá, tudo bem?",
            data_hora=datetime.now(),
            nome_remetente="Fulano",
            nome_destinatario="Ciclano"
        )

        id_mensagem = inserir_mensagem(mensagem)
        print(f"ID inserido: {id_mensagem}")

        mensagem_db = obter_mensagem_por_id(id_mensagem)
        print(f"Mensagem obtida do DB: {mensagem_db}")

        assert mensagem_db is not None

    def test_obter_mensagem(self, test_db):
        criar_tabela_usuario()
        criar_tabela_mensagem()
        id_mensagem = self.inserir_mensagem_para_teste()
        mensagem_db = obter_mensagem_por_id(id_mensagem)
        assert mensagem_db is not None

    def test_obter_mensagem_por_id(self,test_db):
        criar_tabela_usuario()
        criar_tabela_mensagem()
        #Arrange
        mensagem = Mensagem(
            id_mensagem=0,
            id_remetente=1,
            id_destinatario=2,
            conteudo="Mensagem específica",
            data_hora=datetime.now(),
            nome_remetente="José",
            nome_destinatario="Gabriel"
        )
        #Act
        id_mensagem = inserir_mensagem(mensagem)
        id_mensagem = inserir_mensagem(mensagem)
        print("ID inserido:", id_mensagem)
        mensagem_db = obter_mensagem_por_id(id_mensagem)
        #Assert
        assert mensagem_db is not None, "A mensagem obtida não deve ser None"
        assert mensagem_db.conteudo == "Mensagem específica", "O conteúdo da mensagem obtida não corresponde ao esperado"

    def test_obter_mensagem_por_pagina(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_mensagem()

        for i in range(15):
            mensagem = Mensagem(
                id_mensagem=0,
                id_remetente=1,
                id_destinatario=2,
                conteudo="Mensagem específica",
                data_hora=datetime.now(),
                nome_remetente="José",
                nome_destinatario="Gabriel"
            )
            inserir_mensagem(mensagem)
        with sqlite3.connect(test_db) as conn:
            mensagem_pagina_1 = obter_mensagem_por_pagina(conn, limit=10, offset=0)
            mensagem_pagina_2 = obter_mensagem_por_pagina(conn,limit=10,offset=10)
            mensagem_pagina_3 = obter_mensagem_por_pagina(conn,limit=10, offset=20)
        # Assert
        assert len(mensagem_pagina_1) == 10, "A primeira página deveria conter 10 mensagens"
        assert len(mensagem_pagina_2) == 5, "A segunda página deveria conter os 5 mensagens restantes"
        assert len(mensagem_pagina_3) == 0, "A terceira página não deveria conter nenhuma mensagem"
        # Opcional
        ids_pagina_1 = {m.id_mensagem for m in mensagem_pagina_1}
        ids_pagina_2 = {m.id_mensagem for m in mensagem_pagina_2}
        assert ids_pagina_1.isdisjoint(ids_pagina_2), "As mensagens da página 1 não devem se repetir na página 2"

    def test_atualizar_mensagem(self,test_db):
        criar_tabela_usuario()
        criar_tabela_mensagem()
        #Arrange
        mensagem = Mensagem(
            id_mensagem=0,
            id_remetente=1,
            id_destinatario=2,
            conteudo="Mensagem antiga",
            data_hora=datetime.now(),
            nome_remetente="Gabriel",
            nome_destinatario="Javier"
        )
        #Act
        id_mensagem = inserir_mensagem(mensagem)
        mensagem_atualizada = obter_mensagem_por_id(id_mensagem)
        mensagem_atualizada.conteudo = "Mensagem atualizada"
        resultado = atualizar_mensagem(mensagem_atualizada)
        #Assert
        assert resultado is True

    def test_deletar_mensagem(self,test_db):
        criar_tabela_usuario()
        criar_tabela_mensagem()
        #Arrange
        mensagem = Mensagem(
            id_mensagem=0,
            id_remetente=1,
            id_destinatario=2,
            conteudo="Mensagem para deletar",
            data_hora=datetime.now(),
            nome_remetente="Gabriel",
            nome_destinatario="MK"
        )
        #Act
        id_mensagem = inserir_mensagem(mensagem)
        resultado = deletar_mensagem(id_mensagem)
        #Assert
        assert resultado is True
