if 20>40:
    print('20 is greater')
else:
    print("20 is less than")
    
    # declare a valiable marks then check if the marks is above 50 and less than 100 print pass otherwise fail
marks = 30  
if marks > 50 and marks<100:
    print("Pass")
else:
    print("Fail")
    
    # declare a variable number then check if no. is even otherwise print odd
    num=60
if num%2==0:
    print('even')
else:
    print('odd')
    
    #You 
    #marks=
    #90=>100 (A) if
    #80=>90 (B) elif
    #70=>80(c) elif
    #60=>70(d)elif
    #50=>60 (e)elif
    #50 and below (fail) else
marks=int(input('enter marks:'))
if marks>=90 and marks<=100:
    print('A')
elif marks>=80 and marks<90:
    print('B')
elif marks>=70 and marks<80:
    print('C')
elif marks>=60 and marks<70:
    print('D')
elif marks>=50 and marks<60:
    print('E')
else:
    print('fail')
        
        #write a program that takes age from input
        #if age is above 60 or above  print you are older
        # if age is 18 and above print you are a adult
        # otherwise you are a minor
        
age=int(input('enter age:'))
if age>=60:
    print('You are older')
elif age>=18 and age<60:
    print('You are an adult')
else:
    print('You are a minor')
    
    # nested if statements
    # you give 100 discount on purchase above 1000
    # you give 
    
    
puchase=int(input('enter purchase'))
if puchase>1000:
    print('100 discount')
    if puchase>5000:
     print ('200 discount')
else:
    print ('no discount')
    #Write a program that takes users age as input 
    # if the age is 18 and above, check if the drivers license if they do print you are eligible to drive
    # if they dont have a drivers license print you are not eligible to drive
    # otherwise you are too young to drive
    age = int(input('enter your age:'))
    license= True
if age >=18:
    license=input("do you have a license yes/no:").lower().strip()
    if license =='yes' :
        print('you are eligible to drive')
    else:
        print('you are not eligible to drive')
else:
    print('you are too young to drive')
    
   # Write a program that:
#=>Takes the user's credit score and annual income as input.
#=>If the credit score is above 700, check if the income is above $50,000:
#=>If both conditions are met, print "Loan approved."
#=>If only the credit score is high, print "Income requirement not met."
#=>If the credit score is below 700, print "Credit score too low."


credit_score = int(input("Enter your credit score: "))
annual_income=int(input('enter your anual income: '))

if credit_score > 700:
    if annual_income > 50000:
      print("Loan approved.")
    else:
      print("Income requirement not met.")
else:
      print("Credit score too low.")



