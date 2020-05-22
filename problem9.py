"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
a=1 
while(a<1000):
    b=a+1
    for j in range(b,1000):
        c=j+1
        for k in range(c,1000):
            if a+j+k==1000 and a*a+j*j==k*k:
                print(a,"\t",j,"\t",k)
                print("product=\t",a*j*k)
    a+=1
