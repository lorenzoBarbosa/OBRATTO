from datetime import datetime
from typing import Optional, List
from data.prestador.prestador_model import Prestador
from data.prestador.prestador_sql import (CRIAR_TABELA_PRESTADOR, INSERIR_PRESTADOR, OBTER_PRESTADOR, OBTER_PRESTADOR_POR_ID, ATUALIZAR_PRESTADOR, DELETAR_PRESTADOR)
from data.usuario.usuario_repo import atualizar_usuario, deletar_usuario, inserir_usuario
from utils.db import open_connection


def criar_tabela_prestador():
    """Cria a tabela 'prestador' no banco de dados, se não existir."""
    with open_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_PRESTADOR)
        conn.commit()

def inserir_prestador(prestador: Prestador) -> Optional[int]:
    """
    Insere um novo prestador no banco de dados.
    Primeiro insere na tabela 'usuario' para obter o ID, depois na tabela 'prestador'.
    """
    with open_connection() as conn:
        cursor = conn.cursor()
        
        # 1. Insere o registro na tabela base 'usuario'
        id_usuario_gerado = inserir_usuario(prestador)

        # 2. Se o usuário foi inserido com sucesso, insere na tabela 'prestador'
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
    """Retorna uma lista de todos os prestadores cadastrados."""
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
    """Busca um prestador pelo seu ID."""
    with open_connection() as conn:
        # Permite acessar os resultados da consulta pelo nome da coluna
        conn.row_factory = lambda cursor, row: {col[0]: row[idx] for idx, col in enumerate(cursor.description)}
        cursor = conn.cursor()
        cursor.execute(OBTER_PRESTADOR_POR_ID, (prestador_id,))
        row = cursor.fetchone()
        if row:
            # Converte a data de string para datetime se necessário
            if isinstance(row.get("data_cadastro"), str):
                row["data_cadastro"] = datetime.fromisoformat(row["data_cadastro"])
            return Prestador(**row)
        return None

def atualizar_prestador(prestador: Prestador) -> bool:
    """Atualiza os dados de um prestador no banco de dados."""
    with open_connection() as conn:
        cursor = conn.cursor()
        
        # 1. Atualiza os dados na tabela base 'usuario'
        atualizar_usuario(prestador)
        
        # 2. Atualiza os dados na tabela 'prestador'
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
    """
    Deleta um prestador do banco de dados.
    A deleção em cascata (ou a deleção manual do usuário) deve ser configurada no banco de dados
    ou tratada aqui.
    """
    with open_connection() as conn:
        cursor = conn.cursor()
        # Deleta da tabela 'prestador' primeiro para respeitar a chave estrangeira
        cursor.execute(DELETAR_PRESTADOR, (prestador_id,))
        rows_affected = cursor.rowcount
        conn.commit()

        # Depois deleta da tabela 'usuario'
        if rows_affected > 0:
            deletar_usuario(prestador_id)
            
        return rows_affected > 0