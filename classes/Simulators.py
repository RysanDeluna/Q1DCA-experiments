"""
    * Author :        rysan  (https://github.com/RysanDeluna/)
    * Created:        20/04/2024
"""

# IMPORTS --------------------------------
import qiskit

from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import QiskitRuntimeService

class Simulator:
    """Handles different quantum simulators"""

    def __init__(self, backend: str):
        self.backend = AerSimulator.from_backend(QiskitRuntimeService().get_backend(backend))

    def run_noisy(self, circuit: qiskit.QuantumCircuit, shots: int):
        return self.backend.run(circuit, shots=shots).result()

    def run_ideal(self, circuit, shots):
        return AerSimulator().run(circuit, shots=shots).result()

