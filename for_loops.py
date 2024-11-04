fruits=['apple','banana','cherry','avocado']

for fruit in fruits:
    if fruit=='banana':
        print(fruit)
        
# range function => used to create a list of numbers

x=[1,2,3,4,5,6,7,8,9,10]
y=list (range(1,11))

num=list(range(1,1000))
print(num)

z=list(range(101))

#iterate through numberrs from 20 to 100

c=list(range(20,101))

for num in c:
    print(num)
    
for num in range(20,101):
    print(num)
        
#iterate through numberrs from 20 to 100 and only display even numbers
        
numbers=list(range(20,101))

for i in numbers:
    if i%2==0:
        even_numbers.append(i)
        
print(even_numbers)

#break => used to stop the loop


        