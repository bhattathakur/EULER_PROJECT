"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

#opening the text file and storing the names in the list
filename="p022_names.txt"
with open(filename) as f:
    namedata=f.read().replace('"',"").split(",")

#display the names
print("names\t",namedata[:10],"\n",namedata[-10:-1])

#sorting the names in alphabetical order
namedata_sorted=sorted(namedata)

#display some part of sorted data
print("sorted sample\t",namedata_sorted[:10],"\n",namedata_sorted[-10:-1])

#making a dictionary of letter to number
letter="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number=[i+1 for i in range(len(letter))]
#dictionary of letters and numbers
letter_dict=dict(zip(letter,number))

#dislay the letter dictionary

print(letter_dict)

#defining a function to change a word into corresponing value A-1 B-2 etc

def wordtonum(word):
    sum=0
    for w in word:
        sum+=letter_dict[w]
    return sum

# creating a dictionary of names, order and namevalue

final_dict={namedata_sorted[i]:[i+1,wordtonum(namedata_sorted[i])] for i in range(len(namedata_sorted))}

#print("final dictionary \t",final_dict())

#getting the multiplication of numbers in dictonary values:

value_list=list(final_dict.values())
print("value-list",value_list[:10])

#getting the sum of all the values
sum=0
for i in range(len(value_list)):
    sum+=value_list[i][0]*value_list[i][1]
print("sum\t",sum)
