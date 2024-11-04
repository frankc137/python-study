#1.Write a program that displays a numbers 1 to 50 inside a list.

numbers = list(range(1, 51))
print(numbers)

#2.From 1 above display the ones divisible by 7 or 5 inside a list.

divisible_seven_5=[ ]
for num in numbers:
    if num % 7 == 0 or num % 5 == 0:
        divisible_seven_5.append(num)
        
print(divisible_seven_5)

#3.Find sum and average of values in the range between 10 to 40.
num = list(range(10, 41))
sum = 0
count = 0
for i in num:
    sum+=i
    
average=sum/len(num)
print(sum)
print(average)


#4.Put in a list the first 10 odd numbers between 10 to 50. 

num=list(range(10,50))
odd_numbers=[ ]
for x in num:
    if x%2 !=0:
        odd_numbers.append(x)
        count+=1
        if count == 10:
            break
        
print(odd_numbers)


#5.write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.

num = int(input("Enter a number: "))
for i in range(0, 11):
    mult=num*i
    print(f"{num} x {i} = {num * i}")

#6.write a program that counts and prints the number of even numbers between 1 and 50 using a for loop

count = 0
for i in range(1, 51):
    if i % 2 == 0:
        count += 1
print(count)

#7.ls1 = [ (“Jay”, 20), (“Mo”, 30), (“Mya”, 32) ]
#Display the total quantity of the 3 above.

ls1 = [("Jay", 20), ("Mo", 30), ("Mya", 32)]
total_quantity = 0

for l in ls1:
    stock=l[1]
    total_quantity+=stock
print(total_quantity)