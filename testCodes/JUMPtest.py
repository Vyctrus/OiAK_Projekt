DATA_INT(regC, 105)
DATA_INT(regD, 68)
# DATA(regC,"069") # same as above ( DATA_INT(regC,105)) :D !!!
# DATA(regD,"044")
ADD(regC, regD)  # rozmiar 1
STORE_RESULTS(regE, regE)  # rozmiar1

hexVal = hex3_from_int(CURRENT_CELL)
print("Adress before jump : {0}".format(hexVal))

JUMP("020")  # after this <- will increment +2, we need to change it to? 001?
# cell_update_after_jump("020")

hexVal = hex3_from_int(CURRENT_CELL)
print("Adress after jump : {0}".format(hexVal))

KEEP_IN_PLACE()

hexVal = hex3_from_int(CURRENT_CELL)
print("Adress after jump : {0}".format(hexVal))