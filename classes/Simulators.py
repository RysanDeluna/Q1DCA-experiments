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

    results = {}  # (name:result)

    def __init__(self, backend="ibm_kyoto"):
        self.backend = AerSimulator.from_backend(QiskitRuntimeService().get_backend(backend))

    def run_noisy(self, circuit: qiskit.QuantumCircuit, shots=100, name="noisy"):
        # Run the noisy version of the simulator and put the result inside the dict
        self.results[name] = self.backend.run(circuit, shots=shots).result()

    def run_ideal(self, circuit: qiskit.QuantumCircuit, shots=100, name="ideal"):
        # Run the ideal version of the simulator and put the result inside the dict
        self.results[name] = AerSimulator().run(circuit, shots=shots).result()


# Testes ---------------------------------
def simples_circuit(name="teste"):
    qc = qiskit.QuantumCircuit(2, name=name)
    qc.h([0,1])
    qc.measure_all()
    return qc


if __name__ == "__main__":
    sim = Simulator("ibm_kyoto")
    sim.run_ideal(simples_circuit())
    sim.run_noisy(simples_circuit())

    print(sim.results["ideal"].get_counts())
    print(sim.results["noisy"].get_counts())
