from typing import Optional
from data.usuario.usuario_model import Usuario
from data.usuario.usuario_sql import CRIAR_TABELA, INSERIR, OBTER_TODOS
from data.usuario.usuario_model import Usuario
from data.usuario.usuario_sql import *
from data.usuario.uti import get_connection

def criar_tabela() -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        return cursor.rowcount > 0
   

def inserir(usuario: Usuario) -> Optional[int]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            usuario.nome, 
            usuario.email,
            usuario.senha,
            usuario.cpf_cnpj,
            usuario.telefone,
            usuario.data_cadastro,
            usuario.endereco))
        return cursor.lastrowid
    

def obter_todos() -> list[Usuario]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        usuarios = [
            Usuario(
                id=row["id"], 
                nome=row["nome"], 
                email=row["email"],
                senha=row["senha"],
                cpf_cnpj=row["cpf_cnpj"],
                telefone=row["telefone"],
                data_cadastro=row["data_cadastro"],
                endereco=row["endereco"]) 
                for row in rows]
        return usuarios
