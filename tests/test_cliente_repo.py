from datetime import datetime, date
from data.cliente.cliente_repo import (
    criar_tabela_cliente,
    inserir_cliente,
    obter_cliente,
    obter_cliente_por_id,
    atualizar_cliente,
    deletar_cliente,
)
from data.cliente.cliente_model import Cliente
from data.usuario.usuario_repo import criar_tabela_usuario

class TestClienteRepo:

    def test_criar_tabela_cliente(self, test_db):
        # Arrange
        criar_tabela_usuario()
        # Act
        resultado = criar_tabela_cliente()
        # Assert
        assert resultado is True, "A criação da tabela cliente deveria retornar True"

    def test_inserir_cliente(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        cliente_novo = Cliente(
            id=0, 
            nome="Maria Silva",
            email="maria.silva@email.com",
            senha="senhaforte123",
            cpf_cnpj="111.222.333-44",
            telefone="27988887777",
            data_cadastro=datetime.now(),
            endereco="Rua dos Clientes, 456",
            tipo_usuario=2, 
            genero="Feminino",
            data_nascimento=date(1995, 10, 25)
        )
        # Act
        id_inserido = inserir_cliente(cliente_novo)
        # Assert
        cliente_db = obter_cliente_por_id(id_inserido)
        assert cliente_db is not None, "O cliente inserido não deveria ser None"
        assert cliente_db.nome == "Maria Silva"
        assert cliente_db.genero == "Feminino"
        assert cliente_db.data_nascimento == date(1995, 10, 25)

    def test_obter_todos_os_clientes(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        cliente_1 = Cliente(id=0, nome="Cliente A", email="a@a.com", senha="123", cpf_cnpj="1", telefone="1", data_cadastro=datetime.now(), endereco="Rua A", tipo_usuario=2, genero="M", data_nascimento=date(2001, 1, 1))
        cliente_2 = Cliente(id=0, nome="Cliente B", email="b@b.com", senha="456", cpf_cnpj="2", telefone="2", data_cadastro=datetime.now(), endereco="Rua B", tipo_usuario=2, genero="F", data_nascimento=date(2002, 2, 2))
        inserir_cliente(cliente_1)
        inserir_cliente(cliente_2)
        # Act
        lista_clientes = obter_cliente()
        # Assert
        assert len(lista_clientes) == 2, "A lista deveria conter dois clientes"
        assert lista_clientes[0].nome == "Cliente A"
        assert lista_clientes[1].nome == "Cliente B"
        
    def test_atualizar_cliente(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        cliente_original = Cliente(
            id=0,
            nome="João Santos",
            email="joao.santos@email.com",
            senha="senhaoriginal",
            cpf_cnpj="444.555.666-77",
            telefone="27977776666",
            data_cadastro=datetime.now(),
            endereco="Endereço Antigo, 1",
            tipo_usuario=2,
            genero="Masculino",
            data_nascimento=date(1980, 1, 15)
        )
        id_inserido = inserir_cliente(cliente_original)
        cliente_para_atualizar = obter_cliente_por_id(id_inserido)
        cliente_para_atualizar.nome = "João da Silva Santos"
        cliente_para_atualizar.genero = "Outro"
        cliente_para_atualizar.endereco = "Endereço Novo, 100"
        # Act
        resultado = atualizar_cliente(cliente_para_atualizar)
        # Assert
        assert resultado is True, "A atualização deveria retornar True"
        cliente_atualizado_db = obter_cliente_por_id(id_inserido)
        assert cliente_atualizado_db.nome == "João da Silva Santos"
        assert cliente_atualizado_db.genero == "Outro"
        assert cliente_atualizado_db.endereco == "Endereço Novo, 100"

    def test_deletar_cliente(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        cliente_para_deletar = Cliente(id=0, nome="Cliente Temporário", email="temp@temp.com", senha="123", cpf_cnpj="0", telefone="0", data_cadastro=datetime.now(), endereco="Rua Temp", tipo_usuario=2, genero="N/A", data_nascimento=date(2000, 1, 1))
        id_inserido = inserir_cliente(cliente_para_deletar)
        assert obter_cliente_por_id(id_inserido) is not None
        # Act
        resultado = deletar_cliente(id_inserido)
        # Assert
        assert resultado is True, "A deleção deveria retornar True"
        cliente_apos_delecao = obter_cliente_por_id(id_inserido)
        assert cliente_apos_delecao is None, "O cliente deveria ser None após a deleção"