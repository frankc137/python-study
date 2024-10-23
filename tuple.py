#create a tuple

marks=(100,300,250,160,450,600)
print(type(marks))
print(marks[5])
#convertining into a list
marks=list(marks)
print(type(marks))
#converting back into a tuple
marks=tuple(marks)
print(type(marks))

days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")
# 1. Find Wednesday using an index
wed = days[2]
print(wed)

# 2. Using a function, find the length of the tuple
length_of_days = len(days)
print(length_of_days)

# 3. Replace Thursday with Thur
#convert to a list
days=list(days)
days[3]="Thur"
#convert back to a tuple
days=tuple(days)
print(days)

my_tuple=("age",14,'location',"Kiambu",[100,300,500])
my_tuple[4][1]=1000
print(type(my_tuple))
