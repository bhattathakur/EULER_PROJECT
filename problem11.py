"""
In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
"""
gridstring="""
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
"""
grid_string_list=gridstring.split()
grid_string_list=[int(i) for i in grid_string_list]#changing string numbers into intergers
#print(grid_string_list)
print("list number\t",len(grid_string_list))
#Putting the given list of string into two dimensional array
nrow,ncolumn=20,20
import numpy as np
import pandas as pd
twodilist=np.array(grid_string_list).reshape(nrow,ncolumn)
print("two-dimensional array\n",twodilist)

#checking the first diagonal
def checkdiagonal1(i,j):
    if (((i-3)>=0) and ((j-3)>=0)):
        return True

#checking the second diagonal
def checkdiagonal2(i,j):
    if (((i-3)>=0) and ((j+3)<20)):
        return True

#checking the third diagonal
def checkdiagonal3(i,j):
    if (((i+3)<20) and ((j-3)>=0)):
        return True

#checking the fourth diagonal
def checkdiagonal4(i,j):
    if (((i+3)<20) and ((j+3)<20)):
        return True
    
#checking the left 
def checkleft(i,j):
    if (((i)>=0) and ((j-3)>=0)):
        return True

#checking the right 
def checkright(i,j):
    if (((i)>=0) and ((j+3)<20)):
        return True

#checking the up 
def checkup(i,j):
    if (((i-3)>=0) and ((j)>=0)):
        return True

#checking the down 
def checkdown(i,j):
    if (((i+3)<20) and ((j)>=0)):
        return True
#To test whether each testing functions are working properly
logiclist=[]
for i in range(20):
    for j in range(20):
        logiclist.append(checkdown(i,j))
########################################
#getting the sum of each valid element with other 4 adjacennt members(up,down,right,left,diagonal(4))

def getSumall(i,j):
    max_sum=1
    #1st diagonal sum
    if(checkdiagonal1(i,j)):
        sum1=twodilist[i-3][j-3]*twodilist[i-2][j-2]*twodilist[i-1][j-1]*twodilist[i][j]
        print("sum1\t",sum1)
        if(sum1>max_sum):max_sum=sum1

    #2nd diagonal sum
    if(checkdiagonal2(i,j)):
        sum2=twodilist[i-3][j+3]*twodilist[i-2][j+2]*twodilist[i-1][j+1]*twodilist[i][j]
        print("sum2\t",sum2)
        if(sum2>max_sum):max_sum=sum2

    #3nd diagonal sum
    if(checkdiagonal3(i,j)):
        sum3=twodilist[i+3][j-3]*twodilist[i+2][j-2]*twodilist[i+1][j-1]*twodilist[i][j]
        print("sum3\t",sum3)
        if(sum3>max_sum):max_sum=sum3

    #4th diagonal sum
    if(checkdiagonal4(i,j)):
        sum4=twodilist[i+3][j+3]*twodilist[i+2][j+2]*twodilist[i+1][j+1]*twodilist[i][j]
        print("sum4\t",sum4)
        if(sum4>max_sum):max_sum=sum4

    #left sum
    if(checkleft(i,j)):
        sum5=twodilist[i][j-3]*twodilist[i][j-2]*twodilist[i][j-1]*twodilist[i][j]
        print("sum5\t",sum5)
        if(sum5>max_sum):max_sum=sum5

    #right sum
    if(checkright(i,j)):
        sum6=twodilist[i][j+3]*twodilist[i][j+2]*twodilist[i][j+1]*twodilist[i][j]
        print("sum6\t",sum6)
        if(sum6>max_sum):max_sum=sum6

    #up sum
    if(checkup(i,j)):
        sum7=twodilist[i-3][j]*twodilist[i-2][j]*twodilist[i-1][j]*twodilist[i][j]
        print("sum7\t",sum7)
        if(sum7>max_sum):max_sum=sum7

    #down sum
    if(checkdown(i,j)):
        sum8=twodilist[i+3][j]*twodilist[i+2][j]*twodilist[i+1][j]*twodilist[i][j]
        print("sum8\t",sum8)
        if(sum8>max_sum):max_sum=sum8
    return max_sum

#list stores the sum achieved for each member
sum_list=[]        
for i in range(20):
    for j in range(20):
        sum_list.append(getSumall(i,j))
        #getSumall(i,j)
print(sum_list)

#gives maximum value in the list
print("max\t",max(sum_list))
