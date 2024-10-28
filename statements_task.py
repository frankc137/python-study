#1.Take three inputs from a user, separately. Print the largest of the numbers.
   # Hint: Determine what type of data is taken in as input.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
largest = max(num1, num2, num3)
print(largest)


#Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
#temperature = float(input("Enter the temperature in °C: "))
temperature=int(input())
if temperature > 30:
    print("The temperature is too high")
elif temperature > 15 and temperature<30:
    print("Normal temperature")
else:
    print("Cold temperature")
    
 #3.Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
  #and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

if 10 <= x <= 20 and y > 100:
    print("Conditions met")
else:
    print("Conditions not met")


#4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"

password = input("Enter the password: ")

if password == "secret123":
  print("Access granted")
else:
  print("Access denied")
 
# 5. Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"
student_score = float(input("Enter the student's score: "))
attendance = int(input("Enter the student's attendance percentage: "))

if student_score > 90:
    if attendance > 80:
        print("Excellent student")
    else:
        print("Good score, but attendance needs improvement")
else:
    print("fail")
 
 

 
amount = float(input("Enter the transaction amount: "))
account_type = input("Enter the account type (Standard/Premium): ").lower().strip()

if account_type == "Standard":
 if amount > 500:
  print("Transaction exceeds the limit for Standard accounts.")
 else:
  print("Transaction approved.")
elif account_type == "Premium":
 if amount > 1000:
  print("Transaction exceeds the limit for Premium accounts.")
 else:
    print("Transaction approved.")
else:
  print("Invalid account type.")

