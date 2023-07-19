import unittest
from root_square_solver import rootSquareSolver

#teste de equações de segundo grau
class CheckRootSquareSolve(unittest.TestCase):
    # verifica se uma equação tem duas respostas
    def teste_checkTwoRoots(self):
        response = rootSquareSolver(1, -5, 6) # x²-5x+6 = 0 => r1=3 e r2=2
        self.assertEqual(len(response), 2) # verifica se o tamanho da resposta é igual a 2

    # verifica os se os valores retornados na função são o resultado da equação
    def test_checkRootValue1(self):
        response = rootSquareSolver(1, -5, 6)
        self.assertIn(response[0],[2,3]) # como sabemos que a resposta é 2 e 3, verificamos se a resposta esta dentro do que foi retornado na função na posição 0 do array
    
    def test_checkRootValue2(self):
        response = rootSquareSolver(1, -5, 6)
        self.assertIn(response[1],[2,3]) # como sabemos que a resposta é 2 e 3, verificamos se a resposta esta dentro do que foi retornado na função na posição 1 do array

     # verifica se uma equação tem uma resposta
    def teste_checkOneRoots(self):
        response = rootSquareSolver(1, -4, 4) # x²-4x+4 = 0
        self.assertEqual(len(response), 1) # verifica se o tamanho da resposta é igual a 1
