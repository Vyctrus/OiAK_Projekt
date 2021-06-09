
PROGRAM_NAME = "program.txt"
DECODE_PROGRAM= "decode.txt"
CURRENT_CELL = 0
regA = "000"
regB = "001"
regC = "010"
regD = "011"
regE = "100"
regF = "101"
regG = "110"
regH = "111"


# należy je zwiększać po każdym zapisie do pliku program.txt

def hex3_from_int(number):
    hexVal = '{:03x}'.format(number)
    return hexVal

def int_from_hex3(hexNumber):
    intVal= int(hexNumber, 16)
    return intVal

def cell_inc():
    global CURRENT_CELL
    CURRENT_CELL+=1

def take_me(hex3str):
    # XXX -> LOAD what from what, from where
    my_hex_data= "fa1"
    my_hex_data= hex3str
    scale = 16
    num_of_bits = 12
    val= bin(int(my_hex_data, scale))[2:].zfill(num_of_bits)
    #print(val)

    bit_0 = val[-11:-10:1]
    bit_opcode= val[-10:-6:1]
    bit_A= val[-6:-3:1]
    bit_B= val[-3:]
    if(bit_0 == "1"):
        #print("ALU", end =" ")
        if (bit_opcode == "0000"):
            print("ADD",end=" ")
            text_data = ("ADD")
            with open(DECODE_PROGRAM, 'a') as file_object:
                file_object.write(text_data + " ")
        elif (bit_opcode == "0001"):
            print("ADD_IM",end=" ")
            text_data = ("ADD_IM")
            with open(DECODE_PROGRAM, 'a') as file_object:
                file_object.write(text_data + " ")
        elif (bit_opcode == "0010"):
            print("SUB_IM",end=" ")
            text_data = ("SUB_IM")
            with open(DECODE_PROGRAM, 'a') as file_object:
                file_object.write(text_data + " ")
        elif (bit_opcode == "0011"):
            print("MUL_IM",end=" ")
            text_data = ("MUL_IM")
            with open(DECODE_PROGRAM, 'a') as file_object:
                file_object.write(text_data + " ")
        elif (bit_opcode == "0100"):
            print("DIV_IM",end=" ")
            text_data = ("DIV_IM")
            with open(DECODE_PROGRAM, 'a') as file_object:
                file_object.write(text_data + " ")
        elif (bit_opcode == "0101"):
            print("a2_b2",end=" ")
            text_data = ("a2_b2")
            with open(DECODE_PROGRAM, 'a') as file_object:
                file_object.write(text_data + " ")
        elif (bit_opcode == "0110"):
            print("COMPARE",end=" ")
            text_data = ("COMPARE")
            with open(DECODE_PROGRAM, 'a') as file_object:
                file_object.write(text_data + " ")
        elif (bit_opcode == "0111"):
            print("DEC_A",end=" ")
            text_data = ("DEC_A")
            with open(DECODE_PROGRAM, 'a') as file_object:
                file_object.write(text_data + " ")
        elif (bit_opcode == "1000"):
            print("INC_A",end=" ")
            text_data = ("INC_A")
            with open(DECODE_PROGRAM, 'a') as file_object:
                file_object.write(text_data + " ")
        elif (bit_opcode == "1001"):
            print("MUL_A_C",end=" ")
            text_data = ("MUL_A_C")
            with open(DECODE_PROGRAM, 'a') as file_object:
                file_object.write(text_data + " ")
        elif (bit_opcode == "1010"):
            print("DIV_A_C",end=" ")
            text_data = ("DIV_A_C")
            with open(DECODE_PROGRAM, 'a') as file_object:
                file_object.write(text_data + " ")
        else:
            print("NOT DEFINIED")


    else:
        #print("Not ALU")
        #print(bit_opcode)
        if(bit_opcode=="0000"):
            print("LOAD", end=' ')
            text_data = ("LOAD")
            with open(DECODE_PROGRAM, 'a') as file_object:
                file_object.write(text_data + " ")
        elif(bit_opcode=="0001"):
            print("STORE", end=' ')
            text_data = ("STORE")
            with open(DECODE_PROGRAM, 'a') as file_object:
                file_object.write(text_data + " ")
        elif (bit_opcode == "0010"):
            print("DATA", end=' ')
            text_data = ("DATA")
            with open(DECODE_PROGRAM, 'a') as file_object:
                file_object.write(text_data + " ")
        elif (bit_opcode == "0011"):
            print("JMPR", end=' ')
            text_data = ("JMPR")
            with open(DECODE_PROGRAM, 'a') as file_object:
                file_object.write(text_data + " ")
        elif (bit_opcode == "0100"):
            print("JUMP", end=' ')
            text_data = ("JUMP")
            with open(DECODE_PROGRAM, 'a') as file_object:
                file_object.write(text_data + " ")
        elif (bit_opcode == "0101"):
            print("JMP_IF", end=' ')
            text_data = ("JMP_IF")
            with open(DECODE_PROGRAM, 'a') as file_object:
                file_object.write(text_data + " ")
        elif (bit_opcode == "0110"):
            print("SET_IM", end=' ')
            text_data = ("SET_IM")
            with open(DECODE_PROGRAM, 'a') as file_object:
                file_object.write(text_data + " ")
        elif (bit_opcode == "0111"):
            print("STROE_RESULTS", end=' ')
            text_data = ("STROE_RESULTS")
            with open(DECODE_PROGRAM, 'a') as file_object:
                file_object.write(text_data + " ")
        elif (bit_opcode == "1000"):
            print("RESULT_FLG", end=' ')
            text_data = ("RESULT_FLG")
            with open(DECODE_PROGRAM, 'a') as file_object:
                file_object.write(text_data + " ")
        elif (bit_opcode == "1001"):
            print("STROE_OVS", end=' ')
            text_data = ("STROE_OVS")
            with open(DECODE_PROGRAM, 'a') as file_object:
                file_object.write(text_data + " ")
        else:
            print("NOT DEFINIED")
            text_data = ("NOT DEFINIED")
            with open(DECODE_PROGRAM, 'a') as file_object:
                file_object.write(text_data + " ")

    print("ra: " + bit_A + " rb: " + bit_B)
    text_data=("ra: " + bit_A + " rb: " + bit_B)
    with open(DECODE_PROGRAM, 'a') as file_object:
        file_object.write(text_data+ "\n")

def code_me(bit_alu, bits_operation, bits_reg_a, bits_reg_b):
    isALU= "1"
    operation= "0001"
    regA= "000"
    regB = "010"

    isALU = str(bit_alu)
    operation=str(bits_operation)
    regA = str(bits_reg_a)
    regB =str(bits_reg_b)

    hexik=isALU+operation+regA+regB
    #print(hexik)
    #print('%03X' % int(hexik, 2))
    result= ('%03X' % int(hexik, 2))
    print(result)
    return result


def not_ALU_template(ra,rb, opcode):
    hex_code = code_me("0", opcode, ra, rb)
    with open(PROGRAM_NAME, 'a') as file_object:
        file_object.write(hex_code + " ")
    cell_inc()

def ALU_template(ra,rb, opcode):
    hex_code = code_me("1", opcode, ra, rb)
    with open(PROGRAM_NAME, 'a') as file_object:
        file_object.write(hex_code + " ")
    cell_inc()

def LOAD(ra,rb):
    """"reg(rb)= RAM(reg(ra))
    loads from RAM specified in register number ra, to register number rb
    Parameters
    ----------
    ra : str
        address/number of register A
    rb : str
        address/number of register B
    """
    opcode="0000"
    not_ALU_template(ra,rb,opcode)


def STORE(ra,rb):
    """" RAM(reg(ra))= reg(rb)
    loads from register number rb, to RAM specified in register number ra
    Parameters
    ----------
    ra : str
        address/number of register A
    rb : str
        address/number of register B
    """
    opcode="0001"
    not_ALU_template(ra,rb,opcode)


def DATA(rb,value):
    """" reg(rb)= RAM from next RAM space
    read from next cell of RAM to register
    Parameters
    ----------
    rb : str
        address/number of register B
    value: str
        value in next RAM cell, value we want to load to register B
    """
    ra="000" #bcs not used!
    #hex_val = value
    nexT_data =value#  ('%03X' % int(hex_val, 2))
    opcode="0010"
    not_ALU_template(ra,rb,opcode)
    with open(PROGRAM_NAME, 'a') as file_object:
        file_object.write(nexT_data + " ")
    cell_inc()

def JMPR(ra,rb):
    opcode="0011"
    not_ALU_template(ra,rb,opcode)

def JUMP(value):
    """" Jump to adress specified in next cell of RAM
    Parameters
    ----------
    value: str
        where we want program to jump
    """
    nexT_data = value #('%03X' % int(hex_val, 2))
    ra="000"
    rb="000"
    opcode="0100"
    not_ALU_template(ra,rb,opcode)
    with open(PROGRAM_NAME, 'a') as file_object:
        file_object.write(nexT_data + " ")
    cell_inc()

def JMP_IF(ra,rb):
    opcode="0101"
    not_ALU_template(ra,rb,opcode)

def SET_IM(ra,rb):
    opcode="0110"
    not_ALU_template(ra,rb,opcode)

def STORE_RESULTS(ra,rb):
    opcode="0111"
    not_ALU_template(ra,rb,opcode)

def RESET_FLG(ra,rb):
    opcode="1000"
    not_ALU_template(ra,rb,opcode)

def STORE_OVS(ra,rb):
    opcode="1001"
    not_ALU_template(ra,rb,opcode)

#=========================================  ALU part
def ADD(ra,rb):
    """" acc re= val(ra)+val(rb)
    ADD numbers from register specified in ra to register specified in rb
    You need to use STORE_RESULTS if you want to save result, read more in STORE_RESULT doc
    Todo: merge this with STORE_RESULTS
    Parameters
    ----------
    ra: value of first operand

    rb: value of second operand
    """
    opcode="0000"
    ALU_template(ra,rb,opcode)

def ADD_IM(ra,rb):
    opcode="0001"
    ALU_template(ra,rb,opcode)

def SUB_IM(ra,rb):
    opcode="0010"
    ALU_template(ra,rb,opcode)

def MUL_IM(ra,rb):
    opcode="0011"
    ALU_template(ra,rb,opcode)

def DIV_IM(ra,rb):
    opcode="0100"
    ALU_template(ra,rb,opcode)

def a2_b2(ra,rb):
    opcode="0101"
    ALU_template(ra,rb,opcode)

def COMPARE(ra,rb):
    opcode="0110"
    ALU_template(ra,rb,opcode)

def DEC_A(ra,rb):
    opcode="0111"
    ALU_template(ra,rb,opcode)

def INC_A(ra,rb):
    opcode="1000"
    ALU_template(ra,rb,opcode)

def MUL_A_C(ra,rb):
    opcode="1001"
    ALU_template(ra,rb,opcode)

def DIV_A_C(ra,rb):
    opcode="1010"
    ALU_template(ra,rb,opcode)

#======== Higher level functions ====================

def KEEP_IN_PLACE():
    """" cell JUMP-> cell JUMP
     keep program in one place, stops execution of RAM
     works only if CURRENT_CELL incremented properly
     DANGER! other jumps in program, desynchronize this function
     Todo: update CURRENT_CELL after each JUMP instruction
    """
    JUMP(hex3_from_int(CURRENT_CELL))

def DATA_INT(register,intVal):
    """"fills register with integerValue
     Parameters
    ----------
    register: register where we want to store value

    intVal: integer number we want to store on RAM, and then it will be loaded form there to specified register,
    when program runs

    """
    DATA(register, hex3_from_int(intVal))

#========== Live code section =====================
if __name__ == '__main__':
    #code_me("1","1111","010","001")
    #take_me("022")
    # ^- very primitive start :D

    codes=["022","011","066"]
    code_me("0", "0010", "000", "011")
    # for code in codes:
    #     take_me(code)

    take_me("082")
    # jak uzyskato poniej w lepszy sposb?
    # inkrementacja zajetej pamieci w zaleznosci od wykonanych zapisw wczesniej
    # ADDx(liczba A, liczba B) i zapis do rejestru "eax"
    # zapisz do rejestru A? podstwic symbole pod konkretne numery rejestrów
    # załaduj z rejestru do rejestru coś takiego eax=ebx
    # stwórz funkcje exit/zawieszenie KEEP_IN_PLACE do tego potrzebne inkrementacje pamięciowe
    if(False):
        #example of usage hex3_from_int(), int_from_hex3
        DATA("010","069") #rozmiar na 2 komorki pamieci
        DATA("011","044") #rozmiar na 2 komorki pamieci
        ADD("010","011") #rozmiar 1
        STORE_RESULTS("100","100") #rozmiar1
        print("Skacze na CELL: {0}".format(CURRENT_CELL))
        hexVal= hex3_from_int(CURRENT_CELL)
        print("Hexvalue : {0}".format(hexVal))
        intVal= int_from_hex3(hexVal)
        print("Int value : {0}".format(intVal))
        JUMP("006")
    else:
        DATA_INT(regC,105)
        DATA_INT(regD,68)
        #DATA(regC,"069") # same as above ( DATA_INT(regC,105)) :D !!!
        #DATA(regD,"044")
        ADD(regC,regD) #rozmiar 1
        STORE_RESULTS(regE,regE) #rozmiar1
        KEEP_IN_PLACE()

