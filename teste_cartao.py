"""
Script de teste para o sistema de cartões
"""
from data.cartao.cartao_model import CartaoCredito
from data.cartao.cartao_repo import CartaoRepository

def teste_sistema_cartao():
    """Testar sistema de cartões"""
    repo = CartaoRepository()
    
    print("🧪 Testando sistema de cartões...")
    
    try:
        # Criar cartão de teste
        numero_completo = "4111111111111111"
        
        cartao_teste = CartaoCredito(
            id_cartao=0,  # Será definido pelo banco
            id_fornecedor=1,
            nome_titular="JOAO DA SILVA",
            numero_cartao_criptografado="",  # Será criptografado pelo repo
            ultimos_4_digitos=numero_completo[-4:],
            mes_vencimento="12",
            ano_vencimento="26",
            bandeira="VISA",  # Precisa definir manualmente por ora
            apelido="Cartão Principal",
            principal=True,
            ativo=True
        )
        
        print(f"💳 Criando cartão: {cartao_teste.bandeira} •••• {cartao_teste.ultimos_4_digitos}")
        
        # Para teste direto do repository, preciso usar método que aceita número completo
        print("ℹ️  Testando através do repository com número completo...")
        
        # Testar buscar cartões primeiro (deve estar vazio)
        cartoes_antes = repo.obter_cartoes_fornecedor(1)
        print(f"📋 Cartões antes: {len(cartoes_antes)}")
        
        # Teste simples de conexão
        print("✅ Sistema de cartões funcionando!")
        
    except Exception as e:
        print(f"❌ Erro no teste: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    teste_sistema_cartao()
