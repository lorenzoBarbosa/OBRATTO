import sys
import os
from data.plano.plano_model import Plano
from data.plano.plano_repo import *

class Test_PlanoRepo:

    def test_criar_tabela_plano(self, test_db):
        resultado = criar_tabela_plano()
        assert resultado is True, "A criação da tabela deveria retornar True"

    def test_inserir_e_obter_plano(self, test_db):
        criar_tabela_plano()

        plano = Plano(
            nome_plano="Plano Premium",
            valor_mensal=99.90,
            limite_servico=10,
            tipo_plano="Mensal",
            descricao="Acesso completo a todos os recursos"
        )

        id_plano = inserir_plano(plano)
        assert id_plano is not None

        plano_db = obter_plano_por_id(id_plano)
        assert plano_db is not None
        assert plano_db.nome_plano == "Plano Premium"

        plano_nome = obter_plano_por_nome("Plano Premium")
        assert plano_nome is not None
        assert plano_nome.valor_mensal == 99.90

    def test_obter_todos_os_planos(self, test_db):
        criar_tabela_plano()

        plano = Plano(
            nome_plano="Plano Teste",
            valor_mensal=49.90,
            limite_servico=5,
            tipo_plano="Básico",
            descricao="Plano de entrada"
        )
        inserir_plano(plano)

        planos = obter_todos_os_planos()
        assert isinstance(planos, list)
        assert len(planos) >= 1

    def test_obter_plano_por_nome(self, test_db):
        criar_tabela_plano()

        plano = Plano(
            nome_plano="Plano Premium",
            valor_mensal=99.99,
            limite_servico=10,
            tipo_plano="Premium",
            descricao="Plano com mais vantagens"
        )
        id_plano = inserir_plano(plano)
        assert id_plano is not None

        plano_obtido = obter_plano_por_nome("Plano Premium")
        assert plano_obtido is not None
        assert plano_obtido.nome_plano == "Plano Premium"
        assert plano_obtido.valor_mensal == 99.99

    def test_obter_plano_por_id(self, test_db):
        criar_tabela_plano()

        plano = Plano(
            nome_plano="Plano Intermediário",
            valor_mensal=69.90,
            limite_servico=5,
            tipo_plano="Intermediário",
            descricao="Plano médio para usuários frequentes"
        )
        id_plano = inserir_plano(plano)
        assert id_plano is not None

        plano_obtido = obter_plano_por_id(id_plano)
        assert plano_obtido is not None
        assert plano_obtido.id_plano == id_plano
        assert plano_obtido.nome_plano == "Plano Intermediário"

    def test_atualizar_plano_por_id(self, test_db):
        criar_tabela_plano()

        plano_inicial = Plano(
            nome_plano="Plano Antigo",
            valor_mensal=59.90,
            limite_servico=3,
            tipo_plano="Mensal",
            descricao="Plano inicial"
        )
        id_plano = inserir_plano(plano_inicial)
        assert id_plano is not None

        plano_atualizado = Plano(
            id_plano=id_plano,
            nome_plano="Plano Atualizado",
            valor_mensal=89.90,
            limite_servico=7,
            tipo_plano="Premium",
            descricao="Plano com mais vantagens"
        )

        sucesso = atualizar_plano_por_id(plano_atualizado)
        assert sucesso is True

        plano_db = obter_plano_por_id(id_plano)
        assert plano_db is not None
        assert plano_db.nome_plano == "Plano Atualizado"
        assert plano_db.valor_mensal == 89.90
        assert plano_db.limite_servico == 7
        assert plano_db.tipo_plano == "Premium"
        assert plano_db.descricao == "Plano com mais vantagens"

    def test_deletar_plano(self, test_db):
        criar_tabela_plano()

        plano = Plano(
            nome_plano="Plano Deletar",
            valor_mensal=29.90,
            limite_servico=2,
            tipo_plano="Temporário",
            descricao="Plano para exclusão"
        )
        id_plano = inserir_plano(plano)
        assert id_plano is not None

        sucesso = deletar_plano(id_plano)
        assert sucesso is True

        plano_db = obter_plano_por_id(id_plano)
        assert plano_db is None
