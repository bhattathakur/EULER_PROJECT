"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
from functools import lru_cache
@lru_cache(maxsize=2000)
def fabonacci(n):
    if n<0:
        print("Error: input <0")
        return 
    if n==0:
        return 0 
    if n==1:
        return 1
    return fabonacci(n-1)+fabonacci(n-2) 
       
#checking the number of digits in fabonacci number
begin=0
index=0
while True:
    fab=fabonacci(begin)
    length=len(str(fab))
    print(fab,"\t",length,"\tindex\t",index)
    if length==1000:
        print("required number\t",fab,"\tindex\t",index)
        break
    begin+=1
    index+=1
