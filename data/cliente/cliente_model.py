from dataclasses import dataclass
from datetime import date
from data.usuario.usuario_model import Usuario

@dataclass
class Cliente(Usuario):
    genero: str
    data_nascimento: date