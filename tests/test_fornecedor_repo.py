from datetime import datetime

from fastapi.encoders import isoformat
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
            razao_social="Fornecedor Ltda"
        )
        # Act
        id_inserido = inserir_fornecedor(fornecedor)
        # Assert
        fornecedor_db = obter_fornecedor_por_id(id_inserido)
        assert fornecedor_db is not None, "O fornecedor inserido não deveria ser None"
        assert fornecedor_db.nome == "Fornecedor Teste", "O nome do fornecedor inserido não confere"
        assert fornecedor_db.email == "fornecedor@email.com"

    def test_obter_fornecedor(self, test_db):
        # Arrange
        fornecedores = obter_fornecedor()
        # Act & Assert
        assert len(fornecedores) > 0, "Deveria haver pelo menos um fornecedor"
        assert isinstance(fornecedores[0], Fornecedor), "Os itens retornados devem ser instâncias de Fornecedor"

    def test_obter_fornecedor_por_id(self, test_db):
        # Arrange
        fornecedor = obter_fornecedor()[0]
        # Act
        resultado = obter_fornecedor_por_id(fornecedor.id)
        # Assert
        assert resultado is not None, "O fornecedor buscado não deveria ser None"
        assert resultado.id == fornecedor.id
        assert resultado.email == fornecedor.email

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
            razao_social="Fornecedor Ltda"
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
        # Arrange
        fornecedor = obter_fornecedor()[0]
        # Act
        resultado = deletar_fornecedor(fornecedor.id)
        # Assert
        assert resultado is True, "A exclusão do fornecedor deveria retornar True"
        deletado = obter_fornecedor_por_id(fornecedor.id)
        assert deletado is None, "O fornecedor deveria ter sido excluído"
