"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

￼
How many such routes are there through a 20×20 grid?
"""
#Dimenstion of array
import numpy as np

grid_size=20
matrix=np.zeros((grid_size+1,grid_size+1))#dimension of matrix is 1 greater than the grid size

#setting the value of 1st column and 1st row to 1
matrix[:,0]=1
matrix[0,:]=1

#matrix
print(matrix)

#size of matrix
row,col=np.shape(matrix)
print("row\t",row)
print("col\t",col)

#counting the possible routtes
for i in range(1,row):
    for j in range(1,col):
        matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]

#final matrix
print(matrix)

#final result
print("total possible routes",matrix[grid_size][grid_size])
