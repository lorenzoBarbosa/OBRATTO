from typing import List, Optional
from data.servico.servico_model import Servico
from data.servico.servico_sql import CRIAR_TABELA, INSERIR, OBTER_TODOS, OBTER_POR_ID, UPDATE, DELETE
from utils.db import open_connection


def criar_tabela() -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        conn.commit()
        return True


def inserir(servico: Servico) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            servico.id_prestador,
            servico.titulo,
            servico.descricao,
            servico.categoria,
            servico.valor_base
        ))
        conn.commit()
        return cursor.lastrowid


def obter_todos() -> List[Servico]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        servicos = []
        for row in rows:
            servicos.append(Servico(
                id_servico=row["id_servico"],
                id_prestador=row["id_prestador"],
                titulo=row["titulo"],
                descricao=row["descricao"],
                categoria=row["categoria"],
                valor_base=row["valor_base"],
                nome_prestador=row["nome_prestador"]
            ))
        return servicos


def obter_por_id(id_servico: int) -> Optional[Servico]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id_servico,))
        row = cursor.fetchone()
        if row:
            return Servico(
                id_servico=row["id_servico"],
                id_prestador=row["id_prestador"],
                titulo=row["titulo"],
                descricao=row["descricao"],
                categoria=row["categoria"],
                valor_base=row["valor_base"],
                nome_prestador=row["nome_prestador"]
            )
        return None


def atualizar(servico:Servico) -> bool:
    """
    Atualiza dados da tabela servico.
    """
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(UPDATE, (
            servico.id_prestador,
            servico.titulo,
            servico.descricao,
            servico.categoria,
            servico.valor_base,
            servico.id_servico
        ))
        conn.commit()
        return cursor.rowcount > 0


def deletar(id_servico: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(DELETE, (id_servico,))
        conn.commit()
        return cursor.rowcount > 0
