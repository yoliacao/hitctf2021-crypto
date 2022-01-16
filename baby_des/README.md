### Title
baby_des
### Desc
My sbox is so cooool!
try to decrypt and get flag!
ciphertext: e8e2d4985cbe22055041bba9dab1b5bb4ce2d6de4e27bdec4e648ebd3b5112f4
### Hints
1.This not a normal DES
2.Sbox is linear
3.https://crypto.stackexchange.com/questions/53751/non-linearity-of-an-sbox
flag = "HITCTF2021{Us3_N0n_L1n3ar_Sb0x!}"
### Writeup
这是一个线性sbox，这会导致密文之间出现出现线性关系，参考https://crypto.stackexchange.com/questions/53751/non-linearity-of-an-sbox
