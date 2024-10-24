my_ds = [23, "Jane", 560, ["Lesson", "Maths", {"currency": "KES"}], 987, (76, "John")]

# 1. Print KES
currency = my_ds[3][2]["currency"]
print( currency)

# 2. Print 560
print(my_ds[2])

# 3. Print Maths
subject = my_ds[3][1]
print( subject)

# 4. In the dictionary with the key currency, add another key “amount” with value 90
my_ds[3][2]["amount"] = 90
print(my_ds[3][2])

# 5. Reverse 987 to 789 without using an inbuilt method or assigning 789 manually
# find the index of 987
# convert into a string for you to reverse
my_ds[4]= str(my_ds[4])
# reverse the string
my_ds[4]=my_ds[4][::-1]
# convert back to integer
my_ds[4]=int(my_ds[4])
# print the final output
print(my_ds)

# 6. Change the name “John” to “Jane”
my_ds[5] = list(my_ds[5])
my_ds[5][1]='jane'
my_ds[5]=tuple(my_ds[5])
print(my_ds)