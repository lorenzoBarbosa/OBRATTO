from dataclasses import dataclass
from typing import Optional
import datetime


@dataclass
class Produto:
    id: int
    nome: str
    descricao: str
    preco: float
    quantidade: int
