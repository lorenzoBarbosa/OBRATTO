from typing import Optional, List
from data.cliente.cliente_model import Cliente
from data.cliente.cliente_sql import CRIAR_TABELA, INSERIR, OBTER_TODOS, OBTER_POR_ID, UPDATE, DELETE
from utils.db import open_connection


def criar_tabela() -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        conn.commit()
        return True


def inserir(cliente: Cliente) -> Optional[int]:
    """
    Insere os dados específicos do cliente na tabela cliente.
    O id_usuario deve já existir na tabela usuario.
    """
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            cliente.id_usuario,
            cliente.genero,
            cliente.data_nascimento
        ))
        conn.commit()
        return cursor.lastrowid


def obter_todos() -> List[Cliente]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        clientes = []
        for row in rows:
            clientes.append(Cliente(
                id=row["id"],
                id_usuario=row["id_usuario"],
                nome=row["nome"],                 
                email=row["email"],              
                senha=None,                      
                cpf_cnpj=None,                    
                telefone=None,                   
                data_cadastro=None,               
                endereco=None,                 
                cpf=None,                      
                genero=row["genero"],            
                data_nascimento=row["data_nascimento"]
            ))
        return clientes


def obter_por_id(cliente_id: int) -> Optional[Cliente]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (cliente_id,))
        row = cursor.fetchone()
        if row:
            return Cliente(
                id=row["id"],
                id_usuario=row["id_usuario"],
                nome=row["nome"],
                email=row["email"],
                senha=None,
                cpf_cnpj=None,
                telefone=None,
                data_cadastro=None,
                endereco=None,
                cpf=None,
                genero=row["genero"],
                data_nascimento=row["data_nascimento"]
            )
        return None


def atualizar(cliente: Cliente) -> bool:
    """
    Atualiza apenas os dados específicos do cliente.
    Para dados do usuário, use o repositório usuario.
    """
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(UPDATE, (
            cliente.id_usuario,
            cliente.genero,
            cliente.data_nascimento,
            cliente.id
        ))
        conn.commit()
        return cursor.rowcount > 0


def deletar(cliente_id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(DELETE, (cliente_id,))
        conn.commit()
        return cursor.rowcount > 0
