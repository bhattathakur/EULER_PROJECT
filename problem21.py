"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
#returns the list of all properdivisor:
def properdivisor(n):
    divisor=[]
    for i in range(1,n//2+1):
        if n%i==0:divisor.append(i)
    return sum(divisor)

#list of numbers from 1 to 1000
#import numpy as np
#num_list=[i for i in range(2,10001,1)]

#chekcing the amicable numbers, removing from given list and adding to the new list
amicable_list=[]
i=2
limit=10000
while i<limit:
    prodivsum=properdivisor(i)
    prov=properdivisor(prodivsum)
    if prov==i and i!=prodivsum: #and prov in num_list and prodivsum in num_list:
        if i not in amicable_list:amicable_list.append(i)
        if prov not in amicable_list:amicable_list.append(prov)
    i+=1
print("amicable list\t",amicable_list)
print("sum of amicable list till\t",limit,"\t",sum(amicable_list))
