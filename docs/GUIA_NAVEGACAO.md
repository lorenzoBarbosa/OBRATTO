# 🚀 Guia de Navegação - OBRATTO

## Como Testar o Sistema

### 1. **Executar o Servidor**
```bash
cd "c:\Users\20221imi025\Documents\Projeto integrador\OBRATTO"
python main.py
```

### 2. **Rotas Principais para Testar**

#### 🏠 **Página Inicial**
- **URL**: http://127.0.0.1:8000/
- **Descrição**: Página inicial com menu de navegação

#### 🏪 **Painel do Fornecedor**
- **URL**: http://127.0.0.1:8000/fornecedor
- **Descrição**: Home do fornecedor com acesso rápido às funcionalidades

#### 📦 **Gestão de Produtos**
- **Listar**: http://127.0.0.1:8000/fornecedor/produtos/listar
- **Inserir**: http://127.0.0.1:8000/fornecedor/produtos/inserir
- **Atualizar**: http://127.0.0.1:8000/fornecedor/produtos/atualizar/1
- **Debug**: http://127.0.0.1:8000/fornecedor/produtos/debug

### 3. **Fluxo de Teste Completo**

1. **Acesse a página inicial**: http://127.0.0.1:8000/
2. **Clique em "Fornecedor"**
3. **Na home do fornecedor, explore as opções**:
   - 📦 **Gerenciar Produtos** → Lista todos os produtos
   - ➕ **Adicionar Produto** → Formulário para novo produto
   - 🔧 **Informações do Sistema** → Status do banco

### 4. **Testando CRUD Completo**

#### ✅ **Create (Criar)**
1. Acesse: http://127.0.0.1:8000/fornecedor/produtos/inserir
2. Preencha os campos
3. Clique em "Inserir Produto"

#### ✅ **Read (Ler)**
1. Acesse: http://127.0.0.1:8000/fornecedor/produtos/listar
2. Veja todos os produtos cadastrados

#### ✅ **Update (Atualizar)**
1. Na listagem, clique em "Editar" em qualquer produto
2. Modifique os dados
3. Clique em "Atualizar Produto"

#### ✅ **Delete (Excluir)**
1. Na listagem, clique em "Excluir" em qualquer produto
2. Confirme a exclusão

### 5. **Navegação Entre Páginas**

Todas as páginas têm uma **barra de navegação** no topo com:
- 🏪 **Home** → Volta para o painel do fornecedor
- 📦 **Produtos** → Lista de produtos
- ➕ **Novo Produto** → Formulário de inserção
- 🔧 **Debug** → Informações do sistema

### 6. **Banco de Dados**

- **Arquivo**: `obratto.db`
- **Produtos pré-cadastrados**: 5 produtos de exemplo
- **Operações**: Todas as operações CRUD funcionando

### 7. **Recursos Implementados**

- ✅ **Design responsivo** e moderno
- ✅ **Navegação intuitiva** entre páginas
- ✅ **Mensagens de feedback** para ações
- ✅ **Confirmação de exclusão**
- ✅ **Validação de formulários**
- ✅ **Banco de dados funcional**
- ✅ **Templates HTML organizados**

### 🎯 **Teste Rápido**

1. Execute: `python main.py`
2. Abra: http://127.0.0.1:8000/
3. Navegue pelo sistema usando os menus
4. Teste inserir, editar e excluir produtos

**Seu sistema está 100% funcional para testes!** 🚀
