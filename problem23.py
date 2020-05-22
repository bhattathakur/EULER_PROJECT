"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
#returns sum of proper divisors of a given number

def sumproperdivisor(n):
    sum=0
    for i in range(1,n//2+1):
        if n%i==0:
            sum+=i
    return sum
abundant_list=[i for i in range(2,22000) if sumproperdivisor(i)>i]

sumofabundant=[]
limit=len(abundant_list)
for i in range(limit):
    print("run\t",i,"\n")
    for j in range(i,limit):
        check=abundant_list[i]+abundant_list[j]
        if check>28123:break
        if check not in sumofabundant:
            sumofabundant.append(check)
print('sum of abundant\t',sumofabundant)

