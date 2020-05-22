
"""
Loading the csv data file in panda framework
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename1='/home/thakur/PANDAS/pydata-book/examples/ex1.csv'

df=pd.read_csv(filename1)

filename2='/home/thakur/PANDAS/pydata-book/examples/ex2.csv'
df1=pd.read_csv(filename2,names=list('abcde'))

#reading the file csv_mindex.csv
filename3='/home/thakur/PANDAS/pydata-book/examples/csv_mindex.csv'
df3=pd.read_csv(filename3,index_col=['key1','key2'])

#reading the file ex3.txt
filename4='/home/thakur/PANDAS/pydata-book/examples/ex3.txt'

result=pd.read_csv(filename4,sep='\s+')
filename5='/home/thakur/PANDAS/pydata-book/examples/ex4.csv'
df4=pd.read_csv(filename5,skiprows=[0,2,3])

#example ex5.csv
filename5='/home/thakur/PANDAS/pydata-book/examples/ex5.csv'
result=pd.read_csv(filename5)

#check if the result is null

what=pd.isnull(result)

#reading a text file in pieces
pd.options.display.max_rows=10
filename6='/home/thakur/PANDAS/pydata-book/examples/ex6.csv'
result1=pd.read_csv(filename6)
#reading the text file in the given number of rows
read_rows=pd.read_csv(filename6,nrows=5)

#Writing the data in the files
output=read_rows.to_csv('my_test.csv')

