import datetime
from utils.db import open_connection
from typing import List, Optional
from data.usuario.usuario_model import Usuario
from data.usuario.usuario_sql import CRIAR_TABELA, INSERIR, OBTER_TODOS
from data.usuario.usuario_model import Usuario
from data.usuario.usuario_sql import *


def CRIAR_TABELA() -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        conn.commit()
        return True


def INSERIR (usuario: Usuario) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            usuario.nome,
            usuario.email,
            usuario.senha,
            usuario.cpf_cnpj,
            usuario.telefone,
            usuario.data_cadastro.isoformat() if isinstance(usuario.data_cadastro, (datetime.date, datetime.datetime)) else usuario.data_cadastro,
            usuario.endereco,
            usuario.cpf
        ))
        conn.commit()
        return cursor.lastrowid


def OBTER_TODOS() -> List[Usuario]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        usuarios = []
        for row in rows:
            usuarios.append(Usuario(
                id=row["id"],
                nome=row["nome"],
                email=row["email"],
                senha=row["senha"],
                cpf_cnpj=row["cpf_cnpj"],
                telefone=row["telefone"],
                data_cadastro=row["data_cadastro"],
                endereco=row["endereco"],
                cpf=row["cpf"]
            ))
        return usuarios


def OBTER_POR_ID (usuario_id: int) -> Optional[Usuario]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_POR_ID, (usuario_id,))
        row = cursor.fetchone()
        if row:
            return Usuario(
                id=row["id"],
                nome=row["nome"],
                email=row["email"],
                senha=row["senha"],
                cpf_cnpj=row["cpf_cnpj"],
                telefone=row["telefone"],
                data_cadastro=row["data_cadastro"],
                endereco=row["endereco"],
                cpf=row["cpf"]
            )
        return None


def UPDATE (usuario: Usuario) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(UPDATE, (
            usuario.nome,
            usuario.email,
            usuario.senha,
            usuario.cpf_cnpj,
            usuario.telefone,
            usuario.data_cadastro.isoformat() if isinstance(usuario.data_cadastro, (datetime.date, datetime.datetime)) else usuario.data_cadastro,
            usuario.endereco,
            usuario.cpf,
            usuario.id
        ))
        conn.commit()
        return cursor.rowcount > 0


def DELETE(usuario_id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(DELETE, (usuario_id,))
        conn.commit()
        return cursor.rowcount > 0