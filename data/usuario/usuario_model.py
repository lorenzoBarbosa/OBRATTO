from dataclasses import dataclass
import datetime
from sqlite3.dbapi2 import Timestamp
from typing import Optional


@dataclass
class Usuario:
    id: int 
    nome: str
    email: str
    senha: str
    cpf_cnpj: str
    telefone: str
    data_cadastro:Timestamp
    endereco: str
    tipo_usuario: str
    foto: Optional[str] = None
    token_redefinicao: Optional[str] = None
    data_token: Optional[str] = None
    data_cadastro_str: Optional[str] = None


