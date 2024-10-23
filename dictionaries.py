person={
    'name':"Frank",
    'age': 22,
    'gender': 'male',
    'location': ['kiambu',518,'Thika'],
    'address':{
        'street':'muthaiga',
        'city': 'nairobi',
        'country': 'Kenya',
    }
    
}

print(type(person))
print(person['name'])
#age
print(person['age'])
#gender
print(person['gender'])
#diplay 518
print(person['location'][1])
#display thika
print(person['location'][2])
#display city
print(person['address']['city'])
#display street
print(person['address']['country'])
#update values
person['age']=27
#location

#add new key and a value
person['occupation']='producer'
print(person)

    #dictionary methods
# .keys=> returns all the keys in the dictionary
print(person.keys())
# .values => returns all the values in the dictionary
print(person.values())
#  .items => returns a list of a key and value inside a tuple
print(person.items())

# pop=> removes the value with the specified key
person.pop('name')
print(person)
# remove occupation
person.pop('occupation')
print(person)

# .get() retrurn the value of a specific key
print(person.get('address'))


