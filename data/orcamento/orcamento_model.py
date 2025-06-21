from dataclasses import dataclass
import datetime


@dataclass
class Orcamento:
    id_forncedor: int
    id_cliente: int
    valor_estimado: float
    data_solicitação: datetime
    prazo_entrega: datetime
    status: str
    descricao: str
