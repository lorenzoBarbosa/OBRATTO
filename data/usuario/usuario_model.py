from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Usuario:
    id: Optional[int]
    nome: str
    email: str
    senha: str
    cpf_cnpj: str
    telefone: str
    data_cadastro: str
    endereco: str

