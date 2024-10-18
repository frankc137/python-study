fruits = ['mango',[1,2,3,4,5],'banana',100,30.5,False,True]

print(type(fruits))
#accessing elements inside a list
print(fruits[1])
#display True
print(fruits[-1])
#
print(fruits[1][4])

#modifying elements
fruits[0]='water melon'
print(fruits)
#list methods=>used to modify or manipulate data inside a list

# append => used to add elements at the end of the list
fruits.append("oranges")
#print(fruits)
# insert => add items to a specific index
fruits.insert(1,1000)
print(fruits)
#add apple at index 5

#remove => used to remove the "first" occurence of a specific element
num=[10,20,30,40,50,10,50]
#fruits.remove(10)
#print(num)
#remove 50

# pop => this removes items of a specific index
num.pop(0)
print(num)

#list slicing
#it is used to extract a subset of data from a list
print(num[0:3])

#len () => used to get length of a list
print(len(num))

# check if an element is inside a list
students=["maina","arnold", "frank","vera","abdi"]
#in used to check for the membership of an element
print("frank" in students)
print("peter" in students)
#concatenate list
lst1=[1,2,3,4,5]
lst2=[6,7,8,9,10]
lst3=lst1+lst2
print(lst3)

