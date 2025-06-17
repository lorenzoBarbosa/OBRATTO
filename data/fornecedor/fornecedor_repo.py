from typing import Optional, List
from data.fornecedor.fornecedor_model import Fornecedor
from data.fornecedor.fornecedor_sql import CRIAR_TABELA, INSERIR, OBTER_TODOS, OBTER_POR_ID, UPDATE, DELETE
from utils.db import open_connection  
def criar_tabela() -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        conn.commit()
        return True


def inserir(fornecedor: Fornecedor) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            fornecedor.id_usuario,
            fornecedor.razao_social
        ))
        conn.commit()
        return cursor.lastrowid


def obter_todos() -> List[Fornecedor]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        fornecedores = [
            Fornecedor(
                id=row["id"],
                id_usuario=row["id_usuario"],
                razao_social=row["razao_social"]
            )
            for row in rows
        ]
        return fornecedores


def obter_por_id(fornecedor_id: int) -> Optional[Fornecedor]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (fornecedor_id,))
        row = cursor.fetchone()
        if row:
            return Fornecedor(
                id=row["id"],
                id_usuario=row["id_usuario"],
                razao_social=row["razao_social"]
            )
        return None


def atualizar(fornecedor: Fornecedor) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(UPDATE, (
            fornecedor.id_usuario,
            fornecedor.razao_social,
            fornecedor.id
        ))
        conn.commit()
        return cursor.rowcount > 0


def deletar(fornecedor_id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(DELETE, (fornecedor_id,))
        conn.commit()
        return cursor.rowcount > 0
