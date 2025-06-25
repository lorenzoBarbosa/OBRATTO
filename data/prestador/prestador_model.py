from dataclasses import dataclass
from typing import Optional
from data.usuario.usuario_model import Usuario


@dataclass
class Prestador(Usuario):
    area_atuacao: str           # obrigatório
    tipo_pessoa: str            # obrigatório
    razao_social: Optional[str] = None   # opcional
    descricao_servicos: Optional[str] = None  # opcional

