#TASK 13: Using Python or PHP or Java or Ruby or JavaScript or C# or Go
#Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.

tries = 0
while tries < 3:
    email = input("Enter email: ")
    password = input("Enter password: ")
    if email == "admin@mail.com" and password == "Admin@123":
        print("Login is Successful")
        break
    else:
        tries += 1
        print("Invalid username or password")
        if tries == 3:  
            print("You have been blocked")
            break