from qiskit import QuantumRegister,QuantumCircuit, Aer, execute, ClassicalRegister
from module_gates import gates  
Curcuit_len = 6
qreg_q = QuantumRegister(Curcuit_len, 'q')
creg_c = ClassicalRegister(Curcuit_len, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)
circuit.x(qreg_q[0])
# circuit.x(qreg_q[1])
gates.adder(circuit,[qreg_q[0],qreg_q[1]],[qreg_q[2],qreg_q[3],qreg_q[4],qreg_q[5]],[creg_c[0],creg_c[1]])
print(circuit.draw())


emulator = Aer.get_backend('qasm_simulator')
task = execute(circuit,emulator,shots=10)
#result = task.result()
result = task.result().get_counts()
print(result)

