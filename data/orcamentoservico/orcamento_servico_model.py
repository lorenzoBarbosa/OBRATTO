from dataclasses import dataclass
from typing import Optional
from datetime import date

@dataclass
class OrcamentoServico:
    id_orcamento: int
    id_servico: int
    id_prestador: int
    id_cliente: int
    valor_estimado: float
    data_solicitacao: date
    prazo_entrega: date
    status: str
    descricao: str
    nome_prestador: Optional[str] = None    
    nome_cliente: Optional[str] = None
    titulo_servico: Optional[str] = None
    