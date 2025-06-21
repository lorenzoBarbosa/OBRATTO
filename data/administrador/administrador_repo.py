from typing import Optional, List
from data.administrador.administrador_model import Administrador
from data.administrador.administrador_sql import CRIAR_TABELA_ADMINISTRADOR, INSERIR_ADMINISTRADOR, OBTER_TODOS_ADMINISTRADORES, OBTER_ADMINISTRADOR_POR_ID, ATUALIZAR_ADMINISTRADOR, DELETAR_ADMINISTRADOR
from utils.db import open_connection


def criar_tabela_administrador() -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_ADMINISTRADOR)
        conn.commit()
        return True


def inserir_administrador(administrador: Administrador) -> Optional[int]:
    """
    Insere um administrador com o id_usuario já existente.
    """
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_ADMINISTRADOR, (administrador.id_usuario,))
        conn.commit()
        return cursor.lastrowid


def obter_todos_administradores() -> List[Administrador]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_ADMINISTRADORES)
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


def obter_administrador_por_id(administrador_id: int) -> Optional[Administrador]:                 # TA CERTO? 
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_ADMINISTRADOR_POR_ID, (administrador_id,))
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


def atualizar_administrador(administrador: Administrador) -> bool:
    """
    Atualiza apenas o id_usuario do administrador.
    """
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_ADMINISTRADOR, (
            administrador.id_usuario,
            administrador.id
        ))
        conn.commit()
        return cursor.rowcount > 0


def deletar_administrador(administrador_id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(DELETAR_ADMINISTRADOR, (administrador_id,))
        conn.commit()
        return cursor.rowcount > 0
