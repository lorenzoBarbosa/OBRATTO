from typing import Optional, List
from data.cliente.cliente_model import Cliente
from data.cliente.cliente_sql import *
from data.usuario.usuario_model import Usuario
from utils.db import open_connection


def criar_tabela_cliente() -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_CLIENTE)
        conn.commit()
        return True


def inserir_cliente(cliente: Cliente) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_CLIENTE, (
            cliente.id_usuario,
            cliente.genero,
            cliente.data_nascimento
        ))
        conn.commit()
        return cursor.lastrowid

def obter_cliente() -> List[Usuario]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_CLIENTE)
        rows = cursor.fetchall()
        return [
            Usuario(
                id=row["id"],
                nome=row["nome"],
                email=row["email"],
                senha=row["senha"],
                cpf_cnpj=row["cpf_cnpj"],
                telefone=row["telefone"],
                data_cadastro=row["data_cadastro"],
                endereco=row["endereco"],
                tipo_usuario=row["tipo_usuario"]
            ) for row in rows
        ]

def obter_cliente_por_id(cliente_id: int) -> Optional[Usuario]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_CLIENTE_POR_ID, (cliente_id,))
        row = cursor.fetchone()
        if row:
            return Usuario(
                id=row["id"],
                nome=row["nome"],
                email=row["email"],
                senha=row["senha"],
                cpf_cnpj=row["cpf_cnpj"],
                telefone=row["telefone"],
                data_cadastro=row["data_cadastro"],
                endereco=row["endereco"],
                tipo_usuario=row["tipo_usuario"]
            )
    return None


def atualizar_cliente(cliente: Cliente) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_CLIENTE,(
            cliente.genero,
            cliente.data_nascimento,
            cliente.id
        ))
        conn.commit()
        return cursor.rowcount > 0


def deletar_cliente(cliente_id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(DELETAR_CLIENTE, (cliente_id,))
        conn.commit()
        return cursor.rowcount > 0
