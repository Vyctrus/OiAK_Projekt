DATA_INT(regC, 0)  # 2
DATA_INT(regD, 1)  # 2
DATA_INT(regE, 8)  # 2
RESET_FLG()  # 1

ADD(regC, regD)  # 1
STORE_RESULTS(regC, regC)  # 1

COMPARE(regC, regE)  # 1
JMP_IF_3("020")  # 2
JUMP("007")  # 2

cell_update_after_jump("020")
KEEP_IN_PLACE()