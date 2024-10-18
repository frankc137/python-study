#1.Convert a float to an integer with an inbuilt function in Python
   #temp = 56.8926 to 57
temp = 56.8926
temp_rounded = round(temp)
print(temp_rounded) 

#2.Convert the float below to give the results as follows temp = 56.8926 to 56.89
temp = 56.8926
temp_rounded = round(temp, 2)  
print(temp_rounded)

#3. Convert the float below to give the results as follows
    #temp = 56.8926 to 56.893 
temp = 56.8926
temp_rounded = round(temp, 3) 
print(temp_rounded)

#4.Convert the float below to give the results as follows
#temp=56.8926 to 8.926 
#NB: Use string  slice & concatenation, but have result as float 
temp = 56.8926
#convert into a string
temp=str(temp)
print(type(temp))
#slice
#"56.8926"
temp=temp[3:]
print(temp)
#concat
#8926
print(temp[0])
print(temp[1:])
temp=temp[0]+"."+temp[1:]
print(temp)
#convert back  to float
temp=float(temp)

