from typing import Optional, List
from data.orcamento.orcamento_model import Orcamento
from data.orcamento.orcamento_sql import *
from utils.db import open_connection
import datetime


def criar_tabela_orcamento() -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_ORCAMENTO)
        conn.commit()
        return True


def inserir_orcamento(orcamento: Orcamento) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_ORCAMENTO, (
            orcamento.id_fornecedor,
            orcamento.id_cliente,
            orcamento.valor_estimado,
            orcamento.data_solicitacao.isoformat(),
            orcamento.prazo_entrega.isoformat(),
            orcamento.status,
            orcamento.descricao
        ))
        conn.commit()
        return cursor.lastrowid


def obter_orcamento_por_id(orcamento_id: int) -> Optional[Orcamento]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_ORCAMENTO_POR_ID, (orcamento_id,))
        row = cursor.fetchone()
        if row:
            return Orcamento(
                id_orcamento=row["id_orcamento"],
                id_fornecedor=row["id_fornecedor"],
                id_cliente=row["id_cliente"],
                valor_estimado=row["valor_estimado"],
                data_solicitacao=datetime.datetime.fromisoformat(row["data_solicitacao"]),
                prazo_entrega=datetime.datetime.fromisoformat(row["prazo_entrega"]),
                status=row["status"],
                descricao=row["descricao"]
            )
        return None


def obter_todos_orcamentos() -> List[Orcamento]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_ORCAMENTOS)
        rows = cursor.fetchall()
        return [
            Orcamento(
                id_orcamento=row["id_orcamento"],
                id_fornecedor=row["id_fornecedor"],
                id_cliente=row["id_cliente"],
                valor_estimado=row["valor_estimado"],
                data_solicitacao=datetime.datetime.fromisoformat(row["data_solicitacao"]),
                prazo_entrega=datetime.datetime.fromisoformat(row["prazo_entrega"]),
                status=row["status"],
                descricao=row["descricao"]
            ) for row in rows
        ]


def atualizar_orcamento_por_id(id: int, orcamento: Orcamento) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_ORCAMENTO_POR_ID, (
            orcamento.id_fornecedor,
            orcamento.id_cliente,
            orcamento.valor_estimado,
            orcamento.data_solicitacao.isoformat(),
            orcamento.prazo_entrega.isoformat(),
            orcamento.status,
            orcamento.descricao,
            id
        ))
        conn.commit()
        return cursor.rowcount > 0


def deletar_orcamento(id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(DELETAR_ORCAMENTO, (id,))
        conn.commit()
        return cursor.rowcount > 0
