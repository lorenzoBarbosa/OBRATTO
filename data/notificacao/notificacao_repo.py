from typing import Optional, List
from data.notificacao.notificacao_model import Notificacao
from data.notificacao.notificacao_sql import CRIAR_TABELA, INSERIR, OBTER_TODOS, OBTER_POR_ID, UPDATE, DELETE
from utils.db import open_connection


def criar_tabela() -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        conn.commit()
        return True


def inserir(notificacao: Notificacao) -> Optional[int]:
    """
    Insere uma nova Notificacao no banco.
    O id_usuario deve existir na tabela usuario.
    """
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            notificacao.id_usuario,
            notificacao.mensagem,
            notificacao.data_hora,
            notificacao.tipo_notificacao,
            int(notificacao.vizualizar)
        ))
        conn.commit()
        return cursor.lastrowid


def obter_todos() -> List[Notificacao]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        notificacoes = []
        for row in rows:
            notificacoes.append(Notificacao(
                id_notificacao=row["id_notificacao"],
                id_usuario=row["id_usuario"],
                mensagem=row["mensagem"],
                data_hora=row["data_hora"],
                tipo_notificacao= row["tipo_notificacao"],
                visualizar=bool(row["vizualizar"])
            ))
        return notificacoes


def obter_por_id(id_notificacao: int) -> Optional[Notificacao]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id_notificacao,))
        row = cursor.fetchone()
        if row:
            return Notificacao(
                id_notificacao=row["id_notificacao"],
                id_usuario=row["id_usuario"],
                mensagem=row["mensagem"],
                data_hora=row["data_hora"],
                tipo_notificacao= row["tipo_notificacao"],
                visualizar=bool(row["vizualizar"])
            )
        return None


def atualizar(notificacao: Notificacao) -> bool:
    """
    Atualiza dados da tabela notificacao.
    """
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(UPDATE, (
            notificacao.id_usuario,
            notificacao.mensagem,
            notificacao.data_hora,
            notificacao.tipo_notificacao,
            int(notificacao.vizualizar),
            notificacao.id_notificacao
        ))
        conn.commit()
        return cursor.rowcount > 0


def deletar(id_notificacao: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(DELETE, (id_notificacao,))
        conn.commit()
        return cursor.rowcount > 0




