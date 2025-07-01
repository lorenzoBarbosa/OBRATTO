from datetime import datetime
from data.fornecedor.fornecedor_repo import (
    criar_tabela_fornecedor,
    inserir_fornecedor,
    obter_fornecedor,
    obter_fornecedor_por_id,
    atualizar_fornecedor,
    deletar_fornecedor
)
from data.fornecedor.fornecedor_model import Fornecedor
from data.usuario.usuario_repo import criar_tabela_usuario


class TestFornecedorRepo:
    def test_criar_tabela_fornecedor(self, test_db):
        # Arrange
        criar_tabela_usuario()
        # Act
        resultado = criar_tabela_fornecedor()
        # Assert
        assert resultado is True, "A criação da tabela fornecedor deveria retornar True"

    def test_inserir_fornecedor(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_fornecedor()
        fornecedor = Fornecedor(
            id=0,
            nome="Fornecedor Teste",
            email="fornecedor@email.com",
            senha="senha123",
            cpf_cnpj="12345678900",
            telefone="27999999999",
            data_cadastro=datetime.now().isoformat(),
            endereco="Rua dos Fornecedores, 123",
            razao_social="Fornecedor Ltda",
            tipo_usuario="fornecedor" 
        )
        # Act
        id_inserido = inserir_fornecedor(fornecedor)
        # Assert
        fornecedor_db = obter_fornecedor_por_id(id_inserido)
        assert fornecedor_db is not None, "O fornecedor inserido não deveria ser None"
        assert fornecedor_db.nome == "Fornecedor Teste", "O nome do fornecedor inserido não confere"
        assert fornecedor_db.email == "fornecedor@email.com"

    def test_obter_fornecedor(self, test_db):
        criar_tabela_usuario()
        criar_tabela_fornecedor()
        
        # Inserir um fornecedor para o teste
        fornecedor = Fornecedor(
            id=0,
            nome="Fornecedor Teste",
            email="fornecedor@email.com",
            senha="senha123",
            cpf_cnpj="12345678900",
            telefone="27999999999",
            data_cadastro=datetime.now().isoformat(),
            endereco="Rua dos Fornecedores, 123",
            razao_social="Fornecedor Ltda",
            tipo_usuario="fornecedor"
        )
        inserir_fornecedor(fornecedor)

        fornecedores = obter_fornecedor()

        assert len(fornecedores) > 0, "Deveria haver pelo menos um fornecedor"


    def test_obter_fornecedor_por_id(self, test_db):
        criar_tabela_usuario()      # cria tabela usuário (caso seja FK)
        criar_tabela_fornecedor()   # cria tabela fornecedor
        
        # Inserir algum fornecedor para ter dados
        fornecedor = Fornecedor(
            id=0,
            nome="Fornecedor Teste",
            email="fornecedor@email.com",
            senha="senha123",
            cpf_cnpj="12345678900",
            telefone="27999999999",
            data_cadastro=datetime.now().isoformat(),
            endereco="Rua dos Fornecedores, 123",
            razao_social="Fornecedor Ltda",
            tipo_usuario="fornecedor"
        )
        id_inserido = inserir_fornecedor(fornecedor)
        
        # Agora você pode chamar obter_fornecedor()
        fornecedor_bd = obter_fornecedor_por_id(id_inserido)
        
        # Assert 
        assert fornecedor_bd is not None, "Deveria retornar um fornecedor"
        assert fornecedor_bd.id == id_inserido, "ID do fornecedor retornado deve ser igual ao inserido"
        assert fornecedor_bd.nome == "Fornecedor Teste"
        assert fornecedor_bd.email == "fornecedor@email.com"
        assert fornecedor_bd.tipo_usuario == "fornecedor"
        assert fornecedor_bd.razao_social == "Fornecedor Ltda"


    def test_atualizar_fornecedor(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_fornecedor()

        fornecedor = Fornecedor(
            id=0,
            nome="Fornecedor Teste",
            email="fornecedor@email.com",
            senha="senha123",
            cpf_cnpj="12345678900",
            telefone="27999999999",
            data_cadastro=datetime.now().isoformat(),
            endereco="Rua dos Fornecedores, 123",
            razao_social="Fornecedor Ltda",
            tipo_usuario="fornecedor"
        )

        id_inserido = inserir_fornecedor(fornecedor)
        fornecedor_db = obter_fornecedor_por_id(id_inserido)

        fornecedor_db.nome = "Fornecedor Atualizado"
        fornecedor_db.razao_social = "Razão Atualizada"

        # Act
        resultado = atualizar_fornecedor(fornecedor_db)

        # Assert
        assert resultado is True, "A atualização do fornecedor deveria retornar True"

        atualizado = obter_fornecedor_por_id(id_inserido)
        assert atualizado.nome == "Fornecedor Atualizado"
        assert atualizado.razao_social == "Razão Atualizada"


    def test_deletar_fornecedor(self, test_db):
        criar_tabela_usuario()
        criar_tabela_fornecedor()

        fornecedor = Fornecedor(
            id=0,
            nome="Fornecedor Teste",
            email="fornecedor@email.com",
            senha="senha123",
            cpf_cnpj="12345678900",
            telefone="27999999999",
            data_cadastro=datetime.now().isoformat(),
            endereco="Rua dos Fornecedores, 123",
            razao_social="Fornecedor Ltda",
            tipo_usuario="fornecedor"
        )
        id_inserido = inserir_fornecedor(fornecedor)

        fornecedor_bd = obter_fornecedor_por_id(id_inserido)
        assert fornecedor_bd is not None

        resultado = deletar_fornecedor(id_inserido)
        assert resultado is True

        fornecedor_apos = obter_fornecedor_por_id(id_inserido)
        assert fornecedor_apos is None

