from typing import Optional, List
from data.usuario.usuario_model import Usuario
from data.usuario.usuario_sql import ATUALIZAR_SENHA_USUARIO, CRIAR_TABELA_USUARIO, INSERIR_USUARIO, OBTER_USUARIO, OBTER_USUARIO_POR_ID, ATUALIZAR_USUARIO, DELETAR_USUARIO
from utils.db import open_connection


def criar_tabela_usuario() -> bool:
    try:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CRIAR_TABELA_USUARIO)
            return True
    except Exception as e:
        print(f"Erro ao criar tabela de usuário: {e}")
        conn.commit()
        return True


def inserir_usuario(usuario: Usuario) -> Optional[int]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR_USUARIO,(
            usuario["nome"],
            usuario["email"],
            usuario["senha"],
            usuario["cpf_cnpj"],
            usuario["telefone"],
            usuario["data_cadastro"],
            usuario["endereco"]
        ))
        conn.commit()
        return cursor.lastrowid


def obter_usuario() -> List[Usuario]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_USUARIO)
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
                endereco=row["endereco"]
            ))
        return usuarios


def obter_usuario_por_id(usuario_id: int) -> Optional[Usuario]:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_USUARIO_POR_ID, (usuario_id,))
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
                endereco=row["endereco"]
            )
        return None


def atualizar_usuario(usuario: Usuario) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_USUARIO, (
            usuario["nome"],
            usuario["email"],
            usuario["senha"],
            usuario["cpf_cnpj"],
            usuario["telefone"],
            usuario["data_cadastro"],
            usuario["endereco"]
        ))
        conn.commit()
        return cursor.rowcount > 0


def atualizar_senha_usuario(usuario_id: int, nova_senha: str) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_SENHA_USUARIO, (nova_senha, usuario_id))
        conn.commit()
        return cursor.rowcount > 0



def deletar_usuario(usuario_id: int) -> bool:
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(DELETAR_USUARIO, (usuario_id,))
        conn.commit()
        return cursor.rowcount > 0
