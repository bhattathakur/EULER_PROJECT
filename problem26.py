"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
import numpy as np
from decimal import *
getcontext().prec=200

#check the arithmetic series 
def arithmetic_check(series):
    """
    Checks if the given series is in the arithmetic series
    """
    d=series[1]-series[0]
    a=series[0]
    next_series=[a+(i-d) for i in series]
    print("next-series\n",next_series)
    print("org-series\n",series)
    num2=np.array(series)
    num1=np.array(next_series)
    num3=num2-num1
    return np.sum(num3)==0
def get_max_length(arr,st):
    """
    returns the length of longest recurring part in the decimal for the given array list of indices
    """
    #array to string
    #st=''.join([str(i) for i in arr])
    print("array\t",arr)
    print("string from array\t",st)
    for i in range(1,len(arr)-1):
        d1=arr[i+1]-arr[i]
        d2=arr[i]-arr[i-1]
        s1=st[arr[i-1]:arr[i]]
        s2=st[arr[i]:arr[i+1]]
        #print("d1\t",d1)
        #print("d2\t",d2)
        #print("s1\t",s1)
        #print("s2\t",s2)
        if((d1==d2) and (s1==s2)):
            return d1
        
def getotherindex(num):
    """
    gives the indices of  all the other location of the provided letter in a string as a list 
    """
    for i in range(len(num)):
        num_array=np.array(list(num))
        counted_list=num_array[0:i]
        if num_array[i] in counted_list:continue
        index_list=np.where(num_array==num_array[i])[0].tolist()
        if len(index_list)<3:continue
        print('index-list\t:{}\t{}'.format(num_array[i],index_list))
        diff_list=[]
        for i in range(1,len(index_list)):diff_list.append(index_list[i]-index_list[i-1])
        print("difference-list\n",diff_list)
        print("*********************")

        #checking the condition from the array
        st_left=num[index_list[0]:]
        print("left_str\t",st_left)
        print()
        print("@@@@@@@@@@@@@@@@ recurring length \t",get_max_length(index_list,st_left))
        print()
   # return get_max_length(index_list,st_left)

        #if(len(index_list))>=3:
        #    diff=((index_list[2]-index_list[1])==(index_list[1]-index_list[0]))
            #string_list="".join([str(i) for i in(index_list)])
        #    first_string=num[index_list[1]:index_list[2]]
        #    rest_string=num[index_list[2]:]
            #if first_string in rest_string:
            #    print ("match-\t",first_string)
            #second_string=num_str[index_list[2]:index_list[3]]
            #print("first string {}\t\nsecond string\t{}".format(first_string,second_string))
            #print("string_back\t",string_list)
            #string_diff=(string_list[1:2]==string_list[2:3])
            #print(string_diff)
         #   check_in=first_string in rest_string
         #   if diff and check_in:
         #       return index_list

def getdecimalpart(num):
    """
    gives the decimal part of the number in the string form

    """
    division=Decimal(1)/Decimal(num)
    division_str=str(division)
    #print('with deciaml\t\t',division_str)
    point_pos=division_str.find('.')
    return division_str[point_pos+1:]
def getworkinglist(array_list):
    """
    returns the unique values and corresponding counts in the given array
    """
    array,count=np.unique(array_list,return_counts=True)
    print("array\t",array)
    print("count\t",count)

#def count_recurring_digits(num):
#    divide=Decimal(1)/Decimal(num)
#  #  print("divide\t",divide)
#    divide_str=str(divide)
#    point_pos=divide_str.find('.')
#    after_point=divide_str[point_pos+1:]
#  #  print("left str\t",after_point)
#    array,count=np.unique(list(after_point),return_counts=True)
#    print("#############################################################")
#    print("num\t",num)
#    print("decimal\t",divide)
#    print("after-decimal\t",after_point)
#    print("array\n",array)
#    print("unique\n",count)
#    print("max-unique\n",np.max(count))
#    #print("#############################################################")
#    #return divide,after_point,str(set(after_point)),len(set(after_point))
#print("=======================================================\n")
##for i in range(1,30+1):print("num\n",count_recurring_digits(i),"\n")
#test_num=28
recurring_list=[]
for i in range(1,1000+1):
    print("------------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------------------")
    print("                          WORKING ON {} VALUE".format(i))
    print("------------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------------------")
    test_num=i
    decimal_part_string=getdecimalpart(test_num)
    recurring=getotherindex(decimal_part_string)
    print("after decimal of {:} = \t   {:}".format(test_num,decimal_part_string))
    print("other matching index of firt letter\t",recurring)
   # recurring_list.append(recurring) 

    #decimal_list=list(decimal_part_string)
    #getworkinglist(decimal_list)

    #print("true-false\t",arithmetic_check(getotherindex(decimal_part_string)))
    #print("get-index of {}\t{}".format(test_num,getotherindex(i)))
#print("checking the fuction get indics\n")
#print("FINAL LIST\n")
#print(recurring_list)
#print("maximum-recurring\t",max(filter(None,recurring_list)))
#modified=[0 if i is None else i in recurring_list]
#print(getotherindex('12331'))
#print(getdecimalpart(test_num))
#dummy=[i for i in range(5,40,5)]
#print("dummy\t",dummy)
#
#
#print(arithmetic_check(dummy))
