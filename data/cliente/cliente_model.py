from dataclasses import dataclass
import datetime
from data.usuario.usuario_model import Usuario


@dataclass
class Cliente(Usuario):
    genero: str
    data_nascimento: datetime.date


    