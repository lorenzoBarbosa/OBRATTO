from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Avaliacao:
    id_avaliacao: int
    id_avaliador: int
    id_avaliado: int
    nota: float
    data_avaliacao: datetime
    descricao: str
    nome_avaliador: Optional[str] = None
    nome_avaliado: Optional[str] = None