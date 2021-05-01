def xor(curcuit,applied_reg,process_reg,data_reg):
    if len(applied_reg) == 2 and len(process_reg) == 3:
        curcuit.x(applied_reg[0])
        curcuit.ccx(applied_reg[0],applied_reg[1],process_reg[0])
        curcuit.x(applied_reg[0])
        curcuit.x(applied_reg[1])
        curcuit.ccx(applied_reg[0],applied_reg[1],process_reg[1])
        curcuit.x(applied_reg[1])
        curcuit.cx(process_reg[0],process_reg[2])
        curcuit.cx(process_reg[1],process_reg[2])
        curcuit.ccx(process_reg[0],process_reg[1],process_reg[2])
        curcuit.measure(process_reg[2],data_reg)
        return True
    else:
        return None
def adder(curcuit,applied_reg,process_reg,data_reg):
    if len(applied_reg) == 2 and len(process_reg) == 4 and len(data_reg) == 2:
        xor(curcuit,applied_reg,process_reg[:-1],data_reg[0])
        curcuit.ccx(applied_reg[0],applied_reg[1],process_reg[-1])
        curcuit.measure(process_reg[-1],data_reg[1])
        return True
    else:
        return None
