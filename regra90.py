"""
    * Author :        rysan  (https://github.com/RysanDeluna/)
    * Created:        15/04/2024
"""

# IMPORTS --------------------------------
import qiskit

from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import QiskitRuntimeService

from CellularAutomata import Cell, CellularAutomata

# Functions ------------------------------

def simulate_noise(circuit):
    aersim_backend = AerSimulator.from_backend(QiskitRuntimeService().get_backend("ibm_kyoto"))
    return aersim_backend.run(circuit, shots=1).result()


def simulate_ideal(circuit):
    return AerSimulator().run(circuit, shots=1).result()


def oracle(qc: qiskit.QuantumCircuit):
    for i in range(2):
        qc.h(i)
    qc.ccx(0,1,2)


def rodar(ca, t):
    qc = qiskit.QuantumCircuit(len(ca.cells))
    for cell in range(len(ca.cells)):
        if ca.cells.is_alive(): qc.x(cell)

    for _ in range(t):
        for cell in ca.cells:
            print(sim)



# MAIN -----------------------------------
if __name__ == "__main__":
    config = "010"
    ca = CellularAutomata(len(config))

