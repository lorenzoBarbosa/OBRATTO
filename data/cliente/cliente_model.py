from dataclasses import dataclass
from datetime import date
from typing import Optional
from data.usuario.usuario_model import Usuario

@dataclass
class Cliente(Usuario):
    genero: Optional[str] = None
    data_nascimento: Optional[date] = None