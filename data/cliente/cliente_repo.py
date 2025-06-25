from typing import Optional, List
from data.cliente.cliente_model import Cliente
from data.cliente.cliente_sql import *
from utils.db import open_connection


def criar_tabela_cliente() -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_CLIENTE)
        conn.commit()
        return True


def inserir_cliente(cliente: Cliente) -> Optional[int]:
    """
    Insere os dados específicos do cliente na tabela cliente.
    O id deve já existir na tabela usuario.
    """
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_CLIENTE, (
            cliente["id"],          
            cliente["genero"],
            cliente["data_nascimento"]
        ))
        conn.commit()
        return cursor.lastrowid


def obter_cliente() -> List[Cliente]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_CLIENTE)
        rows = cursor.fetchall()
        clientes = []
        for row in rows:
            clientes.append(Cliente(
                id=row["id"],
                nome=row["nome"],
                email=row["email"],
                senha=row["senha"],
                cpf_cnpj=row["cpf_cnpj"],
                telefone=row["telefone"],
                data_cadastro=row["data_cadastro"],
                endereco=row["endereco"],
                genero=row["genero"],
                data_nascimento=row["data_nascimento"]
            ))
        return clientes


def obter_cliente_por_id(cliente_id: int) -> Optional[Cliente]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_CLIENTE_POR_ID, (cliente_id,))
        row = cursor.fetchone()
        if row:
            return Cliente (
                id=row["id"],
                nome=row["nome"],
                email=row["email"],
                senha=row["senha"],
                cpf_cnpj=row["cpf_cnpj"],
                telefone=row["telefone"],
                data_cadastro=row["data_cadastro"],
                endereco=row["endereco"],
                genero=row["genero"],
                data_nascimento=row["data_nascimento"],
            )
        return None


def atualizar_cliente(cliente: Cliente) -> bool:
    """
    Atualiza apenas os dados específicos do cliente.
    Para dados do usuário, use o repositório usuario.
    """
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_CLIENTE,(
            cliente["genero"],
            cliente["data_nascimento"],
            cliente["id"]
        ))
        conn.commit()
        return cursor.rowcount > 0


def deletar_cliente(cliente_id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(DELETAR_CLIENTE, (cliente_id,))
        conn.commit()
        return cursor.rowcount > 0
