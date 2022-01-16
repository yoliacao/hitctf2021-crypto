#!/usr/bin/python2
from os import urandom
ROUNDS = 8

IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

IP_1 = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

E = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

P = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

PC_1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

PC_2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

R = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

def Mysbox(bits):
    a,b,c,d,e,f = (bits[0],bits[1],bits[2],bits[3],bits[4],bits[5])
    return [a^b,d^c^a,f^b^c,d^a,e^f]

def chr_to_bits(c):
    res = bin(ord(c))[2:]
    return map(int, list(res.rjust(8,'0')))

def str_to_bits(s):
    res = []
    for c in s:
        res.extend(chr_to_bits(c))
    return res

def bits_to_chr(bits):
    res = int(''.join(map(str, bits)), 2)
    return chr(res)

def bits_to_str(bits):
    res = ''
    for i in range(0, len(bits), 8):
        res += bits_to_chr(bits[i:i+8])
    return res

def xor_bits(l,r):
    return map(lambda (x,y):x^y, zip(l,r))

def F(hblk, subkey):
    bits = [hblk[x-1] for x in E]
    bits = xor_bits(bits, subkey)
    res = []
    for i in range(0, len(bits), 6):
        val = Mysbox(bits[i:i+6])
        res.extend(map(int, val))
    res = [res[x-1] for x in P]
    return res

def encrypt_block(blk, subkeys):
    assert len(blk)==8
    bits = str_to_bits(blk)
    bits = [bits[x-1] for x in IP]
    for i in range(ROUNDS):
        left = bits[:32]
        right = bits[32:]
        left = xor_bits(left, F(right, subkeys[i]))
        bits = right + left
    bits = left + right
    bits = [bits[x-1] for x in IP_1]
    return bits_to_str(bits)

def gen_subkey(key):
    kbits = str_to_bits(key)
    kbits = [kbits[x-1] for x in PC_1]
    left = kbits[:28]
    right = kbits[28:]
    subkeys = []
    for i in range(ROUNDS):
        left = left[R[i]:]+left[:R[i]]
        right = right[R[i]:]+right[:R[i]]
        cur = left+right
        subkeys.append([cur[x-1] for x in PC_2])
    if subkeys[0] == subkeys[1] or subkeys[0] == subkeys[2]:
        raise Exception("Boom")
    return subkeys

def encrypt(pt, key):
    assert len(pt)%8==0
    subkeys = gen_subkey(key)
    ct = ''
    for i in range(0, len(pt), 8):
        ct += encrypt_block(pt[i:i+8], subkeys)
    return ct

def decrypt_block(blk, subkeys):
    assert len(blk)==8
    bits = str_to_bits(blk)
    bits = [bits[x-1] for x in IP]
    for i in range(ROUNDS):
        left = bits[:32]
        right = bits[32:]
        left = xor_bits(left, F(right, subkeys[ROUNDS-1-i]))
        bits = right + left
    bits = left + right
    bits = [bits[x-1] for x in IP_1]
    return bits_to_str(bits)

def decrypt(ct, key):
    assert len(ct)%8==0
    subkeys = gen_subkey(key)
    pt = ''
    for i in range(0, len(ct), 8):
        pt += decrypt_block(ct[i:i+8], subkeys)
    return pt
def task():
    from secret import key,flag
    assert len(flag)==32
    #flag: HITCTF2021{xxxxxxxxxxxxxxxxxx}
    print encrypt(flag,key).encode('hex')
    #e8e2d4985cbe22055041bba9dab1b5bb4ce2d6de4e27bdec4e648ebd3b5112f4


if __name__ == '__main__':
    task()
