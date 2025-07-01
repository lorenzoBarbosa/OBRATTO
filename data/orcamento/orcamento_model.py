from dataclasses import dataclass
import datetime
from typing import Optional


class Orcamento:
    id: Optional[int] = None        # campo id opcional para identificar o orçamento
    id_fornecedor: int
    id_cliente: int
    valor_estimado: float
    data_solicitacao: datetime.datetime
    prazo_entrega: datetime.datetime
    status: str
    descricao: str