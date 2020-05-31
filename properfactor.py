l=[]
def prop_func(n):
    for i in range(1,n//2+1):
        if(n%i==0):
            l.append(i)
    return (sum(l)==n)

print("numlist\t",prop_func(28))
#print("sumoflist\t",sum(prop_func(12)))
#print("sumoflist\t",sum(prop_func(28)))
#num_list=[(i==sum(prop_func(i))) for i in range(100) ]
#print("num_list\n",num_list)
lis=[(i+1) for i in range(30)]
sum_all=map(prop_func,lis)
#list=[0]*30
#for i in range(30):
#    test=prop_func(i+1)
#    list.append(test)
print("sum_all\n",list(sum_all))
        
