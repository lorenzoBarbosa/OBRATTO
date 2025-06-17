from typing import Optional, List
from data.prestador.prestador_model import Prestador
from data.prestador.prestador_sql import CRIAR_TABELA, INSERIR, OBTER_TODOS, OBTER_POR_ID, UPDATE, DELETE
from utils.db import open_connection  


def CRIAR_TABELA () -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        conn.commit()
        return True 

def INSERIR(prestador: Prestador) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            prestador.area_atuacao,
            prestador.tipo_pessoa,
            prestador.razao_social,
            prestador.descricao_servicos
        ))
        conn.commit()
        return cursor.lastrowid


def OBTER_TODO () -> List[Prestador]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        prestadores = [
            Prestador(
                id=row["id"],
                area_atuacao=row["area_atuacao"],
                tipo_pessoa=row["tipo_pessoa"],
                razao_social=row["razao_social"],
                descricao_servicos=row["descricao_servicos"]
            )
            for row in rows
        ]
        return prestadores


def OBTER_POR_ID (prestador_id: int) -> Optional[Prestador]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (prestador_id,))
        row = cursor.fetchone()
        if row:
            return Prestador(
                id=row["id"],
                area_atuacao=row["area_atuacao"],
                tipo_pessoa=row["tipo_pessoa"],
                razao_social=row["razao_social"],
                descricao_servicos=row["descricao_servicos"]
            )
        return None


def UPDATE(prestador: Prestador) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(UPDATE, (
            prestador.area_atuacao,
            prestador.tipo_pessoa,
            prestador.razao_social,
            prestador.descricao_servicos,
            prestador.id
        ))
        conn.commit()
        return cursor.rowcount > 0


def DELETE (prestador_id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(DELETE, (prestador_id,))
        conn.commit()
        return cursor.rowcount > 0
