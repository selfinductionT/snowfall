from random import random, randint
import time

def s(x):                                                #  #  #
    b = [' ']*80                                          #   #
    for n in x:                                        ###  #  ###
        try:                                              #   #
            b[n] = '*'                                   #  #  #
        except IndexError:
            pass
    b = ''.join(b)
    return b

def coord():                                #  #  #
    x = []                                   #   #
    for i in range(randint(5, 9)):        ###  #  ###
        x.append(randint(0, 80))             #   #
    return(x)                               #  #  #

def house(str):
    while len(str)<24:                                #  #  #
        str.append(' '*24)                             #   #
    for i in range(7):                              ###  #  ###
        s = list(str[17+i])                            #   #
        for k in range(21):                           #  #  #
            s[k] = h[i][k]
        s = ''.join(s)
        str[17+i] = s
    return str

                                                     #  #  #
h = ['                  \\  ',                        #   #
    '     *            /  ',                       ###  #  ###
    '    /|\\        __||  ',                         #   #
    '   //|\\\\      /    \\ ',                      #  #  #
    '   //|\\\\     /   _  \\',
    '  ///|\\\\\\    |  | | |',
    '     |       |  | | |']
x = []                                 #  #  #
x.append(coord())                       #   #
row = 0                              ###  #  ###
                                        #   #
while 5>2:                             #  #  #
    b = []
    for t in range(len(x)):
        b.append(s(x[t]))
        for i in range(len(x[t])):
            q = int(random()*3)-1
            x[t][i] = x[t][i] + q                         #  #  #
    b = house(b)                                           #   #
    for i in range(24):                                 ###  #  ###
        print(b[i])                                        #   #
    time.sleep(0.2)                                       #  #  #
    row+= 1
    if row%2 == 0:
        x = [coord()] + x
    else:
        x = [[90]] + x
    if row == 150:
        x = x[:25]
        b = b[:25]
        row = 25
