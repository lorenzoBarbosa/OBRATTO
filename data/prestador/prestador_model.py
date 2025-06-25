from dataclasses import dataclass
from data.usuario.usuario_model import Usuario


@dataclass
class Prestador(Usuario):
    area_atuacao: str
    tipo_pessoa: str  # 'Física' ou 'Jurídica'
    razao_social: str = None
    descricao_servicos: str = None
    

