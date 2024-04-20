"""
    * Author :        rysan  (https://github.com/RysanDeluna/)
    * Created:        15/04/2024
"""

# IMPORTS --------------------------------
import qiskit

from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import QiskitRuntimeService

from classes.CellularAutomata import Cell, CellularAutomata
from classes.Simulators import Simulator

# FUNCTIONS ------------------------------

def prepare_rule90(qc: qiskit.QuantumCircuit):
    qc.h([0,1,2])

    # Middle bit
    qc.cx([0,2,3],[3,3,1])
    qc.barrier()
    qc.reset(3)

    # Left bit
    qc.cx([1,3],[3,2])
    qc.barrier()
    qc.reset(3)

    # Right bit
    qc.cx([1,3],[3,0])
    qc.barrier()
    qc.reset(3)

    qc.h([0,1,2])
    return qc


# MAIN -----------------------------------
if __name__ == "__main__":
    sim = Simulator("ibm_kyoto")
    qc = prepare_rule90(qiskit.QuantumCircuit(4))
    qc.measure_all()
    sim.run_ideal(qc)
    print(sim.results["ideal"].get_counts())
