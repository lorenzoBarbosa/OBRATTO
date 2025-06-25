from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Usuario:
    nome: str
    email: str
    senha: str
    id: Optional[int] = field(default=None)

