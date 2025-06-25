from dataclasses import dataclass, field
from typing import Optional
from data.usuario.usuario_model import Usuario

@dataclass
class Administrador(Usuario):
    id_usuario: Optional[int] = field(default=None, init=False)
