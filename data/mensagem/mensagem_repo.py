from typing import Optional, List
from data.mensagem.mensagem_model import Mensagem
from data.mensagem.mensagem_sql import CRIAR_TABELA_MENSAGEM, INSERIR_MENSAGEM, OBTER_MENSAGEM, OBTER_MENSAGEM_POR_ID, ATUALIZAR_MENSAGEM, DELETAR_MENSAGEM
from utils.db import open_connection


def criar_tabela_mensagem() -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_MENSAGEM)
        conn.commit()
        return True


def inserir_mensagem(mensagem: Mensagem) -> Optional[int]:
    """
    Insere uma nova mensagem no banco.
    O id_remetente e id_destinatario devem existir na tabela usuario.
    """
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_MENSAGEM, (
            mensagem.id_remetente,
            mensagem.id_destinatario,
            mensagem.conteudo,
            mensagem.data_hora
        ))
        conn.commit()
        return cursor.lastrowid


def obter_mensagem() -> List[Mensagem]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_MENSAGEM)
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


def obter_mensagem_por_id(id_mensagem: int) -> Optional[Mensagem]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_MENSAGEM_POR_ID, (id_mensagem,))
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


def atualizar_mensagem(mensagem: Mensagem) -> bool:
    """
    Atualiza dados da tabela mensagem.
    """
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_MENSAGEM, (
            mensagem.id_remetente,
            mensagem.id_destinatario,
            mensagem.conteudo,
            mensagem.data_hora,
            mensagem.id_mensagem
        ))
        conn.commit()
        return cursor.rowcount > 0


def deletar_mensagem(id_mensagem: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(DELETAR_MENSAGEM, (id_mensagem,))
        conn.commit()
        return cursor.rowcount > 0
