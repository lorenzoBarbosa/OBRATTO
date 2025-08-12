# OBRATTO - Sistema de Gestão de Produtos

## Banco de Dados

O sistema utiliza SQLite com o arquivo `obratto.db` para armazenar todas as informações.

### Configuração do Banco

- **Arquivo**: `obratto.db`
- **Localização**: Diretório raiz do projeto
- **Tipo**: SQLite 3

### Inicialização do Banco

Para inicializar o banco com dados de exemplo, execute:

```bash
python init_database.py
```

Este script irá:
1. Criar a tabela `PRODUTO` se ela não existir
2. Inserir 8 produtos de exemplo
3. Exibir um relatório dos dados inseridos

### Estrutura da Tabela PRODUTO

```sql
CREATE TABLE IF NOT EXISTS PRODUTO (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL
);
```

### Rotas de Produtos

- `GET /fornecedor/produtos/debug` - Informações de debug do banco
- `GET /fornecedor/produtos/listar` - Lista todos os produtos
- `GET /fornecedor/produtos/inserir` - Formulário para inserir produto
- `POST /fornecedor/produtos/inserir` - Insere novo produto
- `GET /fornecedor/produtos/atualizar/{id}` - Formulário para atualizar produto
- `POST /fornecedor/produtos/atualizar/{id}` - Atualiza produto existente
- `GET /fornecedor/produtos/excluir/{id}` - Exclui produto (método GET)
- `POST /fornecedor/produtos/excluir/{id}` - Exclui produto (método POST)

### Como Executar

1. Ative o ambiente virtual:
   ```bash
   .venv\Scripts\activate
   ```

2. Execute o servidor:
   ```bash
   python main.py
   ```

3. Acesse no navegador:
   - http://127.0.0.1:8000/fornecedor/produtos/debug
   - http://127.0.0.1:8000/fornecedor/produtos/listar

### Dados de Exemplo

O sistema inclui 8 produtos de exemplo:
- Notebook Dell Inspiron (R$ 2.500,00)
- Mouse Logitech MX Master 3 (R$ 350,00)
- Teclado Mecânico RGB (R$ 450,00)
- Monitor LG 24'' (R$ 800,00)
- Webcam Logitech C920 (R$ 380,00)
- SSD Samsung 500GB (R$ 280,00)
- Memória RAM 16GB (R$ 420,00)
- Placa de Vídeo RTX 3060 (R$ 1.800,00)
