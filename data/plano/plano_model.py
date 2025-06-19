from dataclasses import dataclass


@dataclass
class Plano:
    id_plano: int
    nome_plano: str
    valor_mensal: float
    limite_servico: int
    tipo_plano: str
    descricao: str


