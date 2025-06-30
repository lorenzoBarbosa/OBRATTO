from typing import Optional, List
from data.prestador.prestador_model import Prestador, PrestadorInfoCompleta
from data.prestador.prestador_sql import (CRIAR_TABELA_PRESTADOR, INSERIR_PRESTADOR, OBTER_PRESTADOR, OBTER_PRESTADOR_POR_ID, ATUALIZAR_PRESTADOR, DELETAR_PRESTADOR)
from utils.db import open_connection


def criar_tabela_prestador() -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_PRESTADOR)
        conn.commit()
        return True

def inserir_prestador(prestador: Prestador) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_PRESTADOR, (
            prestador.id_usuario,
            prestador.area_atuacao,
            prestador.tipo_pessoa,
            prestador.razao_social,
            prestador.descricao_servicos
        ))
        conn.commit()
        return cursor.lastrowid


def obter_prestador() -> List[PrestadorInfoCompleta]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_PRESTADOR)
        rows = cursor.fetchall()
        return [
            PrestadorInfoCompleta(
                id_usuario=row["id_usuario"],
                nome=row["nome"],
                email=row["email"],
                telefone=row["telefone"],
                area_atuacao=row["area_atuacao"],
                tipo_pessoa=row["tipo_pessoa"],
                razao_social=row["razao_social"],
                descricao_servicos=row["descricao_servicos"]
            ) for row in rows
        ]


def obter_prestador_por_id(prestador_id: int) -> Optional[Prestador]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_PRESTADOR_POR_ID, (prestador_id,))
        row = cursor.fetchone()
        if row:
            return Prestador(
                id=row["id"],
                nome=row["nome"],
                email=row["email"],
                senha=row["senha"],
                cpf_cnpj=row["cpf_cnpj"],
                telefone=row["telefone"],
                data_cadastro=row["data_cadastro"],
                endereco=row["endereco"],
                area_atuacao=row["area_atuacao"],
                tipo_pessoa=row["tipo_pessoa"],
                razao_social=row["razao_social"],
                descricao_servicos=row["descricao_servicos"]
            )
        return None


def atualizar_prestador(prestador: Prestador) -> bool:
    """
    Atualiza apenas dados específicos do prestador.
    Dados do usuário são atualizados no repositório usuario.
    """
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_PRESTADOR,(
            prestador.area_atuacao,
            prestador.tipo_pessoa,
            prestador.razao_social,
            prestador.descricao_servicos,
            prestador.id
        ))
        conn.commit()
        return cursor.rowcount > 0


def deletar_prestador(prestador_id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(DELETAR_PRESTADOR, (prestador_id,))
        conn.commit()
        return cursor.rowcount > 0
