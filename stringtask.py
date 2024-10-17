1. #Clean up the following variable to give the clean version in 
   # lower case. Using inbuilt methods in the str class name = “ JOHn .“ to “john” 
name = "  JOHn   "
#step
clean_name = name.strip().lower().replace('.', '')
cleanName = clean_name.capitalize()
print(cleanName) 

2. #Slice the below string to get you the resulting sentence:
# (a.) sentence_one = "The Dog Breed is German Shepherd” only display “Breed is German” 

sentence_one = "The Dog Breed is German Shepherd"
result_one = sentence_one[8:24] 
print(result_one)
# (b.)sentence_two = “Defeats for the Clinton forces,this was her moment of triumph” only display “Clinton forces”

sentence_two = "Defeats for the Clinton forces, this was her moment of triumph"
result_two = sentence_two[16:30]  
print(result_two) 

3. #Split the below sentence using a semicolon i.e ; And display length of the result. 
# “The lazy dog; ran so fast; it hit the wall.” 

sentence = "The lazy dog; ran so fast; it hit the wall."
result = sentence.split(";")
print(result)

4. #first_name=" Joh.n" last_name=" Do,e" Clean up and display Full name i.e John Doe 

first_name = "  Joh.n"
last_name = "   Do,e"
first_name = first_name.strip().replace('.','')
last_name = last_name.strip().replace(',','')
full_name = first_name + " " + last_name
print(full_name)

5.#Having the string r = '["E","W","C"]' #Manipulate it to display EWC
r = '["E","W","C"]'
r2 = r.replace('[','').replace(']','').replace('"','').replace(',','')
print(r2) 

