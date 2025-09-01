from dataclasses import dataclass
from typing import Optional
from data.usuario.usuario_model import Usuario


@dataclass
class Prestador(Usuario):
    area_atuacao: str
    tipo_pessoa: str
    razao_social: str
    descricao_servicos: str

