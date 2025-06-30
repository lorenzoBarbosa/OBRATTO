from dataclasses import dataclass


@dataclass
class Plano:
    def __init__(self, id_plano=None, nome_plano=None, valor_mensal=None, limite_servico=None, tipo_plano=None, descricao=None):
        self.id_plano = id_plano
        self.nome_plano = nome_plano
        self.valor_mensal = valor_mensal
        self.limite_servico = limite_servico
        self.tipo_plano = tipo_plano
        self.descricao = descricao

