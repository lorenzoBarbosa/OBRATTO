from dataclasses import dataclass
from typing import Optional
import datetime
from data.usuario.usuario_model import Usuario


@dataclass
class Cliente(Usuario):
    id_usuario: Optional[int] = None
    genero: Optional[str] = None
    data_nascimento: Optional[datetime.date] = None
