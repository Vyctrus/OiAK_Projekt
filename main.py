"""
Project Name : mindkeeper
Author: Andrzej Gierlak
Project started in 06.2021
Desription: i just got annoyed by hex<->binary<->instruction transformations
and have a little free time before exams
i always wanted to do this:
creating imaginary programs in imaginary language,
for imaginary CPU xD
mindkeeper because i thought, i would have gone insane
"""
PROGRAM_NAME = "program.txt"
DECODE_PROGRAM = "decode.txt"
CURRENT_CELL = 0
reg_a = "000"
reg_b = "001"
reg_c = "010"
reg_d = "011"
reg_e = "100"
reg_f = "101"
reg_g = "110"
reg_h = "111"


def hex3_from_int(number):
    """ Formats given value to 3HexCell type

    :param number: Integer value from range <0, 4095>
        (4095 is 0xFFF)
    :return: formats value to specified type that can be stored in our CPU RAM
    """
    hex_val = '{:03x}'.format(number)
    return hex_val


def int_from_hex3(hex_number):
    """ Formats given value from 3HexCell type to integer value

    :param hex_number: value in hexadecimal representation
    :return: formats value to integer representation
    """
    int_val = int(hex_number, 16)
    return int_val


def cell_inc():
    """ CURRENT_CELL incrementation, probably will vanish in future versions
    CURRENT_CELL mechanics are hard to maintain,
    this is probably wrong way of doing this

    """
    global CURRENT_CELL
    CURRENT_CELL += 1


def cell_update_after_jump(jmp_address):
    """ CURRENT_CELL incrementation, probably will vanish in future versions
    CURRENT_CELL mechanics are hard to maintain,
    this is probably wrong way of doing this

    """
    updated_val = int_from_hex3(jmp_address)
    global CURRENT_CELL
    CURRENT_CELL = updated_val


def stop_not_ready():
    """
    Function which stops program because  there were function not ready to use
    :return:
    """
    raise Exception("Sorry, you shouldn't use this function,"
                    " check doc once more, or implement your own function")


def alu_operation(bit_opcode):
    """
    base decoder of alu instructions
    :param bit_opcode: code of wanted function
    :return:
    """
    if bit_opcode == "0000":
        # print("ADD", end=" ")
        text_data = "ADD"
        with open(DECODE_PROGRAM, 'a') as file_object:
            file_object.write(text_data + " ")
    elif bit_opcode == "0001":
        # print("ADD_IM", end=" ")
        text_data = "ADD_IM"
        with open(DECODE_PROGRAM, 'a') as file_object:
            file_object.write(text_data + " ")
    elif bit_opcode == "0010":
        # print("SUB_IM", end=" ")
        text_data = "SUB_IM"
        with open(DECODE_PROGRAM, 'a') as file_object:
            file_object.write(text_data + " ")
    elif bit_opcode == "0011":
        # print("MUL_IM", end=" ")
        text_data = "MUL_IM"
        with open(DECODE_PROGRAM, 'a') as file_object:
            file_object.write(text_data + " ")
    elif bit_opcode == "0100":
        # print("DIV_IM", end=" ")
        text_data = "DIV_IM"
        with open(DECODE_PROGRAM, 'a') as file_object:
            file_object.write(text_data + " ")
    elif bit_opcode == "0101":
        # print("a2_b2", end=" ")
        text_data = "a2_b2"
        with open(DECODE_PROGRAM, 'a') as file_object:
            file_object.write(text_data + " ")
    elif bit_opcode == "0110":
        # print("COMPARE", end=" ")
        text_data = "COMPARE"
        with open(DECODE_PROGRAM, 'a') as file_object:
            file_object.write(text_data + " ")
    elif bit_opcode == "0111":
        # print("DEC_A", end=" ")
        text_data = "DEC_A"
        with open(DECODE_PROGRAM, 'a') as file_object:
            file_object.write(text_data + " ")
    elif bit_opcode == "1000":
        # print("INC_A", end=" ")
        text_data = "INC_A"
        with open(DECODE_PROGRAM, 'a') as file_object:
            file_object.write(text_data + " ")
    elif bit_opcode == "1001":
        # print("MUL_A_C", end=" ")
        text_data = "MUL_A_C"
        with open(DECODE_PROGRAM, 'a') as file_object:
            file_object.write(text_data + " ")
    elif bit_opcode == "1010":
        # print("DIV_A_C", end=" ")
        text_data = "DIV_A_C"
        with open(DECODE_PROGRAM, 'a') as file_object:
            file_object.write(text_data + " ")
    else:
        # print("NOT DEFINIED")
        text_data = "NOT DEFINIED"
        with open(DECODE_PROGRAM, 'a') as file_object:
            file_object.write(text_data + " ")


def cs_operation(bit_opcode):
    """
    decoder, controll section/ general instructions
    :param bit_opcode: code of wanted instruction
    :return:
    """
    if bit_opcode == "0000":
        # print("LOAD", end=' ')
        text_data = "LOAD"
        with open(DECODE_PROGRAM, 'a') as file_object:
            file_object.write(text_data + " ")
    elif bit_opcode == "0001":
        # print("STORE", end=' ')
        text_data = "STORE"
        with open(DECODE_PROGRAM, 'a') as file_object:
            file_object.write(text_data + " ")
    elif bit_opcode == "0010":
        # print("DATA", end=' ')
        text_data = "DATA"
        with open(DECODE_PROGRAM, 'a') as file_object:
            file_object.write(text_data + " ")
    elif bit_opcode == "0011":
        # print("JMPR", end=' ')
        text_data = "JMPR"
        with open(DECODE_PROGRAM, 'a') as file_object:
            file_object.write(text_data + " ")
    elif bit_opcode == "0100":
        # print("JUMP", end=' ')
        text_data = "JUMP"
        with open(DECODE_PROGRAM, 'a') as file_object:
            file_object.write(text_data + " ")
    elif bit_opcode == "0101":
        # print("JMP_IF", end=' ')
        text_data = "JMP_IF"
        with open(DECODE_PROGRAM, 'a') as file_object:
            file_object.write(text_data + " ")
    elif bit_opcode == "0110":
        # print("SET_IM", end=' ')
        text_data = "SET_IM"
        with open(DECODE_PROGRAM, 'a') as file_object:
            file_object.write(text_data + " ")
    elif bit_opcode == "0111":
        # print("STROE_RESULTS", end=' ')
        text_data = "STROE_RESULTS"
        with open(DECODE_PROGRAM, 'a') as file_object:
            file_object.write(text_data + " ")
    elif bit_opcode == "1000":
        # print("RESULT_FLG", end=' ')
        text_data = "RESULT_FLG"
        with open(DECODE_PROGRAM, 'a') as file_object:
            file_object.write(text_data + " ")
    elif bit_opcode == "1001":
        # print("STROE_OVS", end=' ')
        text_data = "STROE_OVS"
        with open(DECODE_PROGRAM, 'a') as file_object:
            file_object.write(text_data + " ")
    else:
        # print("NOT DEFINIED")
        text_data = "NOT DEFINIED"
        with open(DECODE_PROGRAM, 'a') as file_object:
            file_object.write(text_data + " ")


def take_me(hex3str):
    """ Basic decoding function, base for future decoder
    :param hex3str: "010" -->translate--> print("LOAD")
    """
    my_hex_data = hex3str
    scale = 16
    num_of_bits = 12
    val = bin(int(my_hex_data, scale))[2:].zfill(num_of_bits)
    bit_0 = val[-11:-10:1]
    bit_opcode = val[-10:-6:1]
    bit_a = val[-6:-3:1]
    bit_b = val[-3:]

    if bit_0 == "1":
        alu_operation(bit_opcode)
    else:
        cs_operation(bit_opcode)
    # print("ra: " + bit_a + " rb: " + bit_b)
    text_data = ("ra: " + bit_a + " rb: " + bit_b)
    with open(DECODE_PROGRAM, 'a') as file_object:
        file_object.write(text_data + "\n")


def code_me(bit_alu, bits_operation, bits_reg_a, bits_reg_b):
    """ Base for all coding functions, translates specified functions to machine language

    :param bit_alu: "0"/"1" decides which part of functions we wanna use
                    0 - cs ControllSection/core instructions
                    1 - alu ALU instructions
    :param bits_operation: "0000" 4bits of operation code (opcode),
                            here we chose instruction
    :param bits_reg_a:  "001" 3 bits describing register A(number of that register)
    :param bits_reg_b:  "001" 3 bits describing register B(number of that register)
    :return:
    """
    is_alu = str(bit_alu)
    operation = str(bits_operation)
    register_a = str(bits_reg_a)
    register_b = str(bits_reg_b)

    hex_representation = is_alu + operation + register_a + register_b
    hex_cell = ('%03X' % int(hex_representation, 2))
    return hex_cell


def save_instruction(cpu_part, opcode, register_a, register_b):
    """
    Template function, used by save_CS, save_alu
    :param cpu_part:
    :param opcode:
    :param register_a:
    :param register_b:
    :return:
    """
    hex_code = code_me(cpu_part, opcode, register_a, register_b)
    with open(PROGRAM_NAME, 'a') as file_object:
        file_object.write(hex_code + " ")
    cell_inc()


def save_cs(register_a, register_b, opcode):
    """
    Template function, use in general/ControlSection instructions to save sommand
    :param register_a:
    :param register_b:
    :param opcode:
    :return:
    """
    cpu_part = "0"
    save_instruction(cpu_part, opcode, register_a, register_b)


def save_alu(register_a, register_b, opcode):
    """
    Template function, use it in ALU instructions to save command
    :param register_a:
    :param register_b:
    :param opcode:
    :return:
    """
    cpu_part = "1"
    save_instruction(cpu_part, opcode, register_a, register_b)


# ======================================= #CS ControlSection
def LOAD(register_a, register_b):
    """"reg(rb)= RAM(reg(ra))
    loads from RAM specified in register number ra, to register number rb
    Parameters
    ----------
    register_a : str
        address/number of register A
    register_b : str
        address/number of register B
    """
    opcode = "0000"
    save_cs(register_a, register_b, opcode)


def STORE(register_a, register_b):
    """" RAM(reg(ra))= reg(rb)
    loads from register number rb, to RAM specified in register number ra
    Parameters
    ----------
    register_a : str
        address/number of register A
    register_b : str
        address/number of register B
    """
    opcode = "0001"
    save_cs(register_a, register_b, opcode)


def DATA(register_b, value):
    """" reg(rb)= RAM from next RAM space
    read from next cell of RAM to register
    size: 2 x 3HexCell
    Parameters
    ----------
    register_b : str
        address/number of register B
    value: str
        value in next RAM cell, value we want to load to register B
    """
    register_a = "000"  # bcs not used!
    # hex_val = value
    nexT_data = value  # ('%03X' % int(hex_val, 2))
    opcode = "0010"
    save_cs(register_a, register_b, opcode)
    with open(PROGRAM_NAME, 'a') as file_object:
        file_object.write(nexT_data + " ")
    cell_inc()


def JUMPR(register_a, register_b):
    """

    :param register_a:
    :param register_b:
    :return:
    """
    stop_not_ready()
    opcode = "0011"
    save_cs(register_a, register_b, opcode)


def JUMP(value):
    """" Jump to adress specified in next cell of RAM
    Size: 2 cells x 3Hex
    Parameters
    ----------
    value: str
        where we want program to jump
    """
    nexT_data = value  # ('%03X' % int(hex_val, 2))
    ra = "000"
    rb = "000"
    opcode = "0100"
    save_cs(ra, rb, opcode)
    with open(PROGRAM_NAME, 'a') as file_object:
        file_object.write(nexT_data + " ")
    cell_inc()
    cell_update_after_jump(value)


def JUMP_IF(): #address, flags
    """ #Todo think about size, change CURRENT_CELL after jump ? how can i know?
        # Do not use now!
    size: ? similar as jump
    JUMP IF condition:
    bit 0 -  ALU.A==0
    bit 1 - numbers (A,B)==(C,D)
    bit 2 - ALU.A > ALU.C
    bit 3 - ALU.A == ALU.C
    bit 4 - flag is true div by zero
    """
    stop_not_ready()
    # next_data = address
    register_a = "111"
    register_b = "111"
    opcode = "0101"
    save_cs(register_a, register_b, opcode)


def SET_IM(register_a, register_b):
    """

    :param register_a:
    :param register_b:
    :return:
    """
    opcode = "0110"
    save_cs(register_a, register_b, opcode)


def STORE_RESULTS(register_a, register_b):
    """
    size: 1 x 3hexCell
    :param register_a:
    :param register_b:
    :return:
    """
    opcode = "0111"
    save_cs(register_a, register_b, opcode)


def RESET_FLG():
    """ CLear FLAGS register
    size: 1 x 3hexCell
    ra, rb are not used, they do not change the result

    """
    register_a = "000"
    register_b = "000"
    opcode = "1000"
    save_cs(register_a, register_b, opcode)


def STORE_OVS(register_a, register_b):
    """

    :param register_a:
    :param register_b:
    :return:
    """
    opcode = "1001"
    save_cs(register_a, register_b, opcode)


# =========================================  #ALU
def ADD(register_a, register_b):
    """" acc re= val(ra)+val(rb)
    size= 1 x 3HexCell
    ADD numbers from register specified in ra to register specified in rb
    You need to use STORE_RESULTS if you want to save result, read more in STORE_RESULT doc
    Parameters
    ----------
    register_a: value of first operand

    register_b: value of second operand
    """
    opcode = "0000"
    save_alu(register_a, register_b, opcode)


def ADD_CX(register_a, register_b):
    """

    :param register_a:
    :param register_b:
    :return:
    """
    opcode = "0001"
    save_alu(register_a, register_b, opcode)


def SUB_CX(register_a, register_b):
    """

    :param register_a:
    :param register_b:
    :return:
    """
    opcode = "0010"
    save_alu(register_a, register_b, opcode)


def MUL_CX(register_a, register_b):
    """
    Multiply complex number
    :param register_a:
    :param register_b:
    :return:
    """
    opcode = "0011"
    save_alu(register_a, register_b, opcode)


def DIV_CX(register_a, register_b):
    """
    Divide complex number
    :param register_a:
    :param register_b:
    :return:
    """
    opcode = "0100"
    save_alu(register_a, register_b, opcode)


def a2_b2(register_a, register_b):
    """ (modulus of complex number)^2, in other words "a^2 + b^2)

    :param register_a:
    :param register_b:
    :return:
    """
    opcode = "0101"
    save_alu(register_a, register_b, opcode)


def COMPARE(register_a, register_b):
    """ compare 2 numbers from selected registers and
        set flags according to the result
    size: 1 x 3HexCell
    :param register_a:
    :param register_b:
    :return:
    """
    opcode = "0110"
    save_alu(register_a, register_b, opcode)


def DEC_A(register_a):
    """Decrementing  by 1 in specified register
    :param register_a: register which contains value we want to decrement
    :return:
    """
    register_b="000"
    opcode = "0111"
    save_alu(register_a, register_b, opcode)


def INC_A(register_a):
    """ Incrementation by 1 in specified register
    :param register_a: register which contains value we want to increment
    :return:
    """
    register_b="000"
    opcode = "1000"
    save_alu(register_a, register_b, opcode)


def MUL_A_C(register_a, register_b):
    """Multiplication A*C, result in ACC_RE, so u need to read it by
     STORE_RESULTS instruction

    :param register_a: number of register that is containing desired A
    :param register_b: number of register that is containing desired C
    :return: A*C
    """
    opcode = "1001"
    save_alu(register_a, register_b, opcode)


def DIV_A_C(register_a, register_b):
    """ Division A/C, result in ACC_RE, so u need to read it by
     STORE_RESULTS instruction

    :param register_a: number of register that is containing desired A
    :param register_b: number of register that is containing desired C
    :return: A/C
    """
    opcode = "1010"
    save_alu(register_a, register_b, opcode)


# ======== Higher level functions ==================== #HLF

def KEEP_IN_PLACE():
    """" cell JUMP-> cell JUMP
     keep program in one place, stops execution of RAM
     works only if CURRENT_CELL incremented properly
     DANGER! other jumps in program, desynchronize this function
     Todo: update CURRENT_CELL after each JUMP instruction
    """
    JUMP(hex3_from_int(CURRENT_CELL))


def DATA_INT(register, intVal):
    """"fills register with integerValue
    size: 2 x 3HexCell
    Parameters
    ----------
    register: register where we want to store value

    intVal: integer number we want to store on RAM,
    and then it will be loaded form there to specified register,
    when program runs

    """
    DATA(register, hex3_from_int(intVal))


def JUMP_IF_3(address):
    """ status: testing
    JUMP IF ocndition specified by flag bit 3: jump if ALU.A == ALU.C
    Dangerous Function! Desynchronizing cell_update !!!
    size: 2 x 3HexCell //instruction name + address in 2nd cell
    :param address:
    :return:
    """
    next_data = address
    register_a = "001"  # bit "number 3" set to 1
    register_b = "000"
    opcode = "0101"
    save_cs(register_a, register_b, opcode)
    with open(PROGRAM_NAME, 'a') as file_object:
        file_object.write(next_data + " ")
    cell_inc()
    # cell_update_after_jump(value)


# ========== Live code section ===================== #LCS
if __name__ == '__main__':
    # code_me("1","1111","010","001")
    # take_me("022")
    # ^- very primitive start :D

    codes = ["022", "011", "066"]
    code_me("0", "0010", "000", "011")
    # for code in codes:
    #     take_me(code)
    take_me("082")


    # trying to create  for loop

    DATA_INT(reg_c, 0)  # 2
    DATA_INT(reg_d, 1)  # 2
    DATA_INT(reg_e, 8)  # 2
    RESET_FLG()  # 1

    ADD(reg_c, reg_d)  # 1
    STORE_RESULTS(reg_c, reg_c)  # 1

    COMPARE(reg_c, reg_e)  # 1
    JUMP_IF_3("020")  # 2
    JUMP("007")  # 2

    cell_update_after_jump("020")
    KEEP_IN_PLACE()
