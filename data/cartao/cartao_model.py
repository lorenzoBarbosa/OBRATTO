from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class CartaoCredito:
    id_cartao: int
    id_fornecedor: int
    nome_titular: str
    numero_cartao_criptografado: str  # Apenas últimos 4 dígitos visíveis
    ultimos_4_digitos: str
    mes_vencimento: str
    ano_vencimento: str
    bandeira: str  # Visa, Mastercard, etc.
    apelido: str  # Ex: "Cartão Principal", "Cartão Empresarial"
    principal: bool  # Se é o cartão principal
    ativo: bool
    data_criacao: Optional[str] = None
    data_atualizacao: Optional[str] = None
    
    def __post_init__(self):
        if self.data_criacao is None:
            self.data_criacao = datetime.now().isoformat()
        if self.data_atualizacao is None:
            self.data_atualizacao = datetime.now().isoformat()
