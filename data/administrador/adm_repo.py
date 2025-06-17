from typing import Optional, List
from data.administrador.adm_model import Administrador
from data.administrador.adm_sql import CRIAR_TABELA, INSERIR, OBTER_TODOS, UPDATE, DELETE
from utils.db import open_connection


def CRIAR_TABELA () -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        conn.commit()
        return True


def INSERIR (administrador: Administrador) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            administrador.nome,
            administrador.email,
            administrador.senha,
            administrador.cpf_cnpj,
            administrador.telefone,
            administrador.data_cadastro,
            administrador.endereco,
            administrador.cpf
        ))
        conn.commit()
        return cursor.lastrowid


def OBTER_TODOS () -> List[Administrador]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        administradores = [
            Administrador(
                id=row["id"],
                nome=row["nome"],
                email=row["email"],
                senha=row["senha"],
                cpf_cnpj=row["cpf_cnpj"],
                telefone=row["telefone"],
                data_cadastro=row["data_cadastro"],
                endereco=row["endereco"],
                cpf=row["cpf"]
            )
            for row in rows
        ]
        return administradores


def UPDATE (administrador: Administrador) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(UPDATE, (
            administrador.id_usuario,
            administrador.id
        ))
        conn.commit()
        return cursor.rowcount > 0


def DELETE (administrador_id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(DELETE, (administrador_id,))
        conn.commit()
        return cursor.rowcount > 0
