from typing import Optional, List
from data.cliente.cliente_model import Cliente
from data.cliente.cliente_sql import CRIAR_TABELA, INSERIR, OBTER_TODOS, OBTER_POR_ID, UPDATE, DELETE
from utils.db import open_connection


def CRIAR_TABELA () -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        conn.commit()
        return True


def INSERIR (cliente: Cliente) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            cliente.id,          
            cliente.genero,
            cliente.data_nascimento.isoformat()  
        ))
        conn.commit()
        return cursor.lastrowid


def OBTER_TODOS () -> List[Cliente]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
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
                cpf=row["cpf"],
                genero=row["genero"],
                data_nascimento=row["data_nascimento"]  
            ))
        return clientes


def OBTER_POR_ID (cliente_id: int) -> Optional[Cliente]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (cliente_id,))
        row = cursor.fetchone()
        if row:
            return Cliente(
                id=row["id"],
                nome=row["nome"],
                email=row["email"],
                senha=row["senha"],
                cpf_cnpj=row["cpf_cnpj"],
                telefone=row["telefone"],
                data_cadastro=row["data_cadastro"],
                endereco=row["endereco"],
                cpf=row["cpf"],
                genero=row["genero"],
                data_nascimento=row["data_nascimento"]
            )
        return None


def UPDATE (cliente: Cliente) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(UPDATE, (
            cliente.id,           
            cliente.genero,
            cliente.data_nascimento.isoformat(),
            cliente.id          
        ))
        conn.commit()
        return cursor.rowcount > 0


def DELETE (cliente_id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(DELETE, (cliente_id,))
        conn.commit()
        return cursor.rowcount > 0
