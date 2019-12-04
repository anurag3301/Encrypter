def decToBin_8bit(val):
    binary = '00000000'

    if val >= 128:
        binary = binary[:0] + '1' + binary[:7]
        val -= 128
    else:
        binary = binary[:0] + '0' + binary[:7]
    if val >= 64:
        binary = binary[:1] + '1' + binary[:6]
        val -= 64
    else:
        binary = binary[:1] + '0' + binary[:6]
    if val >= 32:
        binary = binary[:2] + '1' + binary[:5]
        val -= 32
    else:
        binary = binary[:2] + '0' + binary[:5]
    if val >= 16:
        binary = binary[:3] + '1' + binary[:4]
        val -= 16
    else:
        binary = binary[:3] + '0' + binary[:4]
    if val >= 8:
        binary = binary[:4] + '1' + binary[:3]
        val -= 8
    else:
        binary = binary[:4] + '0' + binary[:3]
    if val >= 4:
        binary = binary[:5] + '1' + binary[:2]
        val -= 4
    else:
        binary = binary[:5] + '0' + binary[:2]
    if val >= 2:
        binary = binary[:6] + '1' + binary[:1]
        val -= 2
    else:
        binary = binary[:6] + '0' + binary[:1]
    if val >= 1:
        binary = binary[:7] + '1' + binary[:0]
        val -= 1
    else:
        binary = binary[:7] + '0' + binary[:0]
    return binary


def TwoCharToBin(val1, val2):
    binary = '00000000'
    if val1 >= 8:
        binary = binary[:0] + '1' + binary[:7]
        val1 -= 8
    else:
        binary = binary[:0] + '0' + binary[:7]
    if val1 >= 4:
        binary = binary[:1] + '1' + binary[:6]
        val1 -= 4
    else:
        binary = binary[:1] + '0' + binary[:6]
    if val1 >= 2:
        binary = binary[:2] + '1' + binary[:5]
        val1 -= 2
    else:
        binary = binary[:2] + '0' + binary[:5]
    if val1 >= 1:
        binary = binary[:3] + '1' + binary[:4]
        val1 -= 1
    else:
        binary = binary[:3] + '0' + binary[:4]
    if val2 >= 8:
        binary = binary[:4] + '1' + binary[:3]
        val2 -= 8
    else:
        binary = binary[:4] + '0' + binary[:3]
    if val2 >= 4:
        binary = binary[:5] + '1' + binary[:2]
        val2 -= 4
    else:
        binary = binary[:5] + '0' + binary[:2]
    if val2 >= 2:
        binary = binary[:6] + '1' + binary[:1]
        val2 -= 2
    else:
        binary = binary[:6] + '0' + binary[:1]
    if val2 >= 1:
        binary = binary[:7] + '1' + binary[:0]
        val2 -= 1
    else:
        binary = binary[:7] + '0' + binary[:0]
    return binary


def binToDec(binary):
    val = 0
    if binary[0] == '1':
        val += 128
    if binary[1] == '1':
        val += 64
    if binary[2] == '1':
        val += 32
    if binary[3] == '1':
        val += 16
    if binary[4] == '1':
        val += 8
    if binary[5] == '1':
        val += 4
    if binary[6] == '1':
        val += 2
    if binary[7] == '1':
        val += 1
    return val


def substitution(num):
    if num == 1:
        val = 14
    elif num == 2:
        val = 15
    elif num == 3:
        val = 5
    elif num == 4:
        val = 9
    elif num == 5:
        val = 11
    elif num == 6:
        val = 6
    elif num == 7:
        val = 13
    elif num == 8:
        val = 2
    elif num == 9:
        val = 4
    elif num == 10:
        val = 8
    elif num == 11:
        val = 1
    elif num == 12:
        val = 3
    elif num == 13:
        val = 10
    elif num == 14:
        val = 7
    elif num == 15:
        val = 12
    else:
        val = 0
    return val


def permutation(binaryIn):
    binary = '00000000'
    binary = binary[:0] + binaryIn[4] + binary[:7]
    binary = binary[:1] + binaryIn[7] + binary[:6]
    binary = binary[:2] + binaryIn[5] + binary[:5]
    binary = binary[:3] + binaryIn[2] + binary[:4]
    binary = binary[:4] + binaryIn[1] + binary[:3]
    binary = binary[:5] + binaryIn[3] + binary[:2]
    binary = binary[:6] + binaryIn[0] + binary[:1]
    binary = binary[:7] + binaryIn[6] + binary[:0]
    return binary


def binToDec_4Bit(binary):
    val = 0
    if binary[0] == '1':
        val += 8
    if binary[1] == '1':
        val += 4
    if binary[2] == '1':
        val += 2
    if binary[3] == '1':
        val += 1
    return val


def decToBin_4Bit(val):
    binary = '0000'
    if val >= 8:
        binary = binary[:0] + '1' + binary[:3]
        val -= 8
    else:
        binary = binary[:0] + '0' + binary[:3]
    if val >= 4:
        binary = binary[:1] + '1' + binary[:2]
        val -= 4
    else:
        binary = binary[:1] + '0' + binary[:2]
    if val >= 2:
        binary = binary[:2] + '1' + binary[:1]
        val -= 2
    else:
        binary = binary[:2] + '0' + binary[:1]
    if val >= 1:
        binary = binary[:3] + '1' + binary[:0]
        val -= 1
    else:
        binary = binary[:3] + '0' + binary[:0]
    return binary


def reversePermutation(binaryIn):
    binary = '00000000'
    binary = binary[:0] + binaryIn[6] + binary[:7]
    binary = binary[:1] + binaryIn[4] + binary[:6]
    binary = binary[:2] + binaryIn[3] + binary[:5]
    binary = binary[:3] + binaryIn[5] + binary[:4]
    binary = binary[:4] + binaryIn[0] + binary[:3]
    binary = binary[:5] + binaryIn[2] + binary[:2]
    binary = binary[:6] + binaryIn[7] + binary[:1]
    binary = binary[:7] + binaryIn[1] + binary[:0]
    return binary


def reverseSubstitution(num):
    if num == 1:
        val = 11
    elif num == 2:
        val = 8
    elif num == 3:
        val = 12
    elif num == 4:
        val = 9
    elif num == 5:
        val = 3
    elif num == 6:
        val = 6
    elif num == 7:
        val = 14
    elif num == 8:
        val = 10
    elif num == 9:
        val = 4
    elif num == 10:
        val = 13
    elif num == 11:
        val = 5
    elif num == 12:
        val = 15
    elif num == 13:
        val = 7
    elif num == 14:
        val = 1
    elif num == 15:
        val = 2
    else:
        val = 0
    return val


