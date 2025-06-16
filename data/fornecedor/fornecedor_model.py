from dataclasses import dataclass
from data.usuario.usuario_model import Usuario


@dataclass
class Fornecedor(Usuario):
    razao_social: str
    

