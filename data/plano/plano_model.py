from dataclasses import dataclass
from typing import Optional

@dataclass
class Plano:
    id_plano: Optional[int] = None
    nome_plano: Optional[str] = None
    valor_mensal: Optional[float] = None
    limite_servico: Optional[int] = None
    tipo_plano: Optional[str] = None
    descricao: Optional[str] = None

