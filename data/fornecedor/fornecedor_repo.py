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
    """
    Insere dados específicos do fornecedor.
    O id_usuario deve existir na tabela usuario.
    """
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            fornecedor.id_usuario,
            fornecedor.razao_social,
            fornecedor.cnpj,
            fornecedor.telefone_contato,
            fornecedor.endereco,
        ))
        conn.commit()
        return cursor.lastrowid


def obter_todos() -> List[Fornecedor]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        fornecedores = []
        for row in rows:
            fornecedores.append(Fornecedor(
                id=row["id"],
                id_usuario=row["id_usuario"],
                nome=row.get("nome"),
                email=row.get("email"),
                senha=None,
                cpf_cnpj=None,
                telefone=None,
                data_cadastro=None,
                endereco=row.get("endereco"),
                cnpj=row.get("cnpj"),
                razao_social=row.get("razao_social"),
                telefone_contato=row.get("telefone_contato")
            ))
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
                nome=row.get("nome"),
                email=row.get("email"),
                senha=None,
                cpf_cnpj=None,
                telefone=None,
                data_cadastro=None,
                endereco=row.get("endereco"),
                cnpj=row.get("cnpj"),
                razao_social=row.get("razao_social"),
                telefone_contato=row.get("telefone_contato")
            )
        return None


def atualizar(fornecedor: Fornecedor) -> bool:
    """
    Atualiza dados da tabela fornecedor.
    """
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(UPDATE, (
            fornecedor.id_usuario,
            fornecedor.razao_social,
            fornecedor.cnpj,
            fornecedor.telefone_contato,
            fornecedor.endereco,
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
