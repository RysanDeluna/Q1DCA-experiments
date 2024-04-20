"""
    * Author :        rysan  (https://github.com/RysanDeluna/)
    * Created:        15/04/2024
"""

# IMPORTS --------------------------------
import random

# Classes --------------------------------

class Cell:
    """Classe representando uma célula de um autômato celular Binário"""

    def __init__(self):
        self.alive = False

    # Mata a célula
    def die(self):
        self.alive = False

    # Revive a célula
    def live(self):
        self.alive = True

    # Alterna o estado da celula
    def alternate(self):
        self.alive = not self.alive

    # Retorna o estado da célula
    def is_alive(self):
        return self.alive

class CellularAutomata:
    """Configuração 1D de células"""

    def __init__(self, n_cell):
        self.n = n_cell
        self.cells = []
        for _ in range(n_cell):
            self.cells.append(Cell())

    # Mostra a configuração do automato
    def _print(self):
        automato = ""
        for c in self.cells:
            if c.is_alive(): automato += "■ "
            else: automato += "□ "
        print(automato)

    def generate_random_configuration(self, threshold):
        for cell in self.cells:
            if random.randint(0,101) > threshold: cell.alternate()
