"""
Script para criar a tabela de cartões no banco de dados
"""
import sqlite3
from data.cartao.cartao_sql import SQL_CRIAR_TABELA_CARTAO

def criar_tabela_cartao():
    """Criar tabela de cartões no banco de dados"""
    try:
        # Conectar ao banco
        conn = sqlite3.connect('obratto.db')
        cursor = conn.cursor()
        
        # Executar SQL de criação da tabela
        print("Criando tabela cartao_credito...")
        cursor.execute(SQL_CRIAR_TABELA_CARTAO)
        
        # Confirmar mudanças
        conn.commit()
        print("✅ Tabela cartao_credito criada com sucesso!")
        
        # Verificar se a tabela foi criada
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='cartao_credito';")
        resultado = cursor.fetchone()
        
        if resultado:
            print(f"✅ Tabela confirmada: {resultado[0]}")
            
            # Mostrar estrutura da tabela
            cursor.execute("PRAGMA table_info(cartao_credito);")
            colunas = cursor.fetchall()
            print("\n📊 Estrutura da tabela cartao_credito:")
            for coluna in colunas:
                print(f"  - {coluna[1]} ({coluna[2]})")
        else:
            print("❌ Erro: Tabela não foi criada")
            
    except Exception as e:
        print(f"❌ Erro ao criar tabela: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    criar_tabela_cartao()
