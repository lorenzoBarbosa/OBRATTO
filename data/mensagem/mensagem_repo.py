from typing import Optional, List
from data.mensagem.mensagem_model import Mensagem
from data.mensagem.mensagem_sql import CRIAR_TABELA, INSERIR, OBTER_TODOS, OBTER_POR_ID, UPDATE, DELETE
from utils.db import open_connection


def criar_tabela() -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        conn.commit()
        return True


def inserir(mensagem: Mensagem) -> Optional[int]:
    """
    Insere uma nova mensagem no banco.
    O id_remetente e id_destinatario devem existir na tabela usuario.
    """
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            mensagem.id_remetente,
            mensagem.id_destinatario,
            mensagem.conteudo,
            mensagem.data_hora
        ))
        conn.commit()
        return cursor.lastrowid


def obter_todos() -> List[Mensagem]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        mensagens = []
        for row in rows:
            mensagens.append(Mensagem(
                id_mensagem=row["id_mensagem"],
                nome_remetente=row["nome_remetente"],
                nome_destinatario=row["nome_destinatario"],
                conteudo=row["conteudo"],
                data_hora= row["data_hora"],
                nome_remetente=row["nome_remetente"],
                nome_destinatario=row["nome_destinatario"]
            ))
        return mensagens


def obter_por_id(id_mensagem: int) -> Optional[Mensagem]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (id_mensagem,))
        row = cursor.fetchone()
        if row:
            return Mensagem(
                id_mensagem=row["id_mensagem"],
                id_remetente=row["id_remetente"],
                id_destinatario=row["id_destinatario"],
                conteudo=row["conteudo"],
                data_hora= row["data_hora"],
                nome_remetente=row["nome_remetente"],
                nome_destinatario=row["nome_destinatario"]
            )
        return None


def atualizar(mensagem: Mensagem) -> bool:
    """
    Atualiza dados da tabela mensagem.
    """
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(UPDATE, (
            mensagem.id_remetente,
            mensagem.id_destinatario,
            mensagem.conteudo,
            mensagem.data_hora,
            mensagem.id_mensagem
        ))
        conn.commit()
        return cursor.rowcount > 0


def deletar(id_mensagem: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(DELETE, (id_mensagem,))
        conn.commit()
        return cursor.rowcount > 0
