"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
def PrimeChecker(num):
    if num<=1:
        return False
    if num<=3:
        return True
    if num%2==0 or num%3==0:
        return False
    i=5
    while(i*i<=num):
        if num%i==0 or num%(i+2)==0:
            return False
        i+=6
    return True

#Checking whether given number is prime or not
counter=0
sum=0
for i in range(2_000_000):
    if PrimeChecker(i):
        counter+=1
        sum+=i
        if counter%10==0:print()
        print(i,sep="\t",end="\t")
    #    print()
print("\nsum\t",sum)
