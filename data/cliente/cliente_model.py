from dataclasses import dataclass
import datetime

@dataclass
class Cliente:
    id: int  # PK da tabela cliente
    id_usuario: int  # FK para tabela usuario
    genero: str
    data_nascimento: datetime.date
