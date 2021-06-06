

def take_me():
    # XXX -> LOAD what from what, from where
    my_hex_data= "fa1"
    scale = 16
    num_of_bits = 12
    val= bin(int(my_hex_data, scale))[2:].zfill(num_of_bits)
    print(val)

    bit_0 = val[-12:-11:1]
    bit_opcode= val[-11:-7:1]
    bit_A= val[-6:-3:1]
    bit_B= val[-3:]
    if(bit_0 == "1"):
        print("ALU")
        if (bit_opcode == "0000"):
            print("ADD")
        elif (bit_opcode == "0001"):
            print("ADD_IM")
        elif (bit_opcode == "0010"):
            print("SUB_IM")
        elif (bit_opcode == "0011"):
            print("MUL_IM")
        elif (bit_opcode == "0100"):
            print("DIV_IM")
        elif (bit_opcode == "0101"):
            print("a2_b2")
        elif (bit_opcode == "0110"):
            print("COMPARE")
        elif (bit_opcode == "0111"):
            print("DEC_A")
        elif (bit_opcode == "1000"):
            print("INC_A")
        elif (bit_opcode == "1001"):
            print("MUL_A_C")
        elif (bit_opcode == "1010"):
            print("DIV_A_C")
        else:
            print("NOT DEFINIED")


    else:
        print("Not ALU")
        if(bit_opcode=="0000"):
            print("LOAD")
        elif(bit_opcode=="0001"):
            print("STORE")
        elif (bit_opcode == "0010"):
            print("DATA")
        elif (bit_opcode == "0011"):
            print("JMPR")
        elif (bit_opcode == "0100"):
            print("JUMP")
        elif (bit_opcode == "0101"):
            print("JMP_IF")
        elif (bit_opcode == "0110"):
            print("SET_IM")
        elif (bit_opcode == "0111"):
            print("STROE_RESULTS")
        elif (bit_opcode == "1000"):
            print("RESULT_FLG")
        elif (bit_opcode == "1001"):
            print("STROE_OVS")
        else:
            print("NOT DEFINIED")

    print("Reg A: " + bit_A)
    print("Reg B: " + bit_B)


def code_me():
    isALU= "1"
    operation= "001"
    regA= "000"
    regB = "010"

    hexik=isALU+operation+regA+regB
    print(hexik)
    print('%03X' % int(hexik, 2))


if __name__ == '__main__':
    #take_me()
    code_me()
