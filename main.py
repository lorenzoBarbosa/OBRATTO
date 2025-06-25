from faker import Faker
import faker_commerce
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import tabulate
import uvicorn


from data.administrador import administrador_repo
from data.anuncio import anuncio_repo
from data.avaliacao import avaliacao_repo
from data.cliente import cliente_repo
from data.cliente.cliente_model import Cliente
from data.fornecedor import fornecedor_repo
from data.fornecedor.fornecedor_model import Fornecedor
from data.inscricaoplano import inscricao_plano_repo
from data.mensagem import mensagem_repo
from data.notificacao import notificacao_repo
from data.orcamento import orcamento_repo
from data.orcamentoservico import orcamento_servico_repo
from data.plano import plano_repo
from data.prestador import prestador_repo
from data.prestador.prestador_model import Prestador
from data.servico import servico_repo
from data.usuario import usuario_repo
from data.usuario.usuario_model import Usuario


fake = Faker()
fake.add_provider(faker_commerce.Provider)

administrador_repo.criar_tabela_administrador()
anuncio_repo.criar_tabela_anuncio()
avaliacao_repo.criar_tabela_avaliacao()
cliente_repo.criar_tabela_cliente()
fornecedor_repo.criar_tabela_fornecedor()
inscricao_plano_repo.criar_tabela_inscricao_plano()
mensagem_repo.criar_tabela_mensagem()
notificacao_repo.criar_tabela_notificacao()
orcamento_repo.criar_tabela_orcamento()
orcamento_servico_repo.criar_tabela_orcamento_servico()
plano_repo.criar_tabela_plano()
prestador_repo.criar_tabela_prestador()
servico_repo.criar_tabela_servico()
usuario_repo.criar_tabela_usuario()

from faker import Faker
from data.usuario.usuario_repo import inserir_usuario
from data.cliente.cliente_repo import inserir_cliente
from data.fornecedor.fornecedor_repo import inserir_fornecedor
from data.prestador.prestador_repo import inserir_prestador
from data.plano.plano_repo import inserir_plano
from data.servico.servico_repo import inserir_servico
from data.orcamento.orcamento_repo import inserir_orcamento
from data.inscricaoplano.inscricao_plano_repo import inserir_inscricao_plano
from data.avaliacao.avaliacao_repo import inserir_avaliacao

from datetime import datetime, timedelta
import random

fake = Faker('pt_BR')

# Usuários:
for _ in range(30):
    usuario = Usuario(
        nome = fake.name(),
        email = fake.email(),
        senha = fake.password(),
        cpf_cnpj = fake.cpf(),
        telefone = fake.phone_number(),
        data_cadastro =  fake.date_time_this_decade(),
        endereco = fake.address()
    )

# Clientes:
for i in range(15):
    cliente = Cliente(
        id_usuario =  i + 1,
        genero = fake.random_element(elements=["Masculino", "Feminino", "Outro"]),
        data_nascimento =  fake.date_of_birth(minimum_age=18, maximum_age=90)
    )
    inserir_cliente(cliente)

# Prestadores:
for i in range(10):
    prestador = Prestador(
        id_usuario =  i + 26,
        razao_social =  fake.company(),
        area_atuacao = fake.job(),
        descricao_servicos = fake.text(max_nb_chars=100),
        tipo_pessoa = fake.random_element(elements=["Física", "Jurídica"]),
    )
    inserir_prestador(prestador)

# Fornecedores:
for i in range(10):
    fornecedor = Fornecedor(
        id_usuario = i + 16,
        razao_social = fake.company(),
    )
    inserir_fornecedor(fornecedor)

# Administradores:
for _ in range(5):
    administrador_repo.inserir_administrador({
        "id_usuario": fake.random_int(min=1, max=30),
    })

# Inscrição Plano:
for _ in range(3):
    inserir_inscricao_plano({
        "id_plano": fake.random_int(min=1, max=3),
        "id_fornecedor": fake.random_int(min=1, max=10),
        "id_prestador": fake.random_int(min=1, max=10)
    })

# Serviço:
for _ in range(20):
    inserir_servico({
        "id_prestador": random.randint(1, 10),
        "nome_prestador": fake.name(),
        "titulo": fake.word(),
        "descricao": fake.text(max_nb_chars=200),
        "valor_base": round(random.uniform(100, 5000), 2),
        "categoria": fake.random_element(elements=["Elétrica", "Hidráulica", "Pintura", "Construção"])
    })   
    
    
# Orçamento:
for _ in range(15):
    inserir_orcamento({
        "id_fornecedor": random.randint(1, 10),
        "id_cliente": random.randint(1, 15),
        "valor_estimado": round(random.uniform(500, 10000), 2),
        "data_solicitacao": fake.date_time_this_decade(),
        "prazo_entrega": fake.date_time_between(start_date="+5d", end_date="+60d"),
        "status": fake.random_element(elements=["pendente", "aprovado", "rejeitado"]),
        "descricao": fake.text(max_nb_chars=300)
    })

# Avaliações:
for _ in range(10):
    inserir_avaliacao({
        "id_avaliador": random.randint(1, 30),
        "id_avaliado": random.randint(1, 30),
        "nota": round(random.uniform(1, 5), 1),
        "descricao": fake.sentence(),
        "nome_avaliador": fake.name(),
        "nome_avaliado": fake.name(),
        "data_avaliacao": fake.date_time_this_decade(),
    })

# Anuncios:
for _ in range(15):
    id_remetente = random.randint(1, 30)
    id_destinatario = random.randint(1, 30)
    mensagem_repo.inserir_mensagem({
        "id_remetente": id_remetente,
        "id_destinatario": id_destinatario,
        "conteudo": fake.text(max_nb_chars=300),
        "data_hora": fake.date_time_this_year(),
        "nome_remetente": fake.name(),      
        "nome_destinatario": fake.name()    
    })


# Notificações:
for _ in range(20):
    notificacao_repo.inserir_notificacao({
        "id_usuario": random.randint(1, 30),
        "mensagem": fake.sentence(nb_words=10),
        "data_hora": fake.date_time_this_year(),
        "tipo_notificacao": fake.random_element(elements=["alerta", "mensagem", "sistema", "promoção"]),
        "vizualizar": fake.boolean()
    })



# Orcamento servico:
for _ in range(15):
    id_prestador = random.randint(1, 10)  
    id_cliente = random.randint(1, 15)    
    id_servico = random.randint(1, 20)   
    orcamento_servico_repo.inserir_orcamento_servico({
        "id_orcamento": random.randint(1, 30),  
        "id_servico": id_servico,
        "id_prestador": id_prestador,
        "id_cliente": id_cliente,
        "valor_estimado": round(random.uniform(100, 10000), 2),
        "data_solicitacao": fake.date_this_decade(),
        "prazo_entrega": fake.date_between(start_date="+5d", end_date="+60d"),
        "status": fake.random_element(elements=["pendente", "aprovado", "rejeitado"]),
        "descricao": fake.text(max_nb_chars=200),
        "nome_prestador": fake.name(),  
        "nome_cliente": fake.name(),    
        "titulo_servico": fake.word()
    })







