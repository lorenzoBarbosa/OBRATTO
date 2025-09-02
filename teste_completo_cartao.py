"""
Teste completo do sistema de cartões
"""
from data.cartao.cartao_repo import CartaoRepository

def teste_completo_cartao():
    """Testar sistema de cartões completo"""
    repo = CartaoRepository()
    
    print("🧪 Teste completo do sistema de cartões...")
    
    try:
        # Testar criação de cartão via formulário
        print("\n1️⃣ Testando criação via formulário...")
        resultado = repo.criar_cartao_from_form(
            id_fornecedor=1,
            numero_cartao="4111 1111 1111 1111",  # Visa teste
            nome_titular="João da Silva",
            mes_vencimento="12",
            ano_vencimento="26",
            apelido="Cartão Principal",
            principal=True
        )
        
        if resultado:
            print(f"✅ Cartão criado com ID: {resultado}")
        else:
            print("❌ Erro ao criar cartão")
            return
        
        # Listar cartões
        print("\n2️⃣ Listando cartões do fornecedor 1...")
        cartoes = repo.obter_cartoes_fornecedor(1)
        print(f"📋 Total de cartões: {len(cartoes)}")
        
        for cartao in cartoes:
            status_principal = "⭐ PRINCIPAL" if cartao.principal else ""
            print(f"  💳 {cartao.bandeira} •••• {cartao.ultimos_4_digitos}")
            print(f"     👤 {cartao.nome_titular}")
            print(f"     📝 {cartao.apelido} {status_principal}")
            print(f"     📅 {cartao.mes_vencimento}/{cartao.ano_vencimento}")
            print(f"     🔑 ID: {cartao.id_cartao}")
            print()
        
        # Testar cartão principal
        print("3️⃣ Testando busca do cartão principal...")
        cartao_principal = repo.obter_cartao_principal(1)
        if cartao_principal:
            print(f"✅ Cartão principal: {cartao_principal.bandeira} •••• {cartao_principal.ultimos_4_digitos}")
        else:
            print("❌ Nenhum cartão principal encontrado")
        
        # Criar segundo cartão (não principal)
        print("\n4️⃣ Criando segundo cartão...")
        resultado2 = repo.criar_cartao_from_form(
            id_fornecedor=1,
            numero_cartao="5555 5555 5555 4444",  # Mastercard teste
            nome_titular="João da Silva",
            mes_vencimento="10",
            ano_vencimento="28",
            apelido="Cartão Reserva",
            principal=False
        )
        
        if resultado2:
            print(f"✅ Segundo cartão criado com ID: {resultado2}")
            
            # Listar novamente
            cartoes = repo.obter_cartoes_fornecedor(1)
            print(f"📋 Total de cartões agora: {len(cartoes)}")
        
        print("\n✅ Teste completo finalizado com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro no teste: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    teste_completo_cartao()
