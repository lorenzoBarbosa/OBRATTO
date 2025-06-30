from dataclasses import dataclass
import datetime
from data.usuario.usuario_model import Usuario


@dataclass
class Cliente:
    id: int
    id_usuario: int
    genero: str
    data_nascimento: datetime.date


    