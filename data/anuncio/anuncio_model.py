from dataclasses import dataclass
from datetime import datetime
from data.fornecedor.fornecedor_model import Fornecedor

@dataclass
class Anuncio:
    id_anuncio: int
    nome_anuncio: str
    id_fornecedor: Fornecedor
    data_criacao: datetime
    descricao: str
    preco: float
