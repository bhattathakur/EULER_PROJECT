#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""
number=2
calculated=2**1000
calculatedstring=str(calculated)
stringlist=list(calculatedstring)
numberstringlist=[int(i) for i in stringlist]
toal=sum(numberstringlist)
print("sum\t",toal)
