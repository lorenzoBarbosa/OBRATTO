"""
Teste completo do fluxo de planos
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data.plano import plano_repo
from data.inscricaoplano import inscricao_plano_repo
from data.inscricaoplano.inscricao_plano_model import InscricaoPlano

def test_fluxo_completo():
    print("=== Teste Completo do Fluxo de Planos ===")
    
    id_fornecedor = 1
    
    # 1. Verificar planos disponíveis
    print("\n1. Verificando planos disponíveis...")
    planos = plano_repo.obter_plano_por_pagina(pagina=1, tamanho_pagina=10)
    for plano in planos:
        print(f"   - {plano.nome_plano}: R$ {plano.valor_mensal}")
    
    # 2. Verificar se já tem assinatura
    print(f"\n2. Verificando assinatura atual do fornecedor {id_fornecedor}...")
    assinatura_atual = inscricao_plano_repo.obter_assinatura_ativa_por_fornecedor(id_fornecedor)
    if assinatura_atual:
        plano_atual = plano_repo.obter_plano_por_id(assinatura_atual.id_plano)
        print(f"   ✅ Tem assinatura ativa: {plano_atual.nome_plano}")
    else:
        print("   ❌ Não tem assinatura ativa")
    
    # 3. Testar mudança de plano (se tiver assinatura)
    if assinatura_atual and len(planos) > 1:
        print(f"\n3. Testando alteração de plano...")
        novo_plano = planos[1] if assinatura_atual.id_plano == planos[0].id_plano else planos[0]
        print(f"   Alterando para: {novo_plano.nome_plano}")
        
        assinatura_atual.id_plano = novo_plano.id_plano
        sucesso = inscricao_plano_repo.atualizar_inscricao_plano(assinatura_atual)
        
        if sucesso:
            print("   ✅ Plano alterado com sucesso!")
            # Verificar se mudou
            assinatura_verificacao = inscricao_plano_repo.obter_assinatura_ativa_por_fornecedor(id_fornecedor)
            if assinatura_verificacao and assinatura_verificacao.id_plano == novo_plano.id_plano:
                print(f"   ✅ Confirmado: Plano atual é {novo_plano.nome_plano}")
            else:
                print("   ❌ Erro: Plano não foi alterado")
        else:
            print("   ❌ Erro ao alterar plano")
    
    # 4. Testar cancelamento
    print(f"\n4. Testando cancelamento...")
    assinatura_para_cancelar = inscricao_plano_repo.obter_assinatura_ativa_por_fornecedor(id_fornecedor)
    if assinatura_para_cancelar:
        sucesso = inscricao_plano_repo.deletar_inscricao_plano(assinatura_para_cancelar.id_inscricao_plano)
        if sucesso:
            print("   ✅ Assinatura cancelada com sucesso!")
            
            # Verificar se foi cancelada
            verificacao = inscricao_plano_repo.obter_assinatura_ativa_por_fornecedor(id_fornecedor)
            if not verificacao:
                print("   ✅ Confirmado: Não há mais assinatura ativa")
            else:
                print("   ❌ Erro: Assinatura ainda existe")
        else:
            print("   ❌ Erro ao cancelar assinatura")
    
    # 5. Testar nova assinatura
    print(f"\n5. Testando nova assinatura...")
    plano_para_assinar = planos[0]
    nova_inscricao = InscricaoPlano(
        id_inscricao_plano=0,
        id_fornecedor=id_fornecedor,
        id_prestador=None,
        id_plano=plano_para_assinar.id_plano
    )
    
    inscricao_id = inscricao_plano_repo.inserir_inscricao_plano(nova_inscricao)
    if inscricao_id:
        print(f"   ✅ Nova assinatura criada: {plano_para_assinar.nome_plano}")
        
        # Verificar se foi criada
        verificacao_final = inscricao_plano_repo.obter_assinatura_ativa_por_fornecedor(id_fornecedor)
        if verificacao_final:
            print(f"   ✅ Confirmado: Assinatura ativa para {plano_para_assinar.nome_plano}")
        else:
            print("   ❌ Erro: Assinatura não foi encontrada")
    else:
        print("   ❌ Erro ao criar nova assinatura")
    
    print("\n=== Teste Completo Finalizado ===")

if __name__ == "__main__":
    test_fluxo_completo()
