import pytest
from data.plano.plano_model import Plano
from data.plano.plano_repo import *

class Test_PlanoRepo:


    def test_criar_tabela_plano(self, test_db):
        resultado = criar_tabela_plano()
        assert resultado is None or resultado == True, "A criação da tabela deveria retornar True ou None"
        criar_tabela_plano()

    def test_inserir_plano(self):
        plano = Plano(
            nome_plano="Plano Básico",
            valor_mensal=99.90,
            limite_servico=10,
            tipo_plano="Mensal",
            descricao="Plano com limite de 10 serviços"
        )
        id_plano = inserir_plano(plano)
        assert id_plano is not None

    def test_obter_plano_por_id(self):
        plano = Plano(
            nome_plano="Plano Básico",
            valor_mensal=99.90,
            limite_servico=10,
            tipo_plano="Mensal",
            descricao="Plano com limite de 10 serviços"
        )
        id_plano = inserir_plano(plano)
        plano_obtido = obter_plano_por_id(id_plano)
        assert plano_obtido is not None
        assert plano_obtido.nome_plano == "Plano Básico"

    def test_obter_todos_planos(self):
        plano1 = Plano(
            nome_plano="Plano Básico",
            valor_mensal=99.90,
            limite_servico=10,
            tipo_plano="Mensal",
            descricao="Plano com limite de 10 serviços"
        )
        plano2 = Plano(
            nome_plano="Plano Premium",
            valor_mensal=199.90,
            limite_servico=50,
            tipo_plano="Anual",
            descricao="Plano com limite de 50 serviços"
        )
        inserir_plano(plano1)
        inserir_plano(plano2)

        planos = obter_todos_planos()
        assert isinstance(planos, list)
        assert len(planos) >= 2
        nomes = [p.nome_plano for p in planos]
        assert "Plano Básico" in nomes
        assert "Plano Premium" in nomes

    def test_atualizar_plano_por_id(self):
        plano = Plano(
            nome_plano="Plano Básico",
            valor_mensal=99.90,
            limite_servico=10,
            tipo_plano="Mensal",
            descricao="Plano com limite de 10 serviços"
        )
        id_plano = inserir_plano(plano)

        plano_atualizado = Plano(
            nome_plano="Plano Básico Atualizado",
            valor_mensal=120.00,
            limite_servico=15,
            tipo_plano="Mensal",
            descricao="Plano atualizado com limite maior"
        )
        resultado = atualizar_plano_por_id(id_plano, plano_atualizado)
        assert resultado is True

        plano_obtido = obter_plano_por_id(id_plano)
        assert plano_obtido.nome_plano == "Plano Básico Atualizado"
        assert plano_obtido.valor_mensal == 120.00
        assert plano_obtido.limite_servico == 15

    def test_deletar_plano(self):
        plano = Plano(
            nome_plano="Plano Básico",
            valor_mensal=99.90,
            limite_servico=10,
            tipo_plano="Mensal",
            descricao="Plano com limite de 10 serviços"
        )
        id_plano = inserir_plano(plano)
        resultado = deletar_plano(id_plano)
        assert resultado is True

        plano_excluido = obter_plano_por_id(id_plano)
        assert plano_excluido is None
