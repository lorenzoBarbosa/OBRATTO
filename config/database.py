"""
Configurações do banco de dados OBRATTO
"""
import os

# Configurações do banco de dados
DATABASE_NAME = "obratto.db"
DATABASE_PATH = os.path.join(os.path.dirname(__file__), DATABASE_NAME)

# Configurações de teste
TEST_DATABASE_NAME = "obratto_test.db"

def get_database_path():
    """Retorna o caminho do banco de dados baseado no ambiente"""
    if os.environ.get('TESTING'):
        return TEST_DATABASE_NAME
    return DATABASE_NAME

# Informações sobre as tabelas
TABLES_INFO = {
    'produto': {
        'name': 'PRODUTO',
        'columns': ['id', 'nome', 'descricao', 'preco', 'quantidade']
    }
    # Adicione outras tabelas aqui conforme necessário
}
