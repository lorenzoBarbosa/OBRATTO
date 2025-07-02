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

    def test_obter_planos_por_pagina(self, test_db):
        criar_tabela_plano()

        # Inserir 5 planos para testar paginação
        for i in range(1, 6):
            plano = Plano(
                nome_plano=f"Plano {i}",
                valor_mensal=10.0 * i,
                limite_servico=5 * i,
                tipo_plano="Teste",
                descricao=f"Descrição {i}"
            )
            inserir_plano(plano)

        # Página 1: tamanho 2
        pagina_1 = obter_plano_por_pagina(pagina=1, tamanho_pagina=2)
        assert len(pagina_1) == 2
        assert pagina_1[0].nome_plano == "Plano 1"
        assert pagina_1[1].nome_plano == "Plano 2"

        # Página 2: tamanho 2
        pagina_2 = obter_plano_por_pagina(pagina=2, tamanho_pagina=2)
        assert len(pagina_2) == 2
        assert pagina_2[0].nome_plano == "Plano 3"
        assert pagina_2[1].nome_plano == "Plano 4"

        # Página 3: tamanho 2 (restante)
        pagina_3 = obter_plano_por_pagina(pagina=3, tamanho_pagina=2)
        assert len(pagina_3) == 1
        assert pagina_3[0].nome_plano == "Plano 5"

        # Página 4: tamanho 2 (sem resultados)
        pagina_4 = obter_plano_por_pagina(pagina=4, tamanho_pagina=2)
        assert len(pagina_4) == 0


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
