"""
Script para popular o banco de dados com dados de teste
"""
from data.plano import plano_repo
from data.plano.plano_model import Plano
from data.inscricaoplano import inscricao_plano_repo
from data.inscricaoplano.inscricao_plano_model import InscricaoPlano
from data.pagamento.pagamento_repo import PagamentoRepository

def setup_test_data():
    """Cria tabelas e insere dados de teste"""
    
    # Criar instância do repositório de pagamento
    pagamento_repo = PagamentoRepository()
    
    # Criar tabelas
    print("Criando tabelas...")
    plano_repo.criar_tabela_plano()
    inscricao_plano_repo.criar_tabela_inscricao_plano()
    pagamento_repo.criar_tabela_pagamento()
    
    # Inserir planos de teste
    print("Inserindo planos de teste...")
    planos_teste = [
        Plano(
            id_plano=0,
            nome_plano="Básico",
            valor_mensal=29.90,
            limite_servico=5,
            tipo_plano="basico",
            descricao="Plano básico com até 5 serviços por mês"
        ),
        Plano(
            id_plano=0,
            nome_plano="Premium",
            valor_mensal=59.90,
            limite_servico=15,
            tipo_plano="premium",
            descricao="Plano premium com até 15 serviços por mês"
        ),
        Plano(
            id_plano=0,
            nome_plano="Empresarial",
            valor_mensal=99.90,
            limite_servico=50,
            tipo_plano="empresarial",
            descricao="Plano empresarial com até 50 serviços por mês"
        )
    ]
    
    for plano in planos_teste:
        plano_id = plano_repo.inserir_plano(plano)
        print(f"Plano '{plano.nome_plano}' inserido com ID: {plano_id}")
    
    print("Dados de teste inseridos com sucesso!")
    
    # Listar planos criados
    print("\nPlanos disponíveis:")
    planos = plano_repo.obter_todos_os_planos()
    for plano in planos:
        print(f"ID: {plano.id_plano}, Nome: {plano.nome_plano}, Valor: R$ {plano.valor_mensal}")

if __name__ == "__main__":
    setup_test_data()
