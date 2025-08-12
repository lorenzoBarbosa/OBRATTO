"""
Modelo para pagamentos
"""
from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Pagamento:
    id_pagamento: Optional[int] = None
    plano_id: int = 0
    fornecedor_id: int = 0
    mp_payment_id: Optional[str] = None
    mp_preference_id: Optional[str] = None
    valor: float = 0.0
    status: str = "pendente"  # pendente, aprovado, rejeitado, cancelado
    metodo_pagamento: Optional[str] = None
    data_criacao: Optional[str] = None
    data_aprovacao: Optional[str] = None
    external_reference: Optional[str] = None
    
    def __post_init__(self):
        if self.data_criacao is None:
            self.data_criacao = datetime.now().isoformat()
