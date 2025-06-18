from dataclasses import dataclass
from datetime import datetime   

@dataclass
class Mensagem:
    id_mensagem: int
    id_remetente: int
    id_destinatario: int
    conteudo: str
    data_hora: datetime
    nome_remetente: str
    nome_destinatario: str