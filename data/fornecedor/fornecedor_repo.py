from typing import Optional, List
from data.fornecedor.fornecedor_model import Fornecedor
from data.fornecedor.fornecedor_sql import * 
from utils.db import open_connection


def criar_tabela_fornecedor() -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_FORNECEDOR)
        conn.commit()
        return True


def inserir_fornecedor(fornecedor: Fornecedor) -> Optional[int]:
    """
    Insere dados específicos do fornecedor.
    O id_usuario deve existir na tabela usuario.
    """
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_FORNECEDOR, (
            fornecedor.id_usuario,
            fornecedor.razao_social,
            fornecedor.cnpj,
            fornecedor.telefone_contato,
            fornecedor.endereco,
        ))
        conn.commit()
        return cursor.lastrowid


def obter_fornecedor() -> List[Fornecedor]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_FORNECEDOR)
        rows = cursor.fetchall()
        fornecedores = []
        for row in rows:
            fornecedores.append(Fornecedor(
                id=row["id"],
                id_usuario=row["id_usuario"],
                nome=row("nome"),
                email=row("email"),
                senha=None,
                cpf_cnpj=None,
                telefone=None,
                data_cadastro=None,
                endereco=row("endereco"),
                cnpj=row("cnpj"),
                razao_social=row("razao_social"),
                telefone_contato=row("telefone_contato")
            ))
        return fornecedores


def obter_fornecedor_por_id(fornecedor_id: int) -> Optional[Fornecedor]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_FORNECEDOR_POR_ID, (fornecedor_id,))
        row = cursor.fetchone()
        if row:
            return Fornecedor(
                id=row["id"],
                id_usuario=row["id_usuario"],
                nome=row("nome"),
                email=row("email"),
                senha=None,
                cpf_cnpj=None,
                telefone=None,
                data_cadastro=None,
                endereco=row("endereco"),
                cnpj=row("cnpj"),
                razao_social=row("razao_social"),
                telefone_contato=row("telefone_contato")
            )
        return None


def atualizar_fornecedor(fornecedor: Fornecedor) -> bool:
    """
    Atualiza dados da tabela fornecedor.
    """
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_FORNECEDOR, (
            fornecedor.id_usuario,
            fornecedor.razao_social,
            fornecedor.cnpj,
            fornecedor.telefone_contato,
            fornecedor.endereco,
            fornecedor.id
        ))
        conn.commit()
        return cursor.rowcount > 0


def deletar_fornecedor(fornecedor_id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(DELETAR_FORNECEDOR, (fornecedor_id,))
        conn.commit()
        return cursor.rowcount > 0
