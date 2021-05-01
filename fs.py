from qiskit import QuantumCircuit, execute, Aer
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi
qreg_q = QuantumRegister(15, 'q')
creg_c = ClassicalRegister(15, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)
q_bit_present = 0
#circuit.x(qreg_q[0])
#circuit.x(qreg_q[1])
#circuit.x(qreg_q[3])
#circuit.x(qreg_q[4])
#circuit.ccx(qreg_q[0], qreg_q[1], qreg_q[2])
#circuit.cx(qreg_q[4], qreg_q[5])
#circuit.x(qreg_q[2])
#circuit.cx(qreg_q[3], qreg_q[5])
#circuit.ccx(qreg_q[3], qreg_q[4], qreg_q[5])
#circuit.x(qreg_q[5])
#circuit.measure(qreg_q[5], creg_c[5])
#circuit.measure(qreg_q[2], creg_c[2])
def binary_num(num,curcuit,reg):
    global q_bit_present
    if num <= 7 and q_bit_present!=6:
        qubit = [reg[q_bit_present],reg[q_bit_present+1],reg[q_bit_present+2]]
        binary = str(bin(num)).replace("0b","")
        if len(binary) < 3:
            binary = "0"*(3-len(binary)) + binary
        for bit,val in zip(qubit,binary):
            if val == "1":
                curcuit.x(bit)
        q_bit_present += 3
        return True
    else:
        return None
binary_num(7,circuit,qreg_q)
binary_num(2,circuit,qreg_q)
circuit.cx(qreg_q[0],qreg_q[6])
circuit.cx(qreg_q[3],qreg_q[7])
circuit.cx(qreg_q[6],qreg_q[8])
circuit.x(qreg_q[8])
circuit.cx(qreg_q[7],qreg_q[9])
circuit.x(qreg_q[9])
"""
q_6(a) is invert of q_8(a')
q_7(b) is invert of q_9(b')
"""
circuit.ccx(qreg_q[7],qreg_q[8],qreg_q[10])
circuit.ccx(qreg_q[6],qreg_q[9],qreg_q[11])
circuit.cx(qreg_q[10],qreg_q[12])
circuit.cx(qreg_q[11],qreg_q[12])
circuit.ccx(qreg_q[10],qreg_q[11],qreg_q[12])
circuit.measure(qreg_q[12],creg_c[12])
print(circuit.draw())
#print(circuit)
# emulator = Aer.get_backend('qasm_simulator')
# task = execute(circuit,emulator,shots=10)
# #result = task.result()
# result = task.result().get_counts()
# print(result)