from typing import Optional, List
from data.orcamento.orcamento_model import Orcamento  
from data.orcamento.orcamento_sql import *
from utils.db import open_connection


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
            orcamento["id_fornecedor"],
            orcamento["id_cliente"],
            orcamento["valor_estimado"],
            orcamento["data_solicitacao"],
            orcamento["prazo_entrega"],
            orcamento["status"],
            orcamento["descricao"]
        ))
        conn.commit()
        return cursor.lastrowid


def obter_todos_os_orcamento() -> List[Orcamento]:  
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_OS_ORCAMENTOS)
        rows = cursor.fetchall()
        orcamentos = []
        for row in rows:
            orcamentos.append(Orcamento(
                id=row["id"],
                id_fornecedor=row["id_fornecedor"],
                id_cliente=row["id_cliente"],
                valor_estimado=row["valor_estimado"],
                data_solicitacao=row["data_solicitacao"],
                prazo_entrega=row["prazo_entrega"],
                status=row["status"],
                descricao=row["descricao"],
            ))
        return orcamentos


def obter_orcamento_por_valor_estimado(valor: float) -> Optional[List[Orcamento]]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_ORCAMENTO_POR_VALOR_ESTIMADO, (valor,))
        rows = cursor.fetchall()
        if rows:
            return [Orcamento(
                id=row["id"],
                id_fornecedor=row["id_fornecedor"],
                id_cliente=row["id_cliente"],
                valor_estimado=row["valor_estimado"],
                data_solicitacao=row["data_solicitacao"],
                prazo_entrega=row["prazo_entrega"],
                status=row["status"],
                descricao=row["descricao"],
            ) for row in rows]
        return None


def obter_orcamento_por_id(orcamento_id: int) -> Optional[Orcamento]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_ORCAMENTO_POR_ID, (orcamento_id,))
        row = cursor.fetchone()
        if row:
            return Orcamento(
                id=row["id"],
                id_fornecedor=row["id_fornecedor"],
                id_cliente=row["id_cliente"],
                valor_estimado=row["valor_estimado"],
                data_solicitacao=row["data_solicitacao"],
                prazo_entrega=row["prazo_entrega"],
                status=row["status"],
                descricao=row["descricao"],
            )
        return None


def atualizar_orcamento_por_id(orcamento: Orcamento) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_ORCAMENTO_POR_ID, (
            orcamento["id_fornecedor"],
            orcamento["id_cliente"],
            orcamento["valor_estimado"],
            orcamento["data_solicitacao"],
            orcamento["prazo_entrega"],
            orcamento["status"],
            orcamento["descricao"]
        ))
        conn.commit()
        return cursor.rowcount > 0


def deletar_orcamento(id_orcamento: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(DELETAR_ORCAMENTO, (id_orcamento,))
        conn.commit()
        return cursor.rowcount > 0
