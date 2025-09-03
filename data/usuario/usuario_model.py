from dataclasses import dataclass
import datetime
from sqlite3.dbapi2 import Timestamp


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


