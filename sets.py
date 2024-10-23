days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday","sunday","sunday","sunday")

#set methods
days.add('mon')
print(days)
#removes values on a set
days.remove("mon")

#adds more values
days.update(
    [1,2,3,4]
)
# .clear
days.clear()

#discard
days.discard()
print(days)