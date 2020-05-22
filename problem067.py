filename='p067_triangle.txt'
with open(filename) as f:
    string_list=f.read().splitlines()
#getting rid of empty lines
#given=[i for i in given if i]
#given string into the list form

#string_list=given.split("\n")
print("string_list",string_list)

#each string into list form
final_stringlist=[i.split() for i in string_list]

print("final string list\n",final_stringlist)

#changing the given string list into the integer list

int_list=[[int(i) for i in j]for j in final_stringlist]

print("integer list\t",int_list)

# manipulating the integer:

while len(int_list)>1:
    print("length of a string\t",len(int_list))
    current=int_list[len(int_list)-2]
    later=int_list[len(int_list)-1]

    print("current list\t",current)
    print("later list\t",later)

    update=[]
    for i in range(len(current)):
        value=current[i]+later[i] if current[i]+later[i]>current[i]+later[i+1] else current[i]+later[i+1]
        update.append(value)

    #removing last two members of the list
    for i in range(2):int_list.pop()

    #adding the updated list in the int list
    int_list.append(update)
print("int_list\t",int_list)

print("-------------------------------")
print("maximum path sum\t",int_list[0][0])
