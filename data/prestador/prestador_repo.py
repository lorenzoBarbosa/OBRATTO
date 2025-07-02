from datetime import datetime
import sqlite3
from typing import Optional, List
from data.prestador.prestador_model import Prestador
from data.prestador.prestador_sql import (CRIAR_TABELA_PRESTADOR, INSERIR_PRESTADOR, OBTER_PRESTADOR, OBTER_PRESTADOR_POR_ID, ATUALIZAR_PRESTADOR, DELETAR_PRESTADOR, OBTER_PRESTADOR_POR_PAGINA)
from data.usuario.usuario_repo import atualizar_usuario, deletar_usuario, inserir_usuario
from utils.db import open_connection


def criar_tabela_prestador():
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_PRESTADOR)
        conn.commit()

def inserir_prestador(prestador: Prestador) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        id_usuario_gerado = inserir_usuario(prestador)
        if id_usuario_gerado:
            cursor.execute(INSERIR_PRESTADOR, (
                id_usuario_gerado,
                prestador.area_atuacao,
                prestador.tipo_pessoa,
                prestador.razao_social,
                prestador.descricao_servicos
            ))
            conn.commit()
            return id_usuario_gerado
        return None

def obter_prestador() -> List[Prestador]:
    with open_connection() as conn:
        conn.row_factory = lambda cursor, row: {col[0]: row[idx] for idx, col in enumerate(cursor.description)}
        cursor = conn.cursor()
        cursor.execute(OBTER_PRESTADOR)
        rows = cursor.fetchall()
        prestadores = []
        for row in rows:
            prestadores.append(Prestador(**row))
        return prestadores

def obter_prestador_por_id(prestador_id: int) -> Optional[Prestador]:
    with open_connection() as conn:
        conn.row_factory = lambda cursor, row: {col[0]: row[idx] for idx, col in enumerate(cursor.description)}
        cursor = conn.cursor()
        cursor.execute(OBTER_PRESTADOR_POR_ID, (prestador_id,))
        row = cursor.fetchone()
        if row:
            if isinstance(row.get("data_cadastro"), str):
                row["data_cadastro"] = datetime.fromisoformat(row["data_cadastro"])
            return Prestador(**row)
        return None
    
def obter_prestador_por_pagina(conn, limit: int, offset: int) -> list[Prestador]:
    conn.row_factory = sqlite3.Row 
    cursor = conn.cursor()
    cursor.execute(OBTER_PRESTADOR_POR_PAGINA, (limit, offset))
    rows = cursor.fetchall()
    return [
        Prestador(
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
            descricao_servicos=row["descricao_servicos"],
            tipo_usuario=row["tipo_usuario"]
        )
        for row in rows
    ]

def atualizar_prestador(prestador: Prestador) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        atualizar_usuario(prestador)
        cursor.execute(ATUALIZAR_PRESTADOR, (
            prestador.area_atuacao,
            prestador.tipo_pessoa,
            prestador.razao_social,
            prestador.descricao_servicos,
            prestador.id
        ))
        conn.commit()
        return cursor.rowcount > 0

def deletar_prestador_repo(prestador_id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(DELETAR_PRESTADOR, (prestador_id,))
        rows_affected = cursor.rowcount
        conn.commit()
        if rows_affected > 0:
            deletar_usuario(prestador_id)
            
        return rows_affected > 0