from dataclasses import dataclass
import datetime
from data.mensagem.mensagem_model import Usuario


@dataclass
class Mensagem(Usuario):
    id_mensagem: int
    id_remetente: int
    id_destinatario: int
    conteudo: str
    data_hora: datetime