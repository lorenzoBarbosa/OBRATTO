#!/usr/bin/env python3
"""Teste das funcionalidades de planos"""

import sqlite3
from data.plano.plano_repo import obter_plano_por_pagina, obter_plano_por_id
from data.plano.plano_model import Plano

def main():
    print("=== TESTE DO SISTEMA DE PLANOS ===\n")
    
    # 1. Verificar tabelas no banco
    print("1. Verificando tabelas no banco:")
    conn = sqlite3.connect('obratto.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tabelas = cursor.fetchall()
    print(f"   Tabelas encontradas: {[t[0] for t in tabelas]}")
    conn.close()
    
    # 2. Verificar planos existentes
    print("\n2. Verificando planos existentes:")
    try:
        planos = obter_plano_por_pagina(pagina=1, tamanho_pagina=10)
        print(f"   Total de planos encontrados: {len(planos)}")
        
        for plano in planos:
            print(f"   - ID: {plano.id_plano}")
            print(f"     Nome: {plano.nome_plano}")
            print(f"     Valor: R$ {plano.valor_mensal}")
            print(f"     Limite de serviços: {plano.limite_servico}")
            print(f"     Tipo: {plano.tipo_plano}")
            print(f"     Descrição: {plano.descricao}")
            print()
            
    except Exception as e:
        print(f"   Erro ao buscar planos: {e}")
    
    # 3. Teste das rotas (URLs que devem funcionar)
    print("3. URLs disponíveis para teste:")
    print("   - http://127.0.0.1:8000/fornecedor/planos/listar")
    print("   - http://127.0.0.1:8000/fornecedor/planos/alterar")
    print("   - http://127.0.0.1:8000/fornecedor/planos/cancelar")
    
    print("\n=== TESTE CONCLUÍDO ===")

if __name__ == "__main__":
    main()
