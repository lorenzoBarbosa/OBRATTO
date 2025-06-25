from dataclasses import dataclass
from data.servico.servico_model import Servico
from typing import Optional

@dataclass
class Servico:
    id_servico: int
    id_prestador: int
    titulo: str
    descricao: str
    categoria: str
    valor_base: float
    nome_prestador: Optional[str] = None
    