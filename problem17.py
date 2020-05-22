"""
f the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""
# create the dictionary of unique keyy
# create a function to convert the numbers and express in a list of strings
# get sum of the each string in a list

#dictionary of unique words
keyy1=[i for i in range(1,21)]
keyy2=[i for i in range(21,100) if i%10==0]
print("list1\t",keyy1)
print("list2\t",keyy2)
#adding uniqe keyy
keyys=keyy1+keyy2
keyys.append(100)
keyys.append(1000)
print("keyy\t",keyys)

#values list
valuess=['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen',
        'seventeen','eighteen','nineteen','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety','one hundred','one thousand']
print("values\t",valuess)

#Defining the dictionary of words
numdict=dict(zip(keyys,valuess))
print(numdict)

#Function to change number to words
final_dict={}
def change(num):
    if num in numdict:
        final_dict[num]=numdict[num]
    elif len(str(num))<=2:
        tens=num//10*10;ones=num%10
        final_dict[num]=numdict[tens]+" "+numdict[ones]
    else:
        hund=int(str(num)[0])
        rem=num%100
        final_dict[num]=numdict[hund]+" hundred and "+final_dict[rem] if rem>0 else numdict[hund]+" hundred"
for i in range(1,1001,1):
    change(i)
#Prining the values of string numbers in list

string_list=list(final_dict.values())
print("string list of numbers\t",string_list)

#getting rid of spaes in string and store them in a number list
num_list=[len(i.replace(" ","")) for i in string_list]

#printing the number list
print(num_list)

#sum of all the list
print("total length\t",sum(num_list))
