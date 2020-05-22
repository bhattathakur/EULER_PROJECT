#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) 
contains 10 terms. Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import time
# from functools import lru_cache
# @lru_cache(maxsize=1000000)

def collatzsequence(num,count=1):
    if num<=0:
        print("invalid input")
        return 
    #print("counter:\t",count,"\tinput:\t",num)
    if count==1:print("input\t",num)
    #while num!=1:
    if num>1:
        num=3*num+1 if num%2 else num/2
    #counter+=1
    if num==1:
        print("total count\t",count)
        return count+1
    #if num>1:
    #value=collatzsequence(num,count)
    #if value==1:return
    
    count+=1
    #return value
    return collatzsequence(num,count)
#Counting the number of terms in collatz sequence
# def collatzcounter(num):
#     counter=1
#     collatzsequence(num,counter)
#     return counter
#using the function for the numbers from 1 to 1 million
#start_time=time.time()
import numpy as np
limit=1000000
# array_list=np.arange(1,limit+1,1)#1 million
# result=np.vectorize(collatzsequence)(array_list)
# print("maximum series length\t",np.max(result))
# print("maximum value to series\t",np.argmax(result)+1)
# end_time=time.time()
# print("time taken\t",end_time-start_time)
#########################################
#new method as hinted
def newmethod(n,mydict={}):
    if n in mydict:return n
    if n==1:return 1
    if n%2==0:
        mydict[n]=1+newmethod(n/2)
        return 1+newmethod(n/2)
    else:
        mydict[n]=1+newmethod(3*n+1)
        return 1+newmethod(3*n+1)
# start_time=time.time()
# for i in range(500000,1000000):
#     print(i,"\t",newmethod(i))
# print("time required:\t",time.time()-start_time)