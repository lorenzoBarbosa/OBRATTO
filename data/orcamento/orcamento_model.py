from dataclasses import dataclass
from typing import Optional
import datetime

@dataclass
class Orcamento:
    id_fornecedor: int
    id_cliente: int
    valor_estimado: float
    data_solicitacao: datetime.datetime
    prazo_entrega: datetime.datetime
    status: str
    descricao: str
    id: Optional[int] = None  # campo opcional deve vir por último
