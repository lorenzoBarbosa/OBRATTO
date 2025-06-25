from dataclasses import dataclass
import datetime


@dataclass
class Usuario:
    id: int 
    nome: str
    email: str
    senha: str
    cpf_cnpj: str
    telefone: str
    data_cadastro: datetime
    endereco: str


    