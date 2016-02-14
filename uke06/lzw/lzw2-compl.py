def code():
    '''
    Implements an initial table for LZW algorithm 
    '''
    table = {}
    table[1] = 'a'
    table[2] = 'b'
    table[3] = 'c'
    table[4] = 'd'
    table[5] = 'e'
    table[6] = 'f'
    table[7] = 'g'
    table[8] = 'h'
    table[9] = 'i'
    table[10] = 'j'
    table[11] = 'k'
    table[12] = 'l'
    table[13] = 'm'
    table[14] = 'n'
    table[15] = 'o' 
    table[16] = 'p'
    table[17] = 'q'
    table[18] = 'r'
    table[19] = 's'
    table[20] = 't'
    table[21] = 'u'
    table[22] = 'v'
    table[23] = 'w'
    table[24] = 'x'
    table[25] = 'y'
    table[26] = 'z'
    table[27] = 'A'
    table[28] = 'B'
    table[29] = 'C'
    table[30] = 'D'
    table[31] = 'E'
    table[32] = 'F'
    table[33] = 'I' 
    table[34] = 'J'
    table[35] = 'K'
    table[36] = 'L'
    table[37] = 'M'
    table[38] = 'N'
    table[39] = 'O'
    table[40] = 'P'
    table[41] = 'Q'
    table[42] = 'R'
    table[43] = 'S'
    table[44] = 'T'
    table[45] = 'U'
    table[46] = 'V'
    table[47] = 'W'
    table[48] = 'X'
    table[49] = 'Y'
    table[50] = 'Z'
    table[51] = '1' 
    table[52] = '2'
    table[53] = '3'
    table[54] = '4'
    table[55] = '5'
    table[56] = '6'
    table[57] = '7'
    table[58] = '8'
    table[59] = '9'
    table[60] = '0'    
    
    return table

def encode(message):
    table = code()
    string = ""
    code_for_string = []
    for byte in message:
        symbol = byte
        if (string + symbol) in table.values():
            string = string + symbol
        else:
            for k,v in table.iteritems():
                if v == string:
                    code_for_string.append(k)
            table[max(table.keys())+1] = string + symbol
            string = symbol
    for k,v in table.iteritems():
        if v == string:
            code_for_string.append(k)
    return code_for_string
    
    

def test():
    test_message = fo = open("compl1.txt", "r")
    test_message2 = fo2 = open("compl2.txt", "r")
    test_message3 = fo3 = open("compl3.txt", "r")
    test_message4 = fo4 = open("compl4.txt", "r")
    test_message5 = fo5 = open("compl5.txt", "r")
    test_message6 = fo6 = open("compl6.txt", "r")
    test_message7 = fo7 = open("compl7.txt", "r")
    test_message8 = fo8 = open("compl8.txt", "r")
    test_message9 = fo9 = open("compl9.txt", "r")
    print encode(test_message)
    print encode(test_message2)
    print encode(test_message3)
    print encode(test_message4)
    print encode(test_message5)
    print encode(test_message6)
    print encode(test_message7)
    print encode(test_message8)
    print encode(test_message9)
    
test()