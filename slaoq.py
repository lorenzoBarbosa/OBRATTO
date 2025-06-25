import os
import sys
import repo.categoria_repo import *

class TestCategoriaRepo:
    def test_criar_tabela_categorias(self,test_db):
        # Arrange
        # Act
        resultado = criar_tabela()
        # Assert
        assert resultado is True, "A tabela de categorias não foi criada com sucesso."
