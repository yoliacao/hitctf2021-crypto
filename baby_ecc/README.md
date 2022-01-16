### 题目：baby_ecc
### 描述：what is ECC？
very easy ecc puzzle,sage is helpful.
### Hints:
1.try to figure out the base multiple function in ecc.
2.try to discrete the puzzle in sage. bruteforce is very hard,try to discrete.
flag: HITCTF2021{babeecc13c001}
### Writeup
题目考察最基本的ecdlp问题，主要是希望选手熟悉椭圆曲线的基本概念和sage的使用。
由于明文很小（<1048575），使用sage的discrete_log函数，可以直接分解，也可以手动写算法恢复，暴力尝试会很慢，但是也可以。

