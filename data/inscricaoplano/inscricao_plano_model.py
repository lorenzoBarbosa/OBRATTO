from dataclasses import dataclass
from typing import Optional

@dataclass
class InscricaoPlano:
    id_plano: int = 0
    id_inscricao_plano: Optional[int] = None
    id_fornecedor: Optional[int] = None
    id_prestador: Optional[int] = None
