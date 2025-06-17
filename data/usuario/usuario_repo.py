from typing import Optional, List
from data.usuario.usuario_model import Usuario
from data.usuario.usuario_sql import CRIAR_TABELA, INSERIR, OBTER_TODOS, OBTER_POR_ID, UPDATE, DELETE
from utils.db import open_connection


def criar_tabela() -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        conn.commit()
        return True


def inserir(usuario: Usuario) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            usuario.nome,
            usuario.email,
            usuario.senha,
            usuario.cpf_cnpj,
            usuario.telefone,
            usuario.data_cadastro,
            usuario.endereco,
            usuario.cpf
        ))
        conn.commit()
        return cursor.lastrowid


def obter_todos() -> List[Usuario]:
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


def obter_por_id(usuario_id: int) -> Optional[Usuario]:
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


def atualizar(usuario: Usuario) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(UPDATE, (
            usuario.nome,
            usuario.email,
            usuario.senha,
            usuario.cpf_cnpj,
            usuario.telefone,
            usuario.data_cadastro,
            usuario.endereco,
            usuario.cpf,
            usuario.id
        ))
        conn.commit()
        return cursor.rowcount > 0


def deletar(usuario_id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(DELETE, (usuario_id,))
        conn.commit()
        return cursor.rowcount > 0
