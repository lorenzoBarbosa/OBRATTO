from dataclasses import dataclass
from data.fornecedor.fornecedor_model import Fornecedor

@dataclass
class Anuncio:
    id_anuncio: int
    nome_anuncio: str
    id_fornecedor: Fornecedor
    data_criacao: str
    descricao: str
    preco: float
