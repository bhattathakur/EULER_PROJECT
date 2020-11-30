"""
Euler Problem 28
================
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
#libraries
import numpy as np

#dimension of the square matrix
size=1001

num=size*size+1
#define matrix with all 0 intilized
mat=np.zeros((size,size))

center=size//2
mat[center][center]=1
#print the initial matrix
print("original matrix\n",mat)
print("center\t",center,center)
#right=1;left=1;up=1;down=1;
right=left=up=down=center;

s="(x={},y={})"
s1="newx={},newy={}"
count=2
newx=center;newy=center
jump=1
while True:
    print("--"*40)
    #print("count\t",count)
    #print("left {}\t right {} \t up {} \t down {}".format(left,right,up,down))
    #jump=count
    #right from center to jump
    #print(s1.format(newx,newy))
    #print("right\t===========")
    tempy=newy+jump
    for i in range(newy+1,tempy+1):
        x=newx;y=i
        #print(s.format(x,y))
        mat[x][y]=count
        count+=1
        if count==num:break
    if count==num:break
    newy=tempy
    #print(s1.format(newx,newy))
    tempx=newx+jump
    #print("newx\t",newx)
    #down
    #print("down\t===========")
    for i in range(newx+1,tempx+1):
        x=i;y=newy
        mat[x][y]=count
        #print(s.format(x,y))
        if count==num:break
        count+=1
    if count==num:break
    newx=tempx
    jump+=1
    #print(s1.format(newx,newy))
    #print("left\t===========")
    tempy=newy-jump
    #print("newy\t",newy)
    for i in range(newy-1,tempy-1,-1):
        y=i;x=newx
        mat[x][y]=count
        #print(s.format(x,y))
        count+=1
        if count==num:break
    if count==num:break
    newy=tempy
    #print(s1.format(newx,newy))
    #print("up\t===========")
    tempx=newx-jump
    #print("tempx\t",tempx)
    for i in range(newx-1,tempx-1,-1):
        y=newy;x=i
        mat[x][y]=count
        #print(s.format(x,y))
        count+=1
        if count==num:break
    newx=tempx
    #print(s1.format(newx,newy))
    if count==num:break
    #newy=newy-jump
    jump+=1
    #newx=newx+jump+1
    #newy=newy+jump+1
    #for 
    #left+=1
    #count+=1
#print("final matrix\n",mat)
#getting the main diagonal sum
row,column=mat.shape
#print("row\t",row,"column\t",column)
mainsum=0
offsum=0
for i in range(row):
    for j in range(column):
        if i==j: mainsum+=mat[i][j]
        if i+j==size-1:
            #print("i+j\t",i+j)
            offsum+=mat[i][j]


print("main-sum\t",mainsum)
print("off-sum\t",offsum)
print("total-sum",mainsum+offsum-1)
#rowidx=np.arange(size)
#colidx=np.flip(np.arange(size))
#print("row-index\t",rowidx)
#print("col-index\t",colidx)
#new_off_sum=0
#
#for i in range(len(rowidx)):
#        new_off_sum+=mat[rowidx[i]][colidx[i]]
#print("new_off_sum\t",new_off_sum)

