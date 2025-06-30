from dataclasses import dataclass
from typing import Optional
from data.usuario.usuario_model import Usuario


@dataclass
class Prestador:
    id: int
    id_usuario: int
    area_atuacao: str
    tipo_pessoa: str
    razao_social: Optional[str] = None
    descricao_servicos: Optional[str] = None

class PrestadorInfoCompleta:
    id_usuario: int
    nome: str
    email: str
    telefone: str
    area_atuacao: str
    tipo_pessoa: str
    razao_social: Optional[str]
    descricao_servicos: Optional[str]

