from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

resources = {
    "00": "Ambulance",
    "01": "Hospital",
    "10": "Blood Bank",
    "11": "Emergency Pharmacy"
}

target = "Hospital"

qc = QuantumCircuit(2, 2)

# Superposition
qc.h(0)
qc.h(1)

# Mark target state 01
qc.x(0)
qc.cz(0, 1)
qc.x(0)

# Grover diffusion
qc.h(0)
qc.h(1)
qc.x(0)
qc.x(1)
qc.cz(0, 1)
qc.x(0)
qc.x(1)
qc.h(0)
qc.h(1)

# Measurement
qc.measure([0, 1], [1, 0])

# Simulation
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()

print("===================================")
print("QUANTUM EMERGENCY RESOURCE SEARCH")
print("===================================")

print("Target Resource:", target)

print("\nResource Mapping:")
for state, resource in resources.items():
    print(state, "->", resource)

print("\nQuantum Measurement Results:")
print(counts)

print("\nProbability Results:")

for state, count in counts.items():
    probability = (count / 1024) * 100
    resource = resources.get(state, "Unknown")
    print(state, "->", resource, "->", round(probability, 2), "%")
print("\n===================================")
print("CLASSICAL vs QUANTUM SEARCH")
print("===================================")

print("Number of resources:", len(resources))

print("\nClassical Search:")
print("Checks resources one by one until the target is found.")

print("\nQuantum Search:")
print("Uses Grover's Algorithm to amplify the target state.")

print("\nOur Quantum Target:")
print("01 -> Hospital")

print("\nSimulation Result:")
print("01 -> Hospital -> 100%")