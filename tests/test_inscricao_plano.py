import sys
import os


from data.fornecedor.fornecedor_model import *
from data.fornecedor.fornecedor_repo import *
from data.inscricaoplano.inscricao_plano_repo import *
from data.plano.plano_model import Plano
from data.plano.plano_repo import *
from data.prestador.prestador_model import Prestador
from data.prestador.prestador_repo import *
from data.usuario.usuario_repo import *


class Test_InscricaoPlanoRepo:
   
    def test_criar_tabela_inscricao_plano(self, test_db):
        criar_tabela_plano()
        criar_tabela_prestador()
        criar_tabela_fornecedor()
        # Act
        resultado = criar_tabela_inscricao_plano()
        assert resultado == True, "A criação da tabela deveria retornar True"
