# TASK 11: Using Python or PHP or Java or Ruby or JavaScript
#Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days TODAY.

from datetime import datetime,date

dob=input('enter date of birth: ')
dob_split=dob.split('-')
# print(dob_split)
today=datetime.now()
# t_month=
today_month=today.month
today_year=today.year
today_day=today.day
print(today_day)

years = today_year-int(dob_split[0])
months = today_month-int(dob_split[1])
days= today_day - int(dob_split[2])
#print (type(today))
#age= today-dob
print(f"{years} yearsb,{months} months and {days} days")
