"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
#returns sum of proper divisors of a given number
import math
def sumproperdivisor(n):
    sum=1 # 1 is already included here
    t=math.ceil(math.sqrt(n))
    for i in range(2,t):
        if n%i==0:
            sum+=i+n//i #note i+n//i both divisor and remainder both factors included
    return sum
abundant_list={i for i in range(1,28123) if sumproperdivisor(i)>i}
#print("abundant_list\n",abundant_list)
#print("total lengths",len(abundant_list))
abundant_sum={(i+j) for i in abundant_list for j in abundant_list if (i+j)<28123}
#print('abundant_sum_list\n',abundant_sum)
rest={i for i in range(1,28123) if i not in abundant_sum}
#print("rest\n",rest)
print("Total sum\n")
print(sum(rest))

#abundat_sum=[] #list of numbers which is the sum of two abundant numbers
#for i in abundant_list:
#    #print("i\t",i)
#    for j in abundant_list:
#        sum=i+j
#        #print("sum\t",sum)
#        if sum in abundant_list:
#            abundat_sum.append(sum)
#            abundant_list.remove(sum)
#    abundant_list.pop(0)
#print("pair-sum\n",abundat_sum)
#print("lengh pair-sum\t",len(abundat_sum))
#all_integers=[i for i in range(1,28124)]
#print("all-integer",all_integers)
#rest_integers=[i for i in all_integers if i not in abundat_sum]
#print("rest-integers",rest_integers)
##sum_all=sum(rest_integers)
#print("============================================================================")
#print("sum of all elements\n")
#sum=0
#for i in rest_integers:
#    sum+=i
#print("sum\t",sum)
#print("sum\t",sum(sum_all))

