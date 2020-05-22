"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def factorial(n):
    if n==1:return 1
    return n*factorial(n-1)

#getting the factorial of 100 and sum of digits

fact_100=factorial(100)
str_list=str(fact_100)
print("str_list",str_list)
digit_list=list(str_list)
int_list=[int(i) for i in digit_list]
print("int_list",int_list)
digitsum=sum(int_list)
print("digits_sum\t",digitsum)
