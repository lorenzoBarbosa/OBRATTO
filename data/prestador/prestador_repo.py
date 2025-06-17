from typing import Optional, List
from data.prestador.prestador_model import Prestador
from data.prestador.prestador_sql import CRIAR_TABELA, INSERIR, OBTER_TODOS, OBTER_POR_ID, UPDATE, DELETE
from utils.db import open_connection  


def criar_tabela() -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        conn.commit()
        return True 

def inserir(prestador: Prestador) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            prestador.id_usuario,
            prestador.area_atuacao,
            prestador.tipo_pessoa,
            prestador.razao_social,
            prestador.descricao_servicos
        ))
        conn.commit()
        return cursor.lastrowid


def obter_todos() -> List[Prestador]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        prestadores = [
            Prestador(
                id=row["id"],
                id_usuario=row["id_usuario"],
                area_atuacao=row["area_atuacao"],
                tipo_pessoa=row["tipo_pessoa"],
                razao_social=row["razao_social"],
                descricao_servicos=row["descricao_servicos"]
            )
            for row in rows
        ]
        return prestadores


def obter_por_id(prestador_id: int) -> Optional[Prestador]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (prestador_id,))
        row = cursor.fetchone()
        if row:
            return Prestador(
                id=row["id"],
                id_usuario=row["id_usuario"],
                area_atuacao=row["area_atuacao"],
                tipo_pessoa=row["tipo_pessoa"],
                razao_social=row["razao_social"],
                descricao_servicos=row["descricao_servicos"]
            )
        return None


def atualizar(prestador: Prestador) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(UPDATE, (
            prestador.id_usuario,
            prestador.area_atuacao,
            prestador.tipo_pessoa,
            prestador.razao_social,
            prestador.descricao_servicos,
            prestador.id
        ))
        conn.commit()
        return cursor.rowcount > 0


def deletar(prestador_id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(DELETE, (prestador_id,))
        conn.commit()
        return cursor.rowcount > 0
