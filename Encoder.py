# Declarations #

import numpy
import matplotlib.pyplot as plt


def encoderfunc(textin, EC):
    # Version Selector(partial) #

    mode = '0010'
    l = len(textin)
    version = 0
    datacap = 0
    terminator = 0
    groups = 0
    gpoly = 0
    g1 = 0
    g2 = 0
    charcount = '{0:09b}'.format(l)
    if EC == 'Low':
        bits = [0, 1]
        if l < 25:
            version = 1
            datacap = 152
            groups = 1
            cwcount = 19
            eccw = 7
            gpoly = [0, 87, 229, 146, 149, 238, 102, 21]
        elif 25 <= l < 47:
            version = 2
            datacap = 272
            groups = 1
            cwcount = 34
            eccw = 10
            gpoly = [0, 251, 67, 46, 61, 118, 70, 64, 94, 32, 45]
        elif 47 <= l < 77:
            version = 3
            datacap = 440
            groups = 1
            cwcount = 55
            eccw = 15
            gpoly = [0, 8, 183, 61, 91, 202, 37, 51, 58, 58, 237, 140, 124, 5, 99, 105]
        elif 77 <= l < 114:
            version = 4
            datacap = 640
            groups = 1
            cwcount = 80
            eccw = 20
            gpoly = [0, 17, 60, 79, 50, 61, 163, 26, 187, 202, 180, 221, 225, 83, 239, 156, 164, 212, 212, 188, 190]
        elif 114 <= l < 154:
            version = 5
            datacap = 864
            groups = 1
            cwcount = 108
            eccw = 26
            gpoly = [0, 173, 125, 158, 2, 103, 182, 118, 17, 145, 201, 111, 28, 165, 53, 161, 21, 245, 142, 13, 102, 48,
                     227, 153, 145, 218, 70]
    elif EC == 'Medium':
        bits = [0, 0]
        if l < 20:
            version = 1
            datacap = 128
            groups = 1
            cwcount = 16
            eccw = 10
            gpoly = [0, 251, 67, 46, 61, 118, 70, 64, 94, 32, 45]
        elif 20 <= l < 38:
            version = 2
            datacap = 224
            groups = 1
            cwcount = 28
            eccw = 16
            gpoly = [0, 120, 104, 107, 109, 102, 161, 76, 3, 91, 191, 147, 169, 182, 194, 225, 120]
        elif 38 <= l < 61:
            version = 3
            datacap = 352
            groups = 1
            cwcount = 44
            eccw = 26
            gpoly = [0, 173, 125, 158, 2, 103, 182, 118, 17, 145, 201, 111, 28, 165, 53, 161, 21, 245, 142, 13, 102, 48,
                     227, 153, 145, 218, 70]
        elif 61 <= l < 90:
            version = 4
            datacap = 512
            groups = 1
            cwcount = 64
            eccw = 18
            gpoly = [0, 215, 234, 158, 94, 184, 97, 118, 170, 79, 187, 152, 148, 252, 179, 5, 98, 96, 153]
        elif 90 <= l < 122:
            version = 5
            datacap = 688
            groups = 1
            cwcount = 86
            eccw = 24
            gpoly = [24, 229, 121, 135, 48, 211, 117, 251, 126, 159, 180, 169, 152, 192, 226, 228, 218, 111, 0, 117,
                     232,
                     87, 96, 227, 21]
    elif EC == 'Quartile':
        bits = [1, 1]
        if l < 16:
            version = 1
            datacap = 104
            groups = 1
            cwcount = 13
            eccw = 13
            gpoly = [13, 74, 152, 176, 100, 86, 100, 106, 104, 130, 218, 206, 140, 78]
        elif 16 <= l < 29:
            version = 2
            datacap = 176
            groups = 1
            cwcount = 22
            eccw = 22
            gpoly = [0, 210, 171, 247, 242, 93, 230, 14, 109, 221, 53, 200, 74, 8, 172, 98, 80, 219, 134, 160, 105, 165,
                     231]
        elif 29 <= l < 47:
            version = 3
            datacap = 272
            groups = 1
            cwcount = 34
            eccw = 18
            gpoly = [0, 215, 234, 158, 94, 184, 97, 118, 170, 79, 187, 152, 148, 252, 179, 5, 98, 96, 153]
        elif 47 <= l < 67:
            version = 4
            datacap = 384
            groups = 1
            cwcount = 48
            eccw = 26
            gpoly = [0, 173, 125, 158, 2, 103, 182, 118, 17, 145, 201, 111, 28, 165, 53, 161, 21, 245, 142, 13, 102, 48,
                     227, 153, 145, 218, 70]
        elif 67 <= l < 87:
            version = 5
            datacap = 496
            groups = 2
            g1 = 15
            g2 = 16
            cwcount = 62
            eccw = 18
            gpoly = [0, 215, 234, 158, 94, 184, 97, 118, 170, 79, 187, 152, 148, 252, 179, 5, 98, 96, 153]
    elif EC == 'High':
        bits = [1, 0]
        if l < 10:
            version = 1
            datacap = 72
            groups = 1
            cwcount = 9
            eccw = 17
        elif 10 <= l < 20:
            version = 2
            datacap = 128
            groups = 1
            cwcount = 16
            eccw = 28
        elif 20 <= l < 35:
            version = 3
            datacap = 208
            groups = 1
            cwcount = 26
            eccw = 22
            gpoly = [0, 210, 171, 247, 242, 93, 230, 14, 109, 221, 53, 200, 74, 8, 172, 98, 80, 219, 134, 160, 105, 165,
                     231]
        elif 35 <= l < 50:
            version = 4
            datacap = 288
            groups = 1
            cwcount = 36
            eccw = 16
            gpoly = [0, 120, 104, 107, 109, 102, 161, 76, 3, 91, 191, 147, 169, 182, 194, 225, 120]
        elif 50 <= l < 64:
            version = 5
            datacap = 368
            groups = 2
            g1 = 11
            g2 = 12
            cwcount = 46
            eccw = 22
            gpoly = [0, 210, 171, 247, 242, 93, 230, 14, 109, 221, 53, 200, 74, 8, 172, 98, 80, 219, 134, 160, 105, 165,
                     231]

    if version == 1:
        remainder = 0
    else:
        remainder = 7

    print("version=" + str(version))
    print("datacap=" + str(datacap))
    print("groups=", groups)

    # String Split Function #

    def split(fn):
        while fn:
            yield fn[:2]
            fn = fn[2:]

    # Loop to convert characters to binary encoded data #

    a = list(split(textin))
    length = len(a)
    encoded = ''

    for i in range(0, length):
        a[i] = a[i].replace('0', '00').replace('1', '01').replace('2', '02').replace('3', '03').replace('4',
                                                                                                        '04').replace(
            '5', '05').replace('6', '06').replace('7', '07').replace('8', '08').replace('9', '09').replace('A', '10')
        a[i] = a[i].replace('B', '11').replace('C', '12').replace('D', '13').replace('E', '14').replace('F',
                                                                                                        '15').replace(
            'G', '16').replace('H', '17').replace('I', '18').replace('J', '19').replace('K', '20').replace('L', '21')
        a[i] = a[i].replace('M', '22').replace('N', '23').replace('O', '24').replace('P', '25').replace('Q',
                                                                                                        '26').replace(
            'R', '27').replace('S', '28').replace('T', '29').replace('U', '30').replace('V', '31').replace('W', '32')
        a[i] = a[i].replace('X', '33').replace('Y', '34').replace('Z', '35').replace(' ', '36').replace('$',
                                                                                                        '37').replace(
            '%', '38').replace('*', '39').replace('+', '40').replace('-', '41').replace('.', '42').replace('/',
                                                                                                           '43').replace(
            ':', '44')
        a[i] = a[i].replace('b', '11').replace('c', '12').replace('d', '13').replace('e', '14').replace('f',
                                                                                                        '15').replace(
            'g', '16').replace('h', '17').replace('i', '18').replace('j', '19').replace('k', '20').replace('l', '21')
        a[i] = a[i].replace('m', '22').replace('n', '23').replace('o', '24').replace('p', '25').replace('q',
                                                                                                        '26').replace(
            'r', '27').replace('s', '28').replace('t', '29').replace('u', '30').replace('v', '31').replace('w', '32')
        a[i] = a[i].replace('x', '33').replace('y', '34').replace('z', '35').replace('a', '10')

        if len(a[i]) == 4:
            a[i] = (int((a[i])[:2]) * 45) + (int((a[i])[2:5]))
            a[i] = '{0:011b}'.format(a[i])
        elif len(a[i]) == 2:
            a[i] = '{0:06b}'.format(int(a[i]))

        encoded = encoded + a[i]

    print("encoded=", encoded)
    datastring2 = (mode + charcount + encoded)
    dist = (datacap - len(datastring2))

    # Pad bits for short string #

    if dist >= 4:
        terminator = "0000"
    elif dist == 3:
        terminator = "000"
    elif dist == 2:
        terminator = "00"
    elif dist == 1:
        terminator = "0"
    elif dist == 0:
        terminator = ""

    datastring = (mode + charcount + encoded + terminator)
    dist2 = (datacap - len(datastring))
    l2 = len(datastring)

    pad = (8 - (l2 % 8))
    pad = "0" * pad
    datastring = datastring + pad
    extrapad = int((datacap - len(datastring)) / 8)

    # POTENTIAL PROBLEM HERE ##### LOOK AT INT ABOVE #############

    for i in range(1, extrapad + 1):
        if i % 2 == 1:
            datastring = datastring + "11101100"
        elif i % 2 == 0:
            datastring = datastring + "00010001"

    print("datastring=", datastring)

    # Creating a log antilog table #

    exp2int = [1]
    int2exp = [i for i in range(256)]

    for i in range(1, 256):
        b = exp2int[i - 1] * 2
        if b >= 256:  # XOR if result is larger than or equal to 256. Use ^^ to XOR two integers
            b = b ^ 285  # USED TO BE b^^285, bitwise xor#
        exp2int.append(b)
        int2exp[b] = i

    int2exp[0] = []  # setting zero blank
    int2exp[1] = 0  # 1 comes up at 255 again

    # Message Polynomial #

    line = datastring
    mpoly = [int(line[i:i + 8], 2) for i in range(0, len(line), 8)]
    print("mpoly=", mpoly)

    # Long Division #

    print("generator polynomial=", gpoly)
    print("message polynomial=", mpoly)

    def longdivision(steps, mpoly, gpoly):
        for i in range(0, steps):
            gap = len(mpoly) - len(gpoly)
            m = mpoly[0]
            m = int2exp[m]
            if gap > 0:
                newgpoly = [exp2int[(g + m) % 255] for g in gpoly] + [0] * gap
            else:
                newgpoly = [exp2int[(g + m) % 255] for g in gpoly]
            blank = []
            if gap < 0:
                mpoly = mpoly + [0] * abs(gap)
            for i in range(0, len(newgpoly)):
                b = [mpoly[i] ^ newgpoly[i]]  # More xor problems?
                blank = blank + b
            mpoly = numpy.trim_zeros(blank, trim='f')
        return mpoly

    # interleaving #

    if groups == 1:
        steps = len(mpoly)
        ecwords = longdivision(steps, mpoly, gpoly)
        print("ecwords=", ecwords)
        message = mpoly + ecwords
        message = ['{0:08b}'.format(i) for i in message] + [0] * remainder
        blank = ''
        for i in message:
            blank = blank + str(i)
        message = blank
        print("full message=", message)

    elif groups == 2:
        b1 = mpoly[0:g1]
        b2 = mpoly[g1:(2 * g1)]
        b3 = mpoly[(2 * g1):(2 * g1 + g2)]
        b4 = mpoly[(2 * g1 + g2):(2 * g1 + 2 * g2)]
        ec1 = longdivision(g1, b1, gpoly)
        ec2 = longdivision(g1, b2, gpoly)
        ec3 = longdivision(g2, b3, gpoly)
        ec4 = longdivision(g2, b4, gpoly)
        print("b1=", b1)
        print("b2=", b2)
        print("b3=", b3)
        print("b4=", b4)
        print("ec1=", ec1)
        print("ec2=", ec2)
        print("ec3=", ec3)
        print("ec4=", ec4)

        blank = []
        for i in range(g1):
            blank = blank + [b1[i]] + [b2[i]] + [b3[i]] + [b4[i]]
        itldata = blank + [b3[-1]] + [b4[-1]]

        blank = []
        for i in range(len(ec1)):
            blank = blank + [ec1[i]] + [ec2[i]] + [ec3[i]] + [ec4[i]]
        itlecw = blank

        message = itldata + itlecw
        message = ['{0:08b}'.format(i) for i in message] + [0] * remainder
        blank = ''
        for i in message:
            blank = blank + str(i)
        message = blank
        print("full message=", message)

    # Graphical Array #

    dimension = ((version - 1) * 4) + 21
    print("dimension  = ", dimension, "x", dimension)
    m = numpy.zeros([dimension, dimension])

    # Finder & Timing Pattern #

    for i in range(7):
        m[i][0:7] = 3
        m[i][-7:dimension] = 3
    for i in range(-1, -8, -1):
        m[i][0:7] = 3

    for i in range(1, 6):
        m[i][1:6] = 0
        m[i][-6:dimension - 1] = 0
    for i in range(-2, -7, -1):
        m[i][1:6] = 0

    for i in range(2, 5):
        m[i][2:5] = 3
        m[i][-5:dimension - 2] = 3
    for i in range(-3, -6, -1):
        m[i][2:5] = 3

    for i in range(8, dimension - 8, 2):
        m[i][6] = 3
        m[6][i] = 3

    # Data graphic #

    shift = 1
    direction = 1
    l = 0
    u = 0
    g = 1
    cap1 = (dimension - 9) * 2
    cap2 = dimension * 2
    count = 0
    counter = 0
    count3 = 0
    maxcount = ((dimension - 17) / 2) + 4
    maxcount3 = (dimension - 17) * 2
    maxcol = ((dimension - 7) / 2) - 1

    for pos, i in enumerate(message):
        if pos > ((dimension - 9) * 8):
            counter = counter + 1
        if pos > 0 and pos % cap1 == 0 and count < 4:
            count = count + 1
            shift = shift + 2
            direction = -direction
            g = -g
            u = u + g
        elif 4 <= count < maxcount and counter % cap2 == 0:
            count = count + 1
            shift = shift + 2
            direction = -direction
            g = -g
            u = u + g
        if (dimension - 1 - u) == 6:
            u = u + (1 * direction)
            counter = counter + 2
        if count == maxcol and counter % cap2 == 0:
            u = u + 8
            counter = counter + 14
            count = count + 1
        if count3 == maxcount3:
            shift = shift + 3
            direction = -direction
            g = -g
            u = u + g
        elif count3 > maxcount3 and count3 % maxcount3 == 0:
            shift = shift + 2
            direction = -direction
            g = -g
            u = u + g
        if count >= maxcol:
            count3 = count3 + 1
        m[dimension - 1 - u][dimension - shift - l] = int(i) + 1
        l = (l + 1) % 2
        u = u + (pos % 2) * direction

    # Masking #

    masknum = 0
    maskbin = [0, 0, 0]

    # maskbin=[0,0,1]
    def mask0(m):
        for r in range(dimension):
            for c in range(dimension):
                if m[r][c] == 1 or 2:
                    if (r + c) % 2 == 0:
                        if m[r][c] == 2:
                            m[r][c] = 1
                        elif m[r][c] == 1:
                            m[r][c] = 2

    def mask1(m):
        for r in range(dimension):
            for c in range(dimension):
                if m[r][c] == 1 or 2:
                    if r % 2 == 0:
                        if m[r][c] == 2:
                            m[r][c] = 1
                        elif m[r][c] == 1:
                            m[r][c] = 2

    mask0(m)
    # mask1(m)

    # Information Bits #

    gpoly = [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1]
    bitstring = bits + maskbin
    infostring = bitstring + [0] * 10
    infostring = numpy.trim_zeros(infostring[:5], trim='f') + infostring[5:]
    print("infostring=", infostring)

    if len(infostring) == 10:
        ecstring = infostring + [0]

    while len(infostring) >= 11:
        gap = len(infostring) - len(gpoly)
        if gap != 0:
            gpoly = gpoly + [0] * gap
        pos = 0
        for i, j in zip(infostring, gpoly):
            infostring[pos] = bool(i) ^ bool(j)
            pos = pos + 1
        infostring = numpy.trim_zeros(infostring, trim='f')
        ecstring = infostring
        print("ecstring=", ecstring)

    if len(ecstring) < 10:
        ecstring = (10 - len(ecstring)) * [0] + ecstring
    print("final ecstring=", ecstring)

    ecstring = bitstring + ecstring
    qrspec = [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
    pos = 0
    for i, j in zip(ecstring, qrspec):
        qrspec[pos] = (bool(i) ^ bool(j)) * 3
        pos = pos + 1
    formatstring = qrspec
    print("format string=", formatstring)

    if EC == 'L':
        if masknum == 0:
            formatstring = [3, 3, 3, 0, 3, 3, 3, 3, 3, 0, 0, 0, 3, 0, 0]
        elif masknum == 1:
            formatstring = [3, 3, 3, 0, 0, 3, 0, 3, 3, 3, 3, 0, 0, 3, 3]
    elif EC == 'M':
        if masknum == 0:
            formatstring = [3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0]
        elif masknum == 1:
            formatstring = [3, 0, 3, 0, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 3]
    elif EC == 'Q':
        if masknum == 0:
            formatstring = [0, 3, 3, 0, 3, 0, 3, 0, 3, 0, 3, 3, 3, 3, 3]
        elif masknum == 1:
            formatstring = [0, 3, 3, 0, 0, 0, 0, 0, 3, 3, 0, 3, 0, 0, 0]
    elif EC == 'H':
        if masknum == 0:
            formatstring = [0, 0, 3, 0, 3, 3, 0, 3, 0, 0, 0, 3, 0, 0, 3]
        elif masknum == 1:
            formatstring = [0, 0, 3, 0, 0, 3, 3, 3, 0, 3, 3, 3, 3, 3, 0]
    print("formatstring2=", formatstring)

    for pos, i in enumerate(range(-8, 0, 1)):
        m[8][i] = formatstring[(pos + 7)]
    for pos, i in enumerate(range(-1, -8, -1)):
        m[i][8] = formatstring[pos]
    for pos, i in enumerate([0, 1, 2, 3, 4, 5, 7, 8]):
        m[8][i] = formatstring[pos]
    for pos, i in enumerate([8, 7, 5, 4, 3, 2, 1, 0]):
        m[i][8] = formatstring[(pos + 7)]
    m[-8][8] = 3

    for i in range(dimension):
        for j in range(dimension):
            if m[i][j] == 1:
                m[i][j] = 0
            if m[i][j] == 2:
                m[i][j] = 3

    plt.matshow(m, fignum=None, cmap='Greys')
    plt.savefig("qrcode.png", format='png')
    plt.show()



