#TASK 6:Using Python or PHP or Java or Ruby or JavaScript
#Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.


correct_password = "admin@123"
attempts = 4

for i in range(attempts):
    password = input("Enter your password: ")
    if password == correct_password:
        display="Access granted."
        break
    else:
        remaining_attempts=attempts-(i+1)
        print(f"incorrect password you have {remaining_attempts} attempts remaining")
        if remaining_attempts==0:
           display="account blocked"
            
        
print(display)

# while loop

correct_password = 'admin@123'
max_attempts = 4
attempts = 0

while attempts<max_attempts:
    password = input("Enter your password: ")
    if password==correct_password:
        display="access granted"
        break
    else:
        attempts+=1
        print(f"incorrect password you have {attempts} attempts remaining ")
        
if attempts==max_attempts:
    display = "Account Blocked"
    
    print(display)



