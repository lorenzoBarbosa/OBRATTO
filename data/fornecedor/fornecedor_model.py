from dataclasses import dataclass
from data.usuario.usuario_model import Usuario


@dataclass(kw_only=True)
class Fornecedor(Usuario):
    razao_social: str
