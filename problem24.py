"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import numpy as np

num="0123456789"
size=len(num)
print("size\t",size)
#all_combination=[i+j+k+l+m+n+o+p+q+r for i in (num) for j in (num) for k in (num) for l in (num) for m in(num)for n in(num) for o in(num) for p in(num) for q in(num) for r in(num)if(np.size(np.unique([i,j,k,l,m,n,o,p,q,r]))==size)]#\
#        #for o in (num) for p in(num) for q in(num)]
##print("total combinations\t",all_combination)
##filter the unique values
#unique_combination=[i for i in (all_combination) if np.size(np.unique(list(i)))==size]
#print("unique combinations\t",unique_combination)
#print("========================================")
#print("unique numbers\n",len(unique_combination))
#print("millionth-number\t",unique_combination[1000000-1])

##Next method
#all_list=[]
#def permutations(string,step=0):
#    if step==len(string):
#        print ("".join(string)) #If step reaches to the end of string
#        all_list.append(int("".join(string)))
#    for i in range(step,len(string)):
#        string_copy=[c for c in string] #copy the string
#        string_copy[step],string_copy[i]=string_copy[i],string_copy[step]
#        permutations(string_copy,step+1)
#
#print(permutations(num))
#print("all_list\n++++++++++++++",all_list)
##sorted_list=sorted([int(i) for i in all
#target=1000000
#print("target\t",target)
#target=target-1
#print("target\t",target)
#
#print("millionth element\t",all_list[target])
#sorted_list=sorted(all_list)
#print("sorted millionth element\t",sorted_list[target])
#
#Using the built in method
from itertools import permutations
perms=[''.join(p) for p in permutations('0123456789')]
sort=sorted(perms)
print(sort[999999])
