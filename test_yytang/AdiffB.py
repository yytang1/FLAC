#!/usr/bin/python
# -*- coding: UTF-8 -*-


def getdiff(A, B):
    outAB = AdiffB(A, B)
    outBA = AdiffB(B, A)
    return outAB, outBA


def AdiffB(A, B):
    C = A[:]
    for i in B:
        if i in C:
            C.remove(i)
            #break
    return C


if __name__ == "__main__":
    A1 = [1, 2, 2, 2, 3, 4, 5, 6]
    B1 = [1, 2, 3, 4, 6, 7]
    out1, out2 = getdiff(A1, B1)
    print(A1)
    print(B1)
    print(out1)
    print(out2)
