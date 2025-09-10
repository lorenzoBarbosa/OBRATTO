from dataclasses import dataclass
from typing import Optional
from data.usuario.usuario_model import Usuario


@dataclass
class Fornecedor(Usuario):
    razao_social: Optional[str] = None