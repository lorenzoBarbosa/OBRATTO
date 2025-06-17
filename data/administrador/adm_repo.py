from typing import Optional, List
from data.administrador.adm_model import Administrador
from data.administrador.adm_sql import CRIAR_TABELA, INSERIR, OBTER_TODOS, OBTER_POR_ID, UPDATE, DELETE
from utils.db import open_connection


def criar_tabela() -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        conn.commit()
        return True


def inserir(administrador: Administrador) -> Optional[int]:
    """
    Insere um administrador com o id_usuario já existente.
    """
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            administrador.id_usuario,
        ))
        conn.commit()
        return cursor.lastrowid


def obter_todos() -> List[Administrador]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        administradores = []
        for row in rows:
            administradores.append(Administrador(
                id=row["id"],
                id_usuario=row["id_usuario"],
                nome=row.get("nome"),          
                email=row.get("email"),
                senha=None,
                cpf_cnpj=None,
                telefone=None,
                data_cadastro=None,
                endereco=None,
                cpf=None
            ))
        return administradores


def obter_por_id(administrador_id: int) -> Optional[Administrador]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (administrador_id,))
        row = cursor.fetchone()
        if row:
            return Administrador(
                id=row["id"],
                id_usuario=row["id_usuario"],
                nome=row.get("nome"),
                email=row.get("email"),
                senha=None,
                cpf_cnpj=None,
                telefone=None,
                data_cadastro=None,
                endereco=None,
                cpf=None
            )
        return None


def atualizar(administrador: Administrador) -> bool:
    """
    Atualiza apenas o id_usuario do administrador.
    """
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(UPDATE, (
            administrador.id_usuario,
            administrador.id
        ))
        conn.commit()
        return cursor.rowcount > 0


def deletar(administrador_id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(DELETE, (administrador_id,))
        conn.commit()
        return cursor.rowcount > 0
