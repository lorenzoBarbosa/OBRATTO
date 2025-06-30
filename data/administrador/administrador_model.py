from dataclasses import dataclass
from data.usuario.usuario_model import Usuario

@dataclass
class Administrador:
    id: int
    id_usuario: int 