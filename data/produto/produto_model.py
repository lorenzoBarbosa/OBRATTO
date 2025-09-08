from dataclasses import dataclass
from typing import Optional
import datetime


@dataclass
class Produto:
    id: Optional[int]
    nome: str
    descricao: str
    preco: float
    quantidade: int
    em_promocao: bool = False
    desconto: float = 0.0
