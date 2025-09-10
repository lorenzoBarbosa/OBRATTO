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
    endereco: str
    tipo_usuario: str
    data_cadastro: datetime
    foto: Optional[str]
    token_redefinicao: Optional[str]
    data_token: Optional[str]


